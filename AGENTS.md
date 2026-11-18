# AGENTS.md

Working notes for agent sessions in this repo. This file is local only and is not committed.

## What this repo is

A gentle introductory primer for general bioengineers who are new to the wet lab. The long-term goal is a lightweight living textbook, hosted on GitHub Pages or elsewhere. It is all Markdown and images. A static site is built from it with `tools/site/build.py` (see `tools/site/README.md`); there is no CI or linter.

## Layout

| Path | Purpose |
| --- | --- |
| `README.md` | Landing page and the table of contents |
| `units/` | Textbook units (background and concepts). Each unit is a directory whose `index.md` is the unit introduction, and each chapter is one `.md` file inside it, e.g. `units/bacteria/strain-selection.md`. `units/foundations/` holds techniques shared by several units, and `units/glossary.md` is a single page |
| `protocols/` | Step-by-step protocols, linked from chapters |
| `media/` | Figures |
| `tools/site/` | Static-site build (Markdown to HTML). Output goes to `_site/`, which is git-ignored |
| `lab_manual.md` | **Deprecated.** Replaced by `units/` |

Do not edit, link to, or copy from `lab_manual.md`. Ask before deleting it.

## What agents may change

**Without asking**, as accurate copy editing or infrastructure only:

- Typos
- Broken links
- Repo infrastructure

**Never change prose or scientific claims.** Agents act as a redundancy for technical terms: check terminology and accuracy, then report concerns to the human instead of rewriting.

**New technical claims need a source.** Do not add a claim or citation unprompted. Suggest it with its source, and add it only after the human gives the go-ahead.

**Figures** are drawn by hand in Affinity Designer. Never add a figure. Remove one only with the human's consent.

## Content conventions

- **Voice:** first-person, informal, and encouraging, written for someone new to the lab. Match it in any text the human asks for.
- **Bold** important terms on first use. These are candidates for linking to a future `glossary` file, which does not exist yet.
- **Numbering:** do not number headings by hand (no `1.1.2`). Reading order comes from the `nav:` list in `tools/site/mkdocs.yml`, so refer to other sections by name. Use standard Markdown headings, and ordered lists for steps.
- **Protocols** stay generic, with optional notes on the knobs each lab can turn. Do not add lab-specific details such as where reagents are stored.
- **Structure:** the guide is organized as units (directories under `units/`) split into chapters (one `.md` file each, with a single `#` title). New topics get a chapter file inside an existing unit, or a new unit directory with an `index.md`. Add `protocols/` pages if needed (protocols stay flat, one file each), a `nav:` entry in `tools/site/mkdocs.yml`, and a README table of contents entry. Techniques that several units rely on go in `units/foundations/`. See `tools/site/README.md`.
- **Links and images** use root-relative paths for now (`/media/x.png`, `/units/x/index.md`). This may change when the site is built, so do not convert paths in bulk unless asked.

## Workflow

- Work on a topic branch, never directly on `main`.
- Push the branch and open a PR.
- **Never merge or close a PR.** That is the human's job.

## Before opening a PR

There are no automated checks, so:

1. Confirm that changed or added links and image paths resolve.
2. Preview the rendered Markdown, including tables and `$...$` math.
