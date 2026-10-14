# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-10-14

Thirteen new styles, a visual gallery, and a numbering policy that keeps every
previously published style number valid.

### Added

- **13 new styles (38–50)**, in three new families:
  - **Print, graphic & ornamental art (38–43)** — Art Deco, Art Nouveau,
    Bauhaus poster, Risograph, woodcut, banknote engraving
  - **Art movements & concepts (44–48)** — pointillism, surrealism, Op Art,
    fresco, stained glass
  - **Material & craft (49–50)** — embroidery, marble sculpture
- **Gallery** (`docs/gallery/`) — a before/after pair and a nine-tile grid, both
  embedded in the READMEs. One input image, seven styles, no per-image tuning.
- **Cross-reference notes** between easily confused neighbours, e.g. #40 Bauhaus
  vs #37 literary magazine, #42 woodcut vs #9 ukiyo-e, #48 stained glass vs
  #29 neon glass, #44 pointillism vs #31 impressionist impasto.

### Changed

- The library now documents an explicit **numbering policy: append, never
  insert**. New entries take the next free number at the end, so every number
  ever published keeps pointing at the same style. (This is how 38–50 were added
  without disturbing 1–37.)

### Fixed

- The `1.0.0` entry below previously described the library as grouped into seven
  families using invented names (Classical Painting, Modern Art Movements, …)
  that did not match the actual sections. Corrected to the real families:
  editorial/magazine, painting & handcraft, trend & digital, retro & film,
  anime & illustration, materials & tones, editorial design.

## [1.0.0] - 2026-10-14

First public release.

### Added

- **37-style prompt library** (`references/style-library.md`), grouped into 7
  families: editorial / magazine, painting & handcraft, trend & digital,
  retro & film, anime & illustration, materials & tones, editorial design.
- **Style menu** (`references/style-menu.md`) — a one-line index for quickly
  picking a style by number.
- **Per-style generation parameters**: recommended `input_fidelity`, size,
  negative-prompt hints, and aspect-ratio notes.
- **Retouching recipes** documented in `SKILL.md`:
  - Local patch method (crop neighbourhood → redraw at low fidelity → paste back
    through a feathered elliptical mask) for fixing a single feature such as an
    ear, nose, or eye without disturbing the rest of the frame.
  - Background vibrancy boost that preserves hue (HSV saturation scaling with a
    subject-protection mask).
  - Why whole-image re-runs cannot fix local defects, and when to prefer a patch.
- **Zero-dependency generator** (`scripts/generate.py`) — standard library only,
  talks to any OpenAI-compatible `/v1/images/edits` endpoint.
- **Plugin manifests** for Codex / Agent Skills hosts: `plugin.json` and
  `skills/image-style-transfer/agents/openai.yaml`.
- **Documentation**: `README.md` (English) and `README.zh-CN.md` (中文).

### Notes

- Installation path for Codex is `~/.agents/skills/`, **not** `~/.codex/skills/`.
- The same package works unmodified with Claude Code, Cursor, Copilot, and
  Gemini CLI, since they read the same Agent Skills layout.

[1.0.0]: https://github.com/jyi06/image-style-transfer/releases/tag/v1.0.0
[1.1.0]: https://github.com/jyi06/image-style-transfer/releases/tag/v1.1.0
