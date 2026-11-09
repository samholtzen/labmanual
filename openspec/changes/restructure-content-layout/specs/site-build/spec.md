# Spec Delta

## MODIFIED Requirements

### Requirement: GitHub-compatible heading anchors
The build SHALL generate heading anchors with the same scheme GitHub uses, so existing in-page links keep working.

#### Scenario: Existing anchor resolves
- **WHEN** the link `#restriction-enzymes` in the cloning chapter is followed
- **THEN** the page scrolls to the "Restriction Enzymes" heading

#### Scenario: Anchor derived from heading text
- **WHEN** a heading's text changes
- **THEN** its anchor follows the new text under the same scheme, and links written against the old anchor no longer resolve

## ADDED Requirements

### Requirement: Nested source directories are published
The build SHALL publish Markdown sources at any directory depth within the allowed content directories, so a chapter can hold its own section pages.

#### Scenario: Page nested inside a chapter directory
- **WHEN** the build is run with a page at `subsections/cloning/pcr.md`
- **THEN** that page is published at `/subsections/cloning/pcr/`

#### Scenario: Chapter landing page
- **WHEN** a chapter directory contains `index.md`
- **THEN** the chapter is published at its directory address rather than at a separate `index` address

### Requirement: Root-relative links resolve from any depth
The build SHALL rewrite root-relative links and image paths correctly regardless of how deeply the referencing page is nested, so moving a page between depths does not require editing its links.

#### Scenario: Glossary link from a nested page
- **WHEN** a page at `subsections/cloning/pcr.md` links to `/subsections/glossary.md#oligonucleotide`
- **THEN** the published page links to the glossary page at that term

#### Scenario: Image reference from a nested page
- **WHEN** that same page references `/media/pcr.png`
- **THEN** the image displays on the published page

#### Scenario: Link to a chapter landing page
- **WHEN** any page links to `/subsections/cloning/index.md`
- **THEN** the published link navigates to the cloning chapter's address
