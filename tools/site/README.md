# Building the site

The Markdown files in this repo are the source of truth. This folder turns them into a static website (plain HTML, CSS, and JS) that any file host can serve. Nothing here changes the Markdown.

## Build

From the repository root:

```
python3 tools/site/build.py
```

The first run creates a local `.venv/` and installs the pinned tools (needs Python 3.8+ and internet access). Output goes to `_site/`. Re-running is safe; it starts from a clean slate each time.

To preview locally:

```
python3 tools/site/build.py --serve
```

Then open <http://localhost:8000>.

### For deployment: `--site-url`

```
python3 tools/site/build.py --site-url https://example.org/labmanual/
```

`--site-url` is optional. Without it, the output works at any URL or subfolder and pages load normally. With it, the site also gets instant page-to-page navigation (the menu and header stay in place) and a sitemap using that URL. Use it for the build you actually upload.

Upload the contents of `_site/` to your host. No server-side code or rewrite rules are needed.

## What gets published

Only `README.md` (as the home page), `subsections/`, `protocols/`, and `media/`. Files such as `lab_manual.md`, `AGENTS.md`, `COMMENTS.md`, and `openspec/` are never copied.

The build works on a copy in `_build/docs/` (git-ignored). In that copy it rewrites root-relative links such as `/media/x.png` and `/protocols/pcr.md` so they work at any base path. The build stops with an error if a link points at a page or image that does not exist.

## How the content is laid out

- **A chapter is a directory** under `subsections/` with an `index.md` landing page. `subsections/cloning/index.md` is published at `/subsections/cloning/`. Use lowercase names with hyphens (`mammalian-cells`).
- **Protocols stay flat.** One file per protocol, directly in `protocols/`, so each keeps a short, stable address like `/protocols/pcr/`.
- **The glossary is one page**, `subsections/glossary.md`.
- **Cross-cutting techniques** that several chapters rely on (gels, DNA quantification, and so on) go in the `foundations` chapter.
- **Reading order comes from the `nav:` list** in `tools/site/mkdocs.yml`, not from filenames or heading numbers. Do not number headings by hand.

## Add a page

To add a section to an existing chapter:

1. Add the Markdown file inside the chapter's directory, e.g. `subsections/cloning/gibson.md`.
2. Add one line for it in `tools/site/mkdocs.yml`, under that chapter and after its `index.md` line.
3. Link to it from the chapter's `index.md`.
4. Rebuild.

To add a new chapter:

1. Create `subsections/<chapter>/index.md`.
2. In the `nav:` list, add a group for it under `Chapters`, with `index.md` as the first entry (this makes the chapter name itself a link).
3. Add one entry for it to the table of contents in `README.md`.
4. Rebuild.

To add a protocol:

1. Add the Markdown file to `protocols/`.
2. Add one line for it under `Protocols` in the `nav:` list.
3. Rebuild.

A page's address comes from its path, e.g. `protocols/pcr.md` becomes `/protocols/pcr/`, and `subsections/cloning/index.md` becomes `/subsections/cloning/`.

## What is in this folder

| File | Purpose |
| --- | --- |
| `build.py` | The build command described above |
| `mkdocs.yml` | Site settings and the menu (`nav:`) |
| `requirements.txt` | Pinned versions of the tools |
| `assets/javascripts/katex.js` | Typesets math on every page view |

Math (`$...$` and `$$...$$`) is typeset with KaTeX loaded from a CDN, so viewing math needs an internet connection.
