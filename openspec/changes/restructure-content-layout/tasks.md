# Tasks

## 1. Chapter directories

- [x] 1.1 Create a topic branch for this work, based on the branch that carries `tools/site/` (currently `add-static-site`, which is not yet merged to `main`), and verify `git log --oneline -1` shows that branch's site-build commit as an ancestor. If that branch has merged by then, branch from `main` instead and verify `tools/site/mkdocs.yml` is present.
- [x] 1.2 `git mv subsections/cloning.md subsections/cloning/index.md` and verify `git status` records it as a rename rather than a delete plus an add.
- [x] 1.3 `git mv subsections/bacteria.md subsections/bacteria/index.md` and verify the same.
- [x] 1.4 `git mv subsections/mammalian_cells.md subsections/mammalian-cells/index.md` (note the rename to kebab-case) and verify the same.
- [x] 1.5 Confirm no chapter file remains directly in `subsections/` except `glossary.md` and `under_construction.md`, by checking that `ls subsections/*.md` lists only those two.

## 2. Inbound links to moved pages

- [x] 2.1 Update the four chapter links in the README table of contents to point at the new `index.md` paths, and verify `grep -c "](/subsections/[a-z-]*/index.md)" README.md` reports 4.
- [x] 2.2 Update the cloning link at `subsections/bacteria.md:80` and the bacteria link at `subsections/mammalian-cells/index.md:17` to the new paths, and verify `grep -rn "](/subsections/\(cloning\|bacteria\|mammalian_cells\)\.md" .` returns nothing.
- [x] 2.3 Confirm the links that must not have changed are intact: verify the glossary and media link counts are still 77 and 6 respectively via `grep -ro "](/subsections/glossary.md#" subsections protocols | wc -l` and `grep -ro "](/media/" subsections protocols | wc -l`.

## 3. Heading numbers in the cloning chapter

- [x] 3.1 Remove the `1.1`, `1.1.x`, `1.2`, `1.2.x`, `1.3` and `1.3.x` prefixes from the 15 numbered headings in `subsections/cloning/index.md`, leaving the heading text and the existing protocol links otherwise untouched, and verify `grep -c "^#\+ \[\?[0-9]\+\." subsections/cloning/index.md` reports 0.
- [x] 3.2 Replace the in-page cross-reference at `subsections/cloning/index.md:51` — `[section 1.1.2](#112-restriction-enzymes)` — with a name-based link to `#restriction-enzymes`, and verify the rendered link text names the section rather than a number.
- [x] 3.3 Confirm no other page carries numbered headings, by verifying `grep -rn "^#\+ \[\?[0-9]\+\.[0-9]" subsections protocols` returns nothing.

## 4. Foundations chapter

- [x] 4.1 Write `subsections/foundations/index.md` as a chapter introduction in the manual's existing voice, naming the sections it will come to hold (gel electrophoresis, DNA quantification, cleanup, solution math) without asserting any new scientific claim, and verify it renders with no empty section links.
- [x] 4.2 Point the README's fourth table-of-contents entry at `/subsections/foundations/index.md`, replacing the "Common techniques" entry and its construction banner, and verify the README lists exactly four chapter entries.
- [x] 4.3 Delete `subsections/under_construction.md`, leave `media/under_construction.png` in place, and verify `grep -rn "under_construction" README.md subsections protocols` returns nothing.

## 5. Site configuration

- [x] 5.1 Add `navigation.indexes` to the theme features in `tools/site/mkdocs.yml` and verify it sits alongside the existing `navigation.*` features.
- [x] 5.2 Rewrite the `nav:` chapter entries as nested three-level groups, each chapter listing its `index.md` as a bare path first so it becomes the chapter's landing page, keeping chapter order as Molecular Cloning, Bacterial Cell Culture, Mammalian Cell Culture, Foundations, and verify the file parses by running the build.
- [x] 5.3 Update the "Add a page" section of `tools/site/README.md` for the new convention (a chapter is a directory with `index.md`; protocols stay flat; nav order carries reading order), and verify the documented steps match what tasks 1-5 actually did.

## 6. Repository conventions

- [x] 6.1 Update the layout table and the "New topics" rule in `AGENTS.md` to describe chapter directories, the flat protocol library, the `foundations` chapter, and the no-numbered-headings rule, and verify the file no longer describes `subsections/` as holding one page per topic.
- [x] 6.2 Record in `COMMENTS.md` that the numbering and chapter-heading inconsistencies raised there are now resolved by this change, and verify the stale open items are checked off or struck rather than left as open questions.

## 7. Build verification

- [x] 7.1 Run `python3 tools/site/build.py` and verify it exits zero with no unresolved-link or strict-mode errors.
- [x] 7.2 Verify the published addresses by confirming `_site/subsections/cloning/index.html`, `_site/subsections/mammalian-cells/index.html`, `_site/subsections/foundations/index.html`, and `_site/protocols/pcr/index.html` all exist.
- [x] 7.3 Verify link rewriting from the new depth by confirming the glossary links in `_site/subsections/cloning/index.html` resolve to `../glossary/` and the figure references resolve to `../../media/`.
- [x] 7.4 Run `python3 tools/site/build.py --serve` and confirm in the browser that the menu shows three levels, that each chapter entry is clickable and opens its landing page, that the current page is marked, and that the cloning chapter's math and tables still render.
- [x] 7.5 Run `openspec validate restructure-content-layout` and verify it reports the change as valid.

## Workflow follow-up

- Push the topic branch and open a PR describing the move, the six link edits, and the two maintainer-approved steps that exceed the `AGENTS.md` agent scope (heading-number removal, placeholder retirement).
- Leave the merge to the maintainer, per `AGENTS.md`.
- Archive this change after it merges.
