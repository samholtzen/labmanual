# Tasks

## 1. Tooling setup

- [x] 1.1 Create `tools/site/requirements.txt` pinning `mkdocs`, `mkdocs-material`, and `pymdown-extensions`; verify `python3 -m venv .venv && .venv/bin/pip install -r tools/site/requirements.txt` succeeds
- [x] 1.2 Add `_site/`, `_build/`, and `.venv/` to `.gitignore`; verify `git status` ignores them after a build
- [x] 1.3 Create `tools/site/mkdocs.yml` with the Material theme, instant navigation, search, `toc` with GitHub-style slugs, `pymdownx.arithmatex` (generic) plus KaTeX assets, and an explicit `nav` (Home, four chapters in README order, Protocols group); verify `mkdocs build` accepts the config against a hand-made stage

## 2. Build script

- [x] 2.1 Write `tools/site/build.py` that creates/uses `.venv`, installs from the pin file, and exits non-zero with install instructions on failure; verify it fails cleanly with a message when Python deps cannot be installed (e.g. simulated offline) and succeeds otherwise
- [x] 2.2 Stage only the allowlist (`README.md` as `index.md`, `subsections/`, `protocols/`, `media/`) into a freshly cleaned `_build/docs/`; verify `lab_manual.md`, `AGENTS.md`, `COMMENTS.md`, and `openspec/` are absent from `_build/` and `_site/`
- [x] 2.3 Rewrite root-relative links/images and README links in the staged copies only; verify `git status` shows no source changes and `grep -r 'href="/'` / `src="/` over `_site/` returns nothing for internal targets
- [x] 2.4 Run `mkdocs build --strict` from the script; verify a deliberately broken link added to a staged copy fails the build and the real sources build cleanly
- [x] 2.5 Verify the build can be run twice in a row with no manual cleanup and gives identical page lists

- [x] 2.6 Add an optional `--site-url` flag to `build.py` (http(s) only, normalised to a trailing `/`, applied through a generated config in `_build/`); verify a build without it is unchanged, an invalid value exits non-zero, and a build with it lists that URL in `sitemap.xml` and keeps the page shell across a menu click in a browser, with math still typeset

## 3. Rendering checks

- [x] 3.1 Verify the heading anchor `112-restriction-enzymes` exists in the built cloning page and the in-page link points to it
- [x] 3.2 Serve `_site/` and open the mammalian cell culture page; verify `$CO_{2}$` and the `$$` block render typeset with no literal dollar signs, including after navigating there from another page via the menu
- [x] 3.3 Verify tables in the PCR, T4 ligase, and bacteria pages render, and all 6 images display
- [x] 3.4 Serve `_site/` under a subpath (e.g. copy into `/tmp/x/labmanual/` and serve `/tmp/x`) and verify images and internal links work
- [x] 3.5 Compare ordered-list numbering in the Golden Gate and T4 ligase protocols against GitHub's rendering; record any differences in `COMMENTS.md` for the human instead of editing prose

## 4. Navigation checks

- [x] 4.1 Verify the menu on every page lists Home, all chapters in README order, and all five protocols, with the current page highlighted
- [x] 4.2 Verify search for "ligase" returns the T4 ligase protocol and the cloning chapter
- [x] 4.3 Verify at 375 px width that there is no horizontal scroll and the menu opens from a toggle; verify print preview hides the menu
- [x] 4.4 Verify adding a throwaway protocol file plus one nav line and rebuilding shows it in the menu; remove the throwaway afterwards

## 5. Documentation and wrap-up

- [x] 5.1 Write `tools/site/README.md` with the single build command, serve command, Python requirement, and how to add a page; verify the documented commands work as written from a fresh clone
- [x] 5.2 Update the local `AGENTS.md` layout and "no build system" notes to mention `tools/site/` and the build; verify the text matches the repo
- [x] 5.3 Before opening a PR per `AGENTS.md`: confirm all changed link and image paths resolve and preview the rendered math and tables in the built site

## Workflow follow-up

- Work on a topic branch (not `main`), push, and open a PR; the human merges.
- Archive this change after review.
- Deployment (host choice, CI) is a separate later change.
