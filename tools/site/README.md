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

## Add a page

1. Add the Markdown file under `subsections/` or `protocols/`.
2. Add one line for it in the `nav:` list in `tools/site/mkdocs.yml`.
3. Rebuild.

The page's address comes from its filename, e.g. `protocols/pcr.md` becomes `/protocols/pcr/`.

## What is in this folder

| File | Purpose |
| --- | --- |
| `build.py` | The build command described above |
| `mkdocs.yml` | Site settings and the menu (`nav:`) |
| `requirements.txt` | Pinned versions of the tools |
| `assets/javascripts/katex.js` | Typesets math on every page view |

Math (`$...$` and `$$...$$`) is typeset with KaTeX loaded from a CDN, so viewing math needs an internet connection.
