#!/usr/bin/env python3
"""
Minimal image-to-image helper for the image-style-transfer skill.

Standard library only — no pip install required. Talks to any
OpenAI-compatible `/v1/images/edits` endpoint, which covers the OpenAI
Images API as well as the many compatible gateways.

Environment:
    OPENAI_API_KEY    required  — your API key
    OPENAI_BASE_URL   optional  — default https://api.openai.com/v1
    IMAGE_MODEL       optional  — default gpt-image-1

Usage:
    python3 generate.py --image photo.jpg \\
        --prompt "Chinese ink wash painting, xieyi brushwork, ..." \\
        --out generated-images/ink.png --size 1536x1024

    # gateways that expose an explicit strength knob
    python3 generate.py --image photo.jpg --prompt "..." \\
        --out generated-images/x.png --extra strength=0.6

    # keep the source aspect ratio
    python3 generate.py --image photo.jpg --prompt "..." \\
        --out generated-images/x.png --match-aspect

Exit codes:
    0 success · 2 bad arguments / missing key · 3 HTTP error · 4 unusable response
"""

import argparse
import base64
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
import uuid

DEFAULT_BASE = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
DEFAULT_MODEL = os.environ.get("IMAGE_MODEL", "gpt-image-1")


def build_multipart(fields, files):
    """files: {name: (filename, bytes, content_type)}"""
    boundary = uuid.uuid4().hex
    chunks = []
    for key, value in fields.items():
        chunks.append(
            ('--%s\r\nContent-Disposition: form-data; name="%s"\r\n\r\n%s\r\n'
             % (boundary, key, value)).encode("utf-8")
        )
    for key, (filename, data, content_type) in files.items():
        chunks.append(
            ('--%s\r\nContent-Disposition: form-data; name="%s"; filename="%s"\r\n'
             'Content-Type: %s\r\n\r\n' % (boundary, key, filename, content_type)).encode("utf-8")
        )
        chunks.append(data)
        chunks.append(b"\r\n")
    chunks.append(("--%s--\r\n" % boundary).encode("utf-8"))
    return b"".join(chunks), "multipart/form-data; boundary=%s" % boundary


def match_aspect_size(path, base_long_edge=1536):
    """Pick the closest of the API's supported sizes to the source aspect ratio."""
    try:
        from PIL import Image  # optional, only used for this convenience flag
        with Image.open(path) as im:
            w, h = im.size
    except Exception:
        return "1024x1024"
    ratio = w / float(h)
    candidates = [
        ("1024x1024", 1.0),
        ("1536x1024", 1.5),
        ("1024x1536", 1.0 / 1.5),
    ]
    return min(candidates, key=lambda c: abs(c[1] - ratio))[0]


def main():
    ap = argparse.ArgumentParser(description="Image-to-image via an OpenAI-compatible API.")
    ap.add_argument("--image", required=True, help="source image path (the user's original)")
    ap.add_argument("--prompt", required=True, help="the assembled style prompt")
    ap.add_argument("--out", required=True, help="output image path")
    ap.add_argument("--size", default=None, help="e.g. 1024x1024 / 1536x1024 / 1024x1536")
    ap.add_argument("--quality", default="high", help="low / medium / high (provider permitting)")
    ap.add_argument("--model", default=DEFAULT_MODEL, help="image model name")
    ap.add_argument("--n", type=int, default=1, help="number of images (default 1)")
    ap.add_argument("--match-aspect", action="store_true",
                    help="choose the supported size closest to the source aspect ratio (needs Pillow)")
    ap.add_argument("--extra", action="append", default=[], metavar="KEY=VALUE",
                    help="extra form field, repeatable (e.g. --extra strength=0.6)")
    args = ap.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("error: OPENAI_API_KEY is not set", file=sys.stderr)
        return 2

    if not os.path.isfile(args.image):
        print("error: source image not found: %s" % args.image, file=sys.stderr)
        return 2

    size = args.size
    if size is None:
        size = match_aspect_size(args.image) if args.match_aspect else "1024x1024"

    with open(args.image, "rb") as fh:
        image_bytes = fh.read()
    content_type = mimetypes.guess_type(args.image)[0] or "image/png"
    filename = os.path.basename(args.image)

    fields = {
        "model": args.model,
        "prompt": args.prompt,
        "size": size,
        "n": str(args.n),
    }
    if args.quality:
        fields["quality"] = args.quality
    for item in args.extra:
        if "=" not in item:
            print("error: --extra expects KEY=VALUE, got %r" % item, file=sys.stderr)
            return 2
        k, v = item.split("=", 1)
        fields[k] = v

    body, ctype = build_multipart(fields, {"image": (filename, image_bytes, content_type)})
    url = "%s/images/edits" % DEFAULT_BASE
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", ctype)
    req.add_header("Authorization", "Bearer %s" % api_key)

    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        print("error: HTTP %s from %s\n%s" % (exc.code, url, detail), file=sys.stderr)
        return 3
    except urllib.error.URLError as exc:
        print("error: could not reach %s — %s" % (url, exc.reason), file=sys.stderr)
        return 3

    data = payload.get("data") or []
    if not data:
        print("error: no image data in response:\n%s" % json.dumps(payload)[:2000], file=sys.stderr)
        return 4

    os.makedirs(os.path.dirname(os.path.abspath(args.out)) or ".", exist_ok=True)
    saved = []
    for index, item in enumerate(data):
        target = args.out if index == 0 else "%s.%d%s" % (os.path.splitext(args.out)[0], index,
                                                          os.path.splitext(args.out)[1])
        if item.get("b64_json"):
            with open(target, "wb") as fh:
                fh.write(base64.b64decode(item["b64_json"]))
        elif item.get("url"):
            with urllib.request.urlopen(item["url"], timeout=300) as resp:
                with open(target, "wb") as fh:
                    fh.write(resp.read())
        else:
            print("error: unrecognised item in response:\n%s" % json.dumps(item)[:1000], file=sys.stderr)
            return 4
        saved.append(target)
        print(target)

    return 0


if __name__ == "__main__":
    sys.exit(main())
