# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-10-14

First public release.

### Added

- **37-style prompt library** (`references/style-library.md`), grouped into 7
  families: Classical Painting, Eastern Hand-drawn, Modern Art Movements,
  Illustration, Photography & Film, Digital & Trend, Design & Layout.
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
