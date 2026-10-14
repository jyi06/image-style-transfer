---
name: image-style-transfer
description: Restyle any image into one of 80 curated art styles (Chinese ink wash, oil painting, watercolor, ukiyo-e, gongbi, Dunhuang mural, Vermeer interior light, Baroque, pointillism, stained glass, cyanotype, Kodachrome, long exposure, glitch art, Superflat, ligne claire, voxel art, cyberpunk, anime, Ghibli, film noir, editorial magazine layouts, Art Deco, Risograph, ...). Use when the user provides an image and asks to "make it X style", "turn this into oil painting", "style transfer", "photo to art", "换成XX风格", "做成XX风", or when they send an image with no style named (present the style menu first). Ships a production-tested prompt library, per-style strength recommendations, and local-patch retouching recipes for fixing one detail without re-rendering the whole image.
license: MIT
compatibility: Any agent that supports the open Agent Skills standard (Codex, ChatGPT, Claude Code, Cursor, GitHub Copilot, Gemini CLI, VS Code...). Requires an image-generation / image-editing capability — either an image model exposed as an MCP tool, or the bundled scripts/generate.py helper pointed at an OpenAI-compatible image API.
---

# Image Style Transfer

Restyle the user's image into a named art style while **preserving the subject, identity and composition**.

This skill does not generate images itself. It does the part that actually determines quality:

1. **parses the requested style** and retrieves a battle-tested prompt template,
2. **assembles the final prompt** (style template + subject fidelity + negative constraints),
3. **hands it to an image-generation tool** available in the host environment,
4. **verifies and repairs** the result (per-style strength tuning, local-patch retouching for one bad detail).

All IP in here is the prompt library, the strength-tuning playbook and the retouching recipes. The generator is pluggable.

## Style library at a glance

**80 styles, numbered 1–80** (authoritative source: `references/style-library.md`).

| Category | Numbers | Count |
|------|------|------|
| Editorial / magazine | 1–4 | 4 |
| Painting & handcraft | 5–10 | 6 |
| Trend & digital | 11–16 | 6 |
| Retro & film | 17–21 | 5 |
| Anime & illustration | 22–26 | 5 |
| Materials, tones & expressionism | 27–32 | 6 |
| Editorial design, zines & posters | 33–37 | 5 |
| Print, graphic & ornamental art *(v4)* | 38–43 | 6 |
| Art movements & concepts *(v4)* | 44–48 | 5 |
| Material & craft *(v4)* | 49–50 | 2 |
| East Asian traditions *(v5)* | 51–57 | 7 |
| Western art history *(v5)* | 58–65 | 8 |
| Photography & imaging processes *(v5)* | 66–73 | 8 |
| Contemporary illustration & digital *(v5)* | 74–80 | 7 |
| **Total** | **1–80** | **80** |

> The numbers must stay consistent across this file, `references/style-library.md` and `references/style-menu.md`. When adding a style, update all three.
> **Append, never insert.** Numbers are the interface users quote back ("do 26 and 37"). Appending new entries as `51, 52, ...` keeps every previously published number valid; inserting in the middle silently renumbers everything after it.

## When to use

- User gives an image **plus** a style name ("make it oil painting")
- User gives an image **without** a style → **present the style menu first** (`references/style-menu.md`), do not pick for them
- User gives a descriptive style request ("that Japanese soft-focus look")
- User wants one image rendered in several styles ("do watercolor and cyberpunk")
- User wants a photo turned into illustration / anime / magazine spread / retro film / blind-box toy

## Prerequisites

- An **input image** (local path or URL). If a style is named but no image is given, ask for the image.
- An **image-generation capability**. Two supported paths:
  - **Preferred — an MCP tool.** Use whatever image generation/editing tool the host exposes (e.g. an image MCP server). Pass the source image as the reference input.
  - **Fallback — `scripts/generate.py`.** A dependency-light Python helper that calls any OpenAI-compatible `/v1/images/edits` endpoint. See the script's `--help` and the README for `OPENAI_API_KEY` / `OPENAI_BASE_URL` setup.
- Generation usually **costs money or credits**. **Tell the user the expected cost before generating and get agreement.** One image is typically 1 generation unit; multi-style requests multiply.

## Workflow

### Step 1 · Get the image and confirm the style

1. Resolve the input image path (uploaded files usually land in the session working directory, or the user gives an absolute path).
2. **Image but no style → present the menu:**
   1. **Read the image**: subject type (portrait / landscape / architecture / still life / pet / casual snapshot), scene and palette.
   2. Open `references/style-menu.md` and pick the **4 best-matching styles** using its "recommended by image type" table.
   3. Present those 4 as a **multi-select control**, and **also list the full catalog in the message body** so the user can pick anything.
   4. Accept answers as **numbers** ("3 and 22"), **names** ("oil painting"), or **"all of them"**.
3. Vague style requests ("make it nicer", "more premium") → same treatment: offer concrete candidates, never guess silently.
4. One image, several styles → keep a task list and run them **serially** (parallel runs with near-identical prompts can overwrite each other's output files, and some APIs rate-limit).
5. **State the cost and get agreement before generating.**

### Step 2 · Retrieve the prompt

1. Open `references/style-library.md` and match the style by name (Chinese or English, synonyms OK).
2. Hit → take that entry's **prompt template** and **recommended strength**.
3. Miss → build it with the "style derivation formula" at the end of that file, and **append the new entry** to `style-library.md` after a successful generation. The library is meant to grow.

### Step 3 · Assemble the final prompt

```
final prompt = style template + subject fidelity clause + composition clause + negative constraints
```

- **Subject fidelity:** `keep the subject, facial features, pose and composition unchanged; only change the rendering style and palette` (unless the user explicitly wants a bigger departure).
- **Composition:** `keep the original composition and subject placement`.
- **Negatives:** `no text watermark, no extra limbs, no distortion`.
- Also add `keep the original natural expression` and a negative `no grinning / no forced smile` — **do not add smiles the user did not ask for** (see Notes).

Example (portrait → oil painting):

> `Classical oil painting, impasto brushwork, visible pigment build-up and canvas texture, impressionist colour, warm chiaroscuro light, loose confident strokes, like a museum canvas; keep the subject's facial features, pose and background composition unchanged, only change the rendering style and palette; no text watermark, no extra limbs, no distortion`

### Step 4 · Generate (image-to-image)

Pass the source image as the **reference image** and the assembled prompt as the prompt.

| Parameter | Guidance |
|------|---------|
| source image | **required** — the user's original |
| prompt | the assembled final prompt |
| **strength / fidelity** | the single most important knob. Names differ per provider (`input_fidelity`, `image_strength`, `denoising_strength`, `--iw`...). **Higher = closer to the original**, lower = more repainted. Per-style recommendations are in the library. |
| size | follow the source aspect ratio, e.g. `1024x1024` / `1024x1536` / `1536x1024` |
| quality | use the highest available for deliverables |
| output | write to a predictable folder, e.g. `generated-images/` in the working directory |

**Strength quick reference** (map onto your provider's parameter):

- `0.75–0.9` — light stylisation / filter-like, subject nearly untouched
- `0.55–0.75` — **standard style transfer** (recommended band: style obvious, subject recognisable)
- `0.35–0.5` — heavy repaint (pixel art, building blocks, and other shape-rebuilding styles)

### Step 5 · Save and present

1. Confirm the output file exists; record its path.
2. Show every result to the user (all of them at once for multi-style jobs).
3. Report: style used, strength used, cost incurred.

## Prompt-writing essentials

- Be specific about **colour / light / material** ("desaturated warm tones + soft side light + matte paper" beats "nice").
- **Separate style words from content words with semicolons** so the model does not read style words as scenery.
- Realistic styles (film, magazine, polaroid) want **high strength (≈0.7)**; painting/cartoon styles tolerate lower.
- Portraits **must** carry "keep the facial features" or the face will be swapped.

**When the user says "the change is too subtle / not enough style", escalate in this order:**

1. **Lower the strength** to `0.45–0.55` — the single most effective move.
2. **Hard-code the palette** — replace "warm tones" with concrete names ("oatmeal beige", "emerald and black gold").
3. **Add intensity words** — `fully re-tone the image`, `visible film grain`, `low-contrast muted greys`, `strongly stylised`.
4. **Name a reference** — `Kinfolk`, `Studio Ghibli`, `Pixar look`, `Blade Runner` beat abstract adjectives by a wide margin.
5. Still weak? Prepend: `completely repaint the photo as a XX-style illustration, do not preserve photographic texture`.

## Notes — hard-won, do not relearn these

- **Tell the user the cost and get agreement before generating.**
- **Output filenames can collide.** Providers often name files from the prompt + timestamp; same-second concurrent runs with similar prompts overwrite each other. For A/B comparisons either run **serially** or give each variant its **own output directory**, then verify what actually landed on disk.
- **If generation fails content review**, explain why and offer a different style or a different image.
- **Fixing one detail: use the *previous good render* as the source, not the original.** When the user is happy overall but dislikes one spot (ear, eye, hand, mouth, face shape), feed the **previous render** back in with a low-intensity prompt (`only fix XX, keep everything else exactly unchanged`) and a **high** strength (0.7+). Re-running from the original with lots of local constraints makes randomness drift the **composition, clothing and palette**. (Measured case: fixing an anime ear from the original lost the palette, turned trousers into swimwear, and cropped into a close-up.)
- **Keep the original expression.** Do not add smiles. When the user wants a "bright / cheerful" mood, carry it with **light and palette** (golden warm light, bright open-air rendering, saturated warm tones), not by changing the face. Default to `keep the original natural expression` + negative `no big grin / no forced smile`; only add a strong smile constraint if the user explicitly asks.
- **When a local detail refuses to change, use "local patch + feathered composite":**
  1. Crop a square neighbourhood around the detail from the **current good render** (with margin, e.g. 340×340) and upscale it (e.g. to 1024).
  2. Run image-to-image on **just that patch** (safe to use a low strength `0.35–0.45`, because the change is confined to the patch).
  3. Scale the patch back, and paste it in with a **feathered ellipse / rounded-rect mask** (20–28px feather kills the seam).
  Everything outside the mask stays **pixel-identical** (verifiable: `diff.sum() == 0`). Try it **before** re-running the whole image. (Measured: 3 whole-image re-runs shrank an offending ear by only 15–20%; one patch fixed it with zero drift.)
  The same trick works for **changing texture in one area only** — e.g. "more oil-paint strokes on the figure but leave the background alone": crop the head as a patch, repaint it, feather it back; background stays pixel-identical.
- **Models are very reluctant to *shrink* a feature.** Asking for smaller ears/eyes usually moves them 15–20% at best. Escalate to the **occlusion route** (cover it with hair, clothing or shadow) or stack multiple patch passes.
- **Global "make the background more vivid / saturated / brighter" is a local image-processing job, not a re-render.** A whole-image re-run will wreck composition, skin tone and detail. Do it locally with an **HSV saturation lift + a subject-protection mask**:
  1. Protection mask = "subject core" (head/hair/torso/arms approximated with ellipses + polygons, then 40–50px Gaussian feather) ∪ "skin region" (YCbCr test `133≤Cr≤173`, `77≤Cb≤127`, `R>80`, dilated 9px then feathered).
  2. Background weight `w = 1 − protection`; lift saturation via `S' = clip(S^0.90 · (1 + (k−1)·w))` where `k≈1.9` is an obvious vivid setting and `1.45` a mild one; optionally add `+0.10·(1−V)·w` to gently lift shadows.
  3. The feathered mask makes the seam invisible; the subject stays essentially pixel-identical. (Measured: cheek mean diff 37 → 5.3, whole-face region 37 → 9.4.)
- **Render on-image text with code, never with the model.** Models reliably mangle Japanese/Chinese glyphs. Use PIL instead:
  - Font: on Windows `C:/Windows/Fonts/YuGothB.ttc` (Yu Gothic Bold, has kana) or `msgothic.ttc`; `ImageFont.truetype(path, size, index=0)`.
  - Outlined text: `draw.text(..., fill=(255,255,255,255), stroke_width=max(6,int(size*0.085)), stroke_fill=(0,0,0,255))`, then trim with `im.crop(im.getbbox())`.
  - Rotate each glyph individually (`rotate(angle, expand=True)`) and `alpha_composite`; **angled text reads far more like a comic** than a horizontal baseline.
  - Placement: on the background at the sides of the subject, mirrored left/right; white fill + heavy black stroke stays legible over both dark clothing and bright sky. **Check all four corners for clipping** afterwards.
  - **Default is no text at all.** Only add onomatopoeia / titles when the user explicitly asks, because text is a strong, opinionated edit.
- **A patch repaint must declare the *same rendering language* as the rest of the image.** If the render is cel-shaded (flat colour + hard edges) and the patch prompt only says "clean up XX", the model returns a **soft realistic gradient** that visibly fights the surrounding flat blocks. Always spell it out: `cel shading, flat hard-edged colour blocks, bold black ink outlines, no gradients, no soft light, no realistic rendering, no halftone dots`.
- **Never use median filters or morphological closing to remove halftone/screened shading.** `MedianFilter` smears the **ink lines** into blurry colour patches; `MaxFilter→MinFilter` closing leaves **square artefacts**; a brightness-ratio approach **blows out the colours** into noisy speckle. This class of fix is patch-repaint only.
- **Never modify the user's original file.** Write new files only.
