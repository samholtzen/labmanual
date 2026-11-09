# Proposal

## Why

The manual currently holds one Markdown file per topic, and the planned writing (see `COMMENTS.md`) adds roughly 60 sections across the same four chapters. Folding that into the existing files would produce single pages of 10,000+ words, and the chapter files are already the largest in the repo. Restructuring now, while there are four chapters and five protocols, costs six link edits; the same migration after a year of writing would touch every page.

## What Changes

- Each chapter becomes a directory with an `index.md` landing page: `subsections/cloning.md` moves to `subsections/cloning/index.md`, and likewise for bacteria and mammalian cells. Chapter prose is moved whole, not split and not rewritten. Splitting a chapter into per-section pages happens later, per chapter, as that chapter is written.
- A new cross-cutting `subsections/foundations/` chapter is added for techniques that several chapters depend on rather than belonging to any one of them (gel electrophoresis, DNA quantification, cleanup, solution math). Its `index.md` lists the sections to come.
- **BREAKING** `subsections/under_construction.md` is retired; `foundations/index.md` replaces its "Common techniques" entry in the table of contents. The placeholder page and its figure stop being reader-facing. The image file itself stays in `media/`, so no figure is deleted from the repo.
- `protocols/` stays flat. Protocols are cross-cutting reference material read at the bench, not chapter children, so their URLs stay short and stable (`/protocols/pcr/`).
- The glossary stays a single page. It is the one page where length is a feature: 77 inbound links and in-page search beat navigation.
- The site menu nests three levels (tab → chapter → page), and the `navigation.indexes` theme feature makes each chapter directory itself clickable rather than a dead label.
- Manual `1.1.2`-style heading numbers are removed from the cloning chapter. Reading order is carried by the menu definition, and cross-references are made by name instead of by number.
- The README table of contents is reduced to chapters only. Each chapter's `index.md` lists its own sections, so the README stops needing an edit every time a section is added.

Out of scope: splitting any chapter into per-section pages, writing any new section content, and changing any prose or scientific claim.

## Capabilities

### New Capabilities
- `content-layout`: How the Markdown sources are organized — the chapter-directory and landing-page convention, the flat protocol library, the single-page glossary, where cross-cutting topics live, the heading-numbering policy, and the division of labor between the README table of contents and the site menu. Today this convention is implicit in `AGENTS.md` prose and in the shape of the files; it becomes the thing new topics are checked against as contributors add them.

### Modified Capabilities
- `site-build`: The "GitHub-compatible heading anchors" requirement is kept, but its scenario asserts that the link `#112-restriction-enzymes` resolves to a "1.1.2 Restriction Enzymes" heading. Removing the manual heading numbers retires that anchor, so the scenario must be restated against an unnumbered heading. The anchor scheme itself does not change.
- `site-navigation`: Two requirements change. "Menu order follows the table of contents" names "Common techniques" as the fourth chapter, which becomes "Foundations". "Persistent menu lists all pages" assumes a flat chapter list and must account for chapter landing pages, so that a chapter entry is a link to its own page rather than an unclickable grouping label.

## Impact

- **Content**: `subsections/cloning.md`, `subsections/bacteria.md`, `subsections/mammalian_cells.md` move into directories. `subsections/under_construction.md` is retired. `subsections/glossary.md` and all of `protocols/` and `media/` stay where they are.
- **Links**: 6 root-relative links point at pages that move (4 in the README table of contents, 1 at `subsections/bacteria.md:80`, 1 at `subsections/mammalian_cells.md:17`). The 77 glossary links, 6 media links, and 6 links into `protocols/` are unaffected. One in-page anchor breaks: `subsections/cloning.md:51` links to `#112-restriction-enzymes`, which the heading-number removal retires; it becomes a name-based link.
- **Headings**: 15 numbered headings in `subsections/cloning.md` lose their numbers. No other chapter is numbered.
- **Build tooling**: `tools/site/build.py` needs no code changes. `ALLOWED_DIRS` stages directories with `copytree`, so any depth is published, and the root-relative link rewriter is depth-aware. Verified by building a nested trial structure: a page at `subsections/cloning/pcr.md` resolved `/subsections/glossary.md#oligonucleotide` to `../../glossary/#oligonucleotide` and `/media/pcr.png` to `../../../media/pcr.png`, and `subsections/cloning/index.md` published at `/subsections/cloning/`.
- **Build config**: `tools/site/mkdocs.yml` gains the `navigation.indexes` theme feature and a nested `nav:` tree. `tools/site/README.md`'s "Add a page" instructions need updating for the new convention.
- **Repo conventions**: `AGENTS.md` describes the current flat layout and the "New topics get a `subsections/` page" rule, and needs to match the new structure.
- **Authorization**: removing the heading numbers and retiring the placeholder page both go beyond the copy-editing scope that `AGENTS.md` grants agents. Both were approved by the maintainer when this change was proposed. No prose or scientific claim is altered.
