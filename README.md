# Image Style Transfer

> Turn any image into one of **37 curated art styles** — Chinese ink wash, oil painting, ukiyo-e, cyberpunk, Studio Ghibli, film noir, editorial magazine spreads and 30 more.

[中文说明 →](README.zh-CN.md)

Built on the open **Agent Skills** standard, so the same skill runs in **Codex, ChatGPT, Claude Code, Cursor, GitHub Copilot, Gemini CLI, VS Code** — any host that reads `SKILL.md`.

---

## Why this one

Most style-transfer prompts are a one-line "make it look like an oil painting". This library is different — every entry is a **production-tested prompt** with four things that actually move the needle:

- **Precise terminology anchors** — `impasto`, `chiaroscuro`, `wet-on-wet`, `Ben-Day dots`, `Araki line`. Terminology beats adjectives by a wide margin.
- **Named references** — a specific painter, film or brand ("Monet", "Katsushika Hokusai", "Blade Runner", "Kinfolk") steers a model far harder than "beautiful".
- **A recommended strength per style** — because the one knob that matters most is image-to-image strength, and the right value is not the same for film grain and for pixel art.
- **Known failure modes** — the entry tells you what goes wrong (e.g. never point Hokusai at a portrait; it turns the face into "photo + wave sticker").

Beyond the library, the skill carries a **retouching playbook** for the part everyone gets stuck on: the render is 95% right, one detail is wrong, and re-running the whole image wrecks everything else. The fix — crop a patch, repaint the patch, feather it back so the rest stays pixel-identical — is documented with measured before/after numbers.

## The 37 styles

| # | Category | Styles |
|---|----------|--------|
| 1–4 | Editorial / magazine | vintage editorial (Kinfolk), Japanese fresh, high fashion, minimal Nordic |
| 5–10 | Painting & handcraft | oil painting, watercolor, Chinese ink wash, pencil sketch, ukiyo-e, marker illustration |
| 11–16 | Trend & digital | cyberpunk, vaporwave, pixel art, 3D cartoon / blind box, claymation, pop art |
| 17–21 | Retro & film | cinematic film, black & white film, HK retro, vintage American poster, Polaroid |
| 22–26 | Anime & illustration | anime, Ghibli, comic book, storybook, JOJO (cel shading + Araki line) |
| 27–32 | Materials & tones | paper cutout, Lego, neon glass, Morandi tones, impressionist impasto, expressionist impasto portrait |
| 33–37 | Editorial design | impasto micro-landscape poster, gathered-scenes zine, watercolor journal, abstract memory panel, literary modernist magazine |

Full prompts and parameters: [`skills/image-style-transfer/references/style-library.md`](skills/image-style-transfer/references/style-library.md).

## Install

### Codex

Codex discovers skills in `.agents/skills` (repo-level, walking up to the repo root) and `~/.agents/skills` (user-level).

```bash
git clone https://github.com/jyi06/image-style-transfer.git
cd image-style-transfer

# user-level install (available in every repo)
mkdir -p ~/.agents/skills
ln -s "$PWD/skills/image-style-transfer" ~/.agents/skills/image-style-transfer
```

> Note: **not** `.codex/skills/` — Codex does not scan that path. Symlinks are followed, so you can keep editing the checkout.

Then in Codex, invoke with `/skills` or `$image-style-transfer`, or just describe the task and let it match.

### Claude Code

```bash
mkdir -p ~/.claude/skills
ln -s "$PWD/skills/image-style-transfer" ~/.claude/skills/image-style-transfer
```

### Repo-level (any host)

Check the skill into the repo so your whole team gets it:

```bash
mkdir -p .agents/skills
cp -r path/to/image-style-transfer/skills/image-style-transfer .agents/skills/
```

### Other hosts

Any agent that supports the open Agent Skills standard reads a `SKILL.md` plus optional `references/`, `scripts/` and `assets/`. Point it at `skills/image-style-transfer/`.

## Give it an image generator

This skill decides *what to ask for*; the host provides *the model that draws it*. Two options:

**1. An MCP image tool (recommended).** If your agent already has an image generation/editing MCP server connected, just tell the skill to use it. Nothing to configure.

**2. The bundled helper.** `scripts/generate.py` is standard-library-only and speaks to any OpenAI-compatible `/v1/images/edits` endpoint:

```bash
export OPENAI_API_KEY=sk-...
# optional, for compatible gateways:
# export OPENAI_BASE_URL=https://your-gateway.example.com/v1
# export IMAGE_MODEL=gpt-image-1

python3 skills/image-style-transfer/scripts/generate.py \
  --image photo.jpg \
  --prompt "Chinese ink wash painting, xieyi brushwork, ..." \
  --out generated-images/ink.png \
  --match-aspect
```

Gateways that expose an explicit strength knob can take it via `--extra`:

```bash
python3 .../generate.py --image photo.jpg --prompt "..." --out out.png --extra strength=0.6
```

The skill maps its own strength guidance (`0.35–0.9`) onto whatever your provider calls the parameter — `input_fidelity`, `image_strength`, `denoising_strength`, `--iw`, and so on.

## Usage

Once installed, just talk to your agent:

> Turn this photo into a Chinese ink wash painting.

> Restyle this portrait as a 90s Hong Kong film still.

> Here's an image — show me the style menu.

> Do this one in watercolor and again as pixel art.

If you send an image with no style named, the skill shows a menu of the four best-matching styles for that image type, plus the full catalog. Reply with numbers, names, or "all of them".

## Repository layout

```
image-style-transfer/
├── plugin.json                              # portable manifest (agent-plugins.org schema)
├── README.md / README.zh-CN.md
├── LICENSE
└── skills/
    └── image-style-transfer/
        ├── SKILL.md                         # the workflow
        ├── agents/openai.yaml               # Codex-side metadata and dependencies
        ├── references/
        │   ├── style-library.md             # the 37 prompt templates
        │   └── style-menu.md                # the selection menu + smart recommendations
        └── scripts/
            └── generate.py                  # optional zero-dependency image-to-image helper
```

## Contributing

The style library is designed to grow. Add a new style, then update the numbering in **all three** places — `SKILL.md` (overview table), `style-library.md` (the entry), `style-menu.md` (the menu) — and the totals.

If you discover a failure mode, write it down in `SKILL.md` under *Notes* with what you measured. "Retrain the model" is not the point; "here is the exact thing that broke and the exact workaround" is.

## Publishing

Author is credited as **can1123**; the repository lives at `github.com/jyi06/image-style-transfer`. Nothing to fill in.

To republish under a different account, update `plugin.json` (`author`, `homepage`, `repository`, and the URLs inside `extensions.com.openai.interface`) plus the copyright line in `LICENSE`.

```bash
git init && git add -A && git commit -m "Initial release"
git branch -M main
git remote add origin https://github.com/jyi06/image-style-transfer.git
git push -u origin main
```

Optional: submit it to the OpenAI plugin directory, or ship it as a team marketplace catalog for local installs.

## License

MIT — see [LICENSE](LICENSE).
