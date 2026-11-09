# Spec Delta

## Purpose

Defines how the manual's Markdown sources are organized as the book grows: where a chapter's pages live, where protocols and cross-cutting techniques live, and how reading order and cross-references are expressed, so that adding a topic has one obvious correct location.

## ADDED Requirements

### Requirement: Each chapter is a directory with a landing page
A chapter SHALL be a directory under `subsections/` containing an `index.md` landing page, so that a chapter can grow from one page to many without moving its address.

#### Scenario: Chapter address
- **WHEN** the site is built
- **THEN** the molecular cloning chapter is published at `/subsections/cloning/` from `subsections/cloning/index.md`

#### Scenario: Chapter gains a section page
- **WHEN** a new section page is added inside an existing chapter directory and the site is rebuilt
- **THEN** the chapter's own address is unchanged and the new page is published beneath it

### Requirement: A chapter landing page lists its sections
A chapter's `index.md` SHALL introduce the chapter and link to each of its section pages, so a reader arriving at the chapter can see its contents without relying on the menu.

#### Scenario: Reader opens a chapter
- **WHEN** a visitor opens a chapter that has section pages
- **THEN** the landing page shows what the chapter covers and links to every section page in that chapter

#### Scenario: Chapter with no section pages yet
- **WHEN** a chapter holds only its landing page
- **THEN** that page carries the chapter's content directly and lists no empty section links

### Requirement: Protocols are a flat library with stable addresses
Protocols SHALL live as single Markdown files directly in `protocols/`, with no subdirectories, so each protocol keeps a short address that stays valid as chapters are reorganized.

#### Scenario: Protocol address
- **WHEN** the site is built
- **THEN** the PCR protocol is published at `/protocols/pcr/`

#### Scenario: Protocol shared by two chapters
- **WHEN** two different chapters both reference the same protocol
- **THEN** both link to the single file in `protocols/` rather than each holding a copy

#### Scenario: Chapter is reorganized
- **WHEN** a chapter's pages are rearranged or renamed
- **THEN** every protocol address is unchanged

### Requirement: Cross-cutting techniques live in a shared chapter
A technique that more than one chapter depends on SHALL live in the `foundations` chapter rather than inside any single topic chapter, so chapters can reference it without one chapter owning it.

#### Scenario: Technique used by several chapters
- **WHEN** a technique such as gel electrophoresis or DNA quantification is added
- **THEN** it is placed in the `foundations` chapter and other chapters link to it

#### Scenario: Technique specific to one chapter
- **WHEN** a technique applies only within a single chapter's subject
- **THEN** it is placed in that chapter rather than in `foundations`

### Requirement: The glossary is a single page
The glossary SHALL remain one Markdown file in which each term is a heading, so that every term has a stable anchor and the whole glossary is searchable within one page.

#### Scenario: Term is linked from a chapter
- **WHEN** a chapter links to a glossary term by its anchor
- **THEN** the link opens the glossary page at that term

#### Scenario: Reader looks for a term
- **WHEN** a visitor is on the glossary page
- **THEN** every defined term is present on that one page

### Requirement: Headings carry no manual section numbers
Headings SHALL NOT contain hand-written section numbers such as `1.1.2`. Reading order is carried by the site menu, so inserting a section does not require renumbering headings or repairing the anchors that numbers would otherwise appear in.

#### Scenario: Heading text
- **WHEN** any chapter page is read
- **THEN** its headings name the topic without a leading section number

#### Scenario: Section inserted mid-chapter
- **WHEN** a new section is inserted ahead of existing sections
- **THEN** no existing heading or anchor has to change

### Requirement: Cross-references name their target
A cross-reference between pages or sections SHALL identify its target by name rather than by section number, so the reference survives reordering.

#### Scenario: Reference to another section
- **WHEN** one section refers the reader to another
- **THEN** the reference links to that section by its name

### Requirement: The README table of contents lists chapters only
The README table of contents SHALL have one entry per chapter, linking to that chapter's landing page, so that adding a section within a chapter does not require a README edit.

#### Scenario: Section added to a chapter
- **WHEN** a section page is added to an existing chapter
- **THEN** the README table of contents needs no change and the new page is reachable from the chapter's landing page and the menu

#### Scenario: New chapter added
- **WHEN** a new chapter is added
- **THEN** the README table of contents gains exactly one entry for it

### Requirement: Internal links are root-relative to the source tree
Links and image references between source files SHALL be written as root-relative paths to the Markdown or image file, for example `/subsections/foundations/index.md` or `/media/plasmid.png`, so that the same link works when reading the Markdown in the repository and when reading the built site.

#### Scenario: Link read in the repository
- **WHEN** a contributor follows an internal link while browsing the Markdown sources
- **THEN** the link resolves to the referenced file

#### Scenario: Link read on the built site
- **WHEN** a visitor follows that same link on the built site
- **THEN** it resolves to the corresponding published page or image
