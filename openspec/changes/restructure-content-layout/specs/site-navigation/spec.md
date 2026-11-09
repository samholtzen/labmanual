# Spec Delta

## MODIFIED Requirements

### Requirement: Persistent menu lists all pages
The site SHALL show a menu on every page that links to the home page, every chapter, and every protocol. A chapter entry SHALL be a link to that chapter's own landing page, not an inactive grouping label, and a chapter's section pages SHALL appear beneath its entry.

#### Scenario: Protocol reachable from menu
- **WHEN** a visitor is on any page
- **THEN** the PCR protocol can be opened from the menu in one click

#### Scenario: Current page indicated
- **WHEN** a page is open
- **THEN** its entry in the menu is visibly marked as current

#### Scenario: Chapter entry is clickable
- **WHEN** a visitor clicks a chapter's entry in the menu
- **THEN** that chapter's landing page opens

#### Scenario: Section page listed under its chapter
- **WHEN** a chapter has section pages
- **THEN** those pages appear in the menu beneath that chapter's entry

### Requirement: Menu order follows the table of contents
The menu SHALL list chapters in the order of the README table of contents, with protocols grouped in their own section. Within a chapter, section pages SHALL appear in the order the menu definition gives them rather than in filename order.

#### Scenario: Chapter order
- **WHEN** the menu is viewed
- **THEN** Molecular Cloning, Bacterial Cell Culture, Mammalian Cell Culture, and Foundations appear in that order

#### Scenario: Section order within a chapter
- **WHEN** a chapter's section pages are listed in the menu
- **THEN** they appear in the order the menu definition sets, independent of their filenames

#### Scenario: Reordering a chapter's sections
- **WHEN** two section pages are reordered in the menu definition and the site is rebuilt
- **THEN** the menu shows the new order and neither page's address changes
