# Design

## Context

See `proposal.md` — Why. The constraints that shape the approach:

- `tools/site/build.py` stages `subsections/`, `protocols/`, and `media/` with `copytree` and rewrites root-relative links relative to each page's own depth. Both behaviors already handle nesting; this was verified by building a nested trial structure before this change was written.
- The site has no public URL yet. `README.md` describes the project as under construction, no host is chosen, and `--site-url` is optional. URL changes therefore cost nothing right now and will not be free later.
- `AGENTS.md` forbids agents from changing prose or scientific claims, and limits them to typos, broken links, and infrastructure. Two steps here exceed that scope — removing heading numbers and retiring the placeholder page — and were approved by the maintainer when this change was proposed.
- The existing `site-build` spec pins the anchor `#112-restriction-enzymes` in a scenario, so the heading-number removal is a spec-visible change, not just an edit.

## Goals / Non-Goals

**Goals:**

- Make the structural convention explicit and checkable, so a contributor adding a topic has one correct location.
- Keep every address that a reader might have bookmarked stable where it is cheap to do so, and change the rest now rather than later.
- Leave the build tooling's logic untouched; this should be a content and configuration change only.

**Non-Goals:**

- Splitting any chapter into section pages. The directories are created so that splitting is a local, per-chapter operation later.
- Writing any `foundations` section content. Only the chapter's landing page is created.
- Changing the reading order of the book, or any prose.

## Decisions

### Chapters become directories; `protocols/` stays flat

The content has two access patterns. Chapters are a reading path, followed in order via the menu, where nesting helps and addresses can move. Protocols are a lookup path — opened at the bench, on a phone, by someone who wants one procedure now — where a short permanent address matters more than hierarchy.

Protocols are also genuinely cross-cutting: `chemical_transformation_of_e_coli.md` is already referenced twice from the cloning chapter, and gel electrophoresis will serve cloning, RNA, and protein work alike. Filing a shared protocol under one chapter would make that chapter its owner, which is wrong.

Alternatives considered:

- **Flat `subsections/` with more files.** Zero migration cost, but `subsections/` becomes a bucket of 30+ files with no structure visible in the repository, and the directory name stops meaning anything.
- **Topic directories co-locating concepts and protocols** (`content/cloning/protocols/pcr.md`). Appealing for `git log` on one folder, but it forces every shared protocol into an arbitrary owning chapter and lengthens the addresses most used at the bench.

### A chapter becomes a directory now, even while it holds one page

All four chapters get directories in this change, rather than converting each when it first outgrows a single file. Uniformity makes the convention self-evident to contributors, and the migration is paid once at four chapters rather than repeatedly at twelve. Mixed depth would also mean every future split re-breaks that chapter's inbound links.

### `foundations` is a chapter, not a new top-level directory

It lives at `subsections/foundations/`, so `ALLOWED_DIRS` in `build.py` needs no change and the chapter sits alongside its peers in the menu. A sibling top-level directory would require touching the build allowlist and would imply foundations is a different kind of thing than a chapter, which it is not.

### `foundations` keeps the menu slot the placeholder had

It takes the position "Common techniques" occupied — last — rather than moving to the front. Chapter order is a pedagogical decision for the author, and this change should not reorder the book as a side effect of restructuring it. If foundations-first is wanted, it is a one-line move in the nav plus one line in the README.

### Directory names use kebab-case

`subsections/mammalian_cells.md` becomes `subsections/mammalian-cells/index.md`, changing that chapter's address from `/subsections/mammalian_cells/` to `/subsections/mammalian-cells/`. Hyphens are the convention for URLs, the `content-layout` spec requires kebab-case for newly introduced path segments, and doing this now — while no address is public — avoids a mixed-convention tree where `mammalian_cells` sits beside `foundations` and `cloning`. The cost is one extra inbound link edit.

### Reading order moves from heading numbers into the nav

With one page per section, hand-written `1.1.2` numbers become a liability: inserting a section renumbers every later heading, and because the numbers appear in the generated anchors (`#112-restriction-enzymes`), every inbound link breaks with them. The menu definition in `mkdocs.yml` becomes the single place that expresses order.

Alternative considered: keep the numbers and renumber on insert. Rejected — it makes the cheapest editorial act (inserting a section) the most expensive mechanical one.

Filename prefixes (`01-plasmids.md`) were also considered and rejected: they bake order into the address, so reordering breaks links — the same trap as numbered headings, one level up.

### The nav stays hand-written in `mkdocs.yml`

An auto-nav plugin (such as `awesome-pages`, with a per-directory `.pages` file) would remove the need to list each page. Rejected: the `site-navigation` spec requires the menu be defined in one place, and now that heading numbers are gone, the nav is the only expression of reading order — that belongs somewhere explicit and reviewable, not inferred from filenames.

### `navigation.indexes` is added to the theme

Without it, a chapter with section pages renders as an inactive label and its `index.md` is unreachable from the menu. With it, the chapter entry is a link to its own landing page. Verified in the trial build: the chapter rendered as an anchor rather than a label, with `navigation.sections` left in place and no visual conflict.

### The glossary stays at `subsections/glossary.md`

Moving it to a top-level `glossary.md` would be tidier in the abstract but would rewrite all 77 inbound links for no reader-visible benefit. It stays put, which is also what keeps this migration's link churn down to six edits.

### The placeholder figure is kept on disk

`subsections/under_construction.md` is deleted, but `media/under_construction.png` stays in `media/`. `AGENTS.md` permits removing a figure only with the maintainer's consent; dropping the page's reference to it achieves the goal without deleting a figure. An unreferenced image in `media/` is harmless — the build copies the directory wholesale and does not check for unused files.

## Risks / Trade-offs

- **A link is missed during the move** → `build.py` fails loudly on any root-relative link it cannot resolve, and mkdocs runs strict, so an unresolved link fails the build rather than shipping. Running the build is the verification step for this change, not an optional check.
- **The retired `#112-restriction-enzymes` anchor is linked from somewhere outside the repo** → Accepted. The site is unpublished and the repository has no inbound links to that anchor other than the one in `cloning.md:51`, which this change fixes.
- **Contributors are unsure whether a new page is a chapter section, a protocol, or a foundations page** → The `content-layout` spec states the rule, and `AGENTS.md` is updated to match so the guidance is where a contributor will actually look.
- **`foundations/index.md` reads as an empty chapter** → It is written as a real chapter introduction that names the sections to come, rather than a stub. This is the behavior the `content-layout` spec requires of a chapter with no section pages yet. The trade-off is that the chapter promises material that does not exist yet, which is already true of the page it replaces and is stated plainly rather than with a construction banner.
- **Chapter addresses change, so any existing bookmark breaks** → Accepted deliberately, and the reason this change is worth doing now: the addresses are not yet public, and the same migration after publication would need redirects that a static host cannot provide without per-host configuration.

## Migration Plan

Ordered so the repository is never left in a state where the build fails:

1. Create the chapter directories and `git mv` each chapter file to `index.md` within it. Using `git mv` keeps each chapter's history attached to its new path.
2. Update the six inbound links that point at moved pages (four in the README table of contents, one in `bacteria.md`, one in `mammalian_cells.md`).
3. Remove the heading numbers in the cloning chapter and convert its one numbered in-page cross-reference to a name-based link.
4. Add `foundations/index.md`; delete `under_construction.md` and point the README entry at the new chapter.
5. Update `mkdocs.yml` (nested nav, `navigation.indexes`) and `tools/site/README.md`'s "Add a page" instructions.
6. Update `AGENTS.md` to describe the new layout.
7. Run `python3 tools/site/build.py` and confirm it exits clean, then preview with `--serve` to check the nav renders as three levels with clickable chapters.

All of it lands on one topic branch as one PR. Per `AGENTS.md`, the maintainer merges.

Rollback is `git revert` of the single merge: nothing here touches build logic, generated output is git-ignored, and no reader-facing address is published yet.
