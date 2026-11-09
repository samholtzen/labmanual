# Design

## Context

See `proposal.md` for motivation and `specs/` for required behavior.

Observed in the repo:

- About 10 Markdown pages plus 6 PNGs. Tables (`pcr.md`, `t4_ligase.md`, `bacteria.md`) and math (`mammalian_cells.md`: inline `$CO_{2}$` and a `$$` block) are the only non-trivial syntax.
- Internal links and images are root-relative (`/media/x.png`, `/protocols/pcr.md`). One in-page anchor depends on GitHub-style heading IDs (`#112-restriction-enzymes`).
- Protocols are reached only through links inside chapters, not through the README table of contents.
- `AGENTS.md` forbids editing prose, converting paths in bulk, or adding figures. The sources therefore cannot be edited to suit the site; the build must adapt to them.
- `python3` is available locally; `node`/`npm` are not.

## Goals / Non-Goals

**Goals:**
- One command produces a deployable `_site/` folder from the unmodified sources.
- The build process is generic enough that adding a chapter or protocol means adding a Markdown file and one menu entry.

**Non-Goals:**
- Deployment automation, hosting choice, custom domain, analytics.
- A bespoke theme. Use the generator's stock look with minimal overrides.
- A glossary or tooltip system.
- Fixing source-content issues listed in `COMMENTS.md`.

## Decisions

### 1. Pre-rendered static site via MkDocs + Material, not a client-side SPA
The theme's instant navigation (fetches page fragments, keeps the shell) provides the app-like feel, while every page is still a real HTML file. This avoids host-specific rewrite rules for S3/CloudFront/GCS.

*Alternatives:* a hand-written SPA (router + runtime Markdown), which needs rewrite rules and hurts deep links; Starlight/mdBook (need Node/Rust, which are not installed); a custom script (reinvents search, nav, and responsive layout).

### 2. Stage a copy of the sources, then build from the stage
`tools/site/build.py` copies the allowed sources into `_build/docs/` and builds from there, never touching originals. This is what lets us:
- exclude non-content files by only copying an allowlist (`README.md`, `subsections/`, `protocols/`, `media/`),
- rename `README.md` to `index.md`,
- rewrite links in the copies only.

*Alternative:* point MkDocs at the repo root with excludes. Rejected because the repo root also holds the config, output, and `lab_manual.md`, and MkDocs cannot rewrite root-relative links without extra plugins.

### 3. Rewrite links in the staged copies
For each staged page, convert root-relative targets (`/media/x.png`, `/subsections/x.md`, `/protocols/x.md`) into paths relative to that page, and map `README.md` links to `index.md`. Absolute `http(s)` links and `#anchor` links are left alone. MkDocs then converts `.md` links to final URLs and warns on missing targets, covering the broken-link scenario.

Relative paths make the output host- and subpath-agnostic, so no `site_url` is required for correct links.

### 4. GitHub-compatible heading slugs
Use `toc` with the `pymdownx.slugs` GitHub-style slugifier so `1.1.2 Restriction Enzymes` yields `112-restriction-enzymes`. The build verifies this anchor exists in the output.

### 5. Math via `pymdownx.arithmatex` (generic mode) + KaTeX
Arithmatex emits delimiters that KaTeX auto-render typesets in the browser. KaTeX is vendored or loaded from a pinned CDN version. Vendoring is preferred so the site works offline, but it is not required for the MVP.

### 6. Menu defined in one explicit file
`tools/site/mkdocs.yml` holds an explicit `nav` list: Home, the four chapters in README order, then a Protocols group. Explicit beats auto-derived because the README table of contents omits protocols and filenames alone do not give titles or order. Adding a page means one line here.

### 7. Tooling layout, pinned dependencies, ignored output

```
 README.md, subsections/, protocols/, media/   (sources, untouched)
        |
        v   tools/site/build.py
 _build/docs/   (staged copy: allowlist, README->index, rewritten links)
        |
        v   mkdocs build (tools/site/mkdocs.yml)
 _site/         (deployable static folder)
```

`tools/site/requirements.txt` pins `mkdocs` and `mkdocs-material` (and `pymdown-extensions`). `build.py` expects a project-local `.venv`, creates it if missing, installs from the pin file, and exits non-zero with install instructions when it cannot. `_site/`, `_build/`, and `.venv/` go in `.gitignore`.

### 8. Optional `--site-url` enables instant navigation
Material's instant navigation only activates when `site_url` is set (it relies on the sitemap). Verified in a browser: without it every click is a normal page load; with it the shell persists and math re-typesets after the swap. Hardcoding a URL would tie the output to one host, so `build.py --site-url <url>` is optional. When given, `build.py` writes a small generated config in `_build/` that inherits `tools/site/mkdocs.yml` and overrides `site_url`; when omitted, the portable build is unchanged. The value is validated as http(s) and normalised to end in `/`.

*Alternatives:* always require a URL (breaks host-agnostic output and local preview); drop instant navigation (loses the app-like feel for little gain). Expect the flag to become a deploy-time setting once a host is chosen.

## Risks / Trade-offs

- **Regex link rewriting is brittle** → Limit it to the three known path shapes, build with `--strict` so unresolved links fail the build, and keep a small check that the output contains no root-relative `href`/`src`.
- **Source numbering quirks** (irregular ordered-list numbers noted in `COMMENTS.md`) may render differently from GitHub → Compare visually in the first build and report differences to the human rather than editing prose.
- **MkDocs 1.x maintenance concerns and Material's own roadmap** may change the toolchain over time → Pin versions; the staged-sources design keeps the generator replaceable.
- **Stock theme styling** may not suit a "textbook" feel → Accept for the MVP; revisit with minimal CSS overrides after review.
- **Instant navigation and math** can fail to re-typeset after a page swap → Hook KaTeX into the theme's page-change event and check navigating to the mammalian page from another page.
- **Python/venv assumptions** on other contributors' machines → Document the single command and Python version in the tooling README.

## Open Questions

- Which host to deploy to, and whether to add CI (a later change).
- Whether to vendor KaTeX or keep a pinned CDN reference long term.
