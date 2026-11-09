# Proposal

## Why

The manual is only readable as raw Markdown on GitHub, with no persistent menu, no rendered math, and no way to host it anywhere else. The goal is a browsable site that can be deployed to any static host (GitHub Pages, S3/CloudFront, Google Cloud Storage, etc.) while the `.md` files stay the single source of truth. This is an MVP to see what a built site looks like and to establish a build process that can be reused as chapters are added.

## What Changes

- Add a reproducible build that turns the existing Markdown (`README.md`, `subsections/`, `protocols/`) and `media/` into a folder of plain static HTML/CSS/JS.
- The build reads the source files without modifying them. Root-relative links (`/media/x.png`, `/subsections/x.md`) and `.md` links are rewritten in a staged copy, so the sources stay GitHub-friendly and work under any hosting subpath.
- Output has a persistent sidebar and top menu, search, mobile layout, and rendered `$...$` / `$$...$$` math.
- The menu covers the home page, the chapters, and the protocols (which currently appear only as links inside chapters).
- Heading anchors match GitHub's scheme so existing in-page links (e.g. `#112-restriction-enzymes`) keep working.
- `lab_manual.md` (deprecated), `AGENTS.md`, `COMMENTS.md`, and `openspec/` are excluded from the site.
- Build tooling, its dependency pins, and the output/staging folders are added to the repo (with output ignored by git).
- Not a literal client-side SPA: pages are pre-rendered, with the theme's instant navigation providing the app-like feel. This avoids host-specific rewrite rules.

Out of scope for the MVP: CI or automatic deployment, a custom domain, a glossary, any edits to prose, figures, or scientific claims, and converting links in the source files.

## Capabilities

### New Capabilities
- `site-build`: Building the static site from the Markdown sources: source-of-truth handling, exclusions, link/path rewriting, math and anchor rendering, and host-agnostic output.
- `site-navigation`: The site's menu structure, search, and page layout for chapters and protocols.

### Modified Capabilities

(none; there are no existing specs)

## Impact

- **New files:** build script, site configuration, dependency pin file, and short build instructions, under a new tooling folder.
- **Changed files:** `.gitignore` (output and staging folders, virtualenv). Local-only `AGENTS.md` layout note should mention the build.
- **Unchanged:** all `.md` content and `media/` files.
- **Dependencies:** Python 3 (already present) with MkDocs and the Material theme in a local virtualenv. No Node needed.
- **Systems:** none deployed in this change. Output is a folder that can be uploaded to any static host.
