# Spec Delta

## Purpose

Defines how readers move around the built site: the persistent menu, search, and page layout across devices, so the chapters and protocols are easy to find and read.

## ADDED Requirements

### Requirement: Persistent menu lists all pages
The site SHALL show a menu on every page that links to the home page, every chapter, and every protocol.

#### Scenario: Protocol reachable from menu
- **WHEN** a visitor is on any page
- **THEN** the PCR protocol can be opened from the menu in one click

#### Scenario: Current page indicated
- **WHEN** a page is open
- **THEN** its entry in the menu is visibly marked as current

### Requirement: Menu order follows the table of contents
The menu SHALL list chapters in the order of the README table of contents, with protocols grouped in their own section.

#### Scenario: Chapter order
- **WHEN** the menu is viewed
- **THEN** Molecular Cloning, Bacterial Cell Culture, Mammalian Cell Culture, and Common techniques appear in that order

### Requirement: New pages appear in the menu on rebuild
The menu SHALL be defined in one place so that adding a topic requires updating only that definition and the new Markdown file.

#### Scenario: Add a protocol
- **WHEN** a new protocol file is added, listed in the menu definition, and the site is rebuilt
- **THEN** it appears in the menu and its page loads

### Requirement: Site is searchable
The site SHALL provide full-text search over all published pages that works without a server.

#### Scenario: Search finds a term
- **WHEN** a visitor searches for "ligase"
- **THEN** results include the T4 ligase protocol and the cloning chapter

### Requirement: Readable on phones and print
The layout SHALL adapt to narrow screens with a collapsible menu, and printing a page SHALL omit the menu chrome.

#### Scenario: Phone width
- **WHEN** a page is viewed at 375 px width
- **THEN** content is readable without horizontal scrolling and the menu is reachable via a toggle

### Requirement: Instant navigation when the site URL is known
When the build is given the site's public URL, moving between pages SHALL load only the changed content, keeping the menu and header in place. Every page SHALL remain independently loadable.

#### Scenario: Click menu entry with a site URL
- **WHEN** the site was built with a site URL and a visitor clicks a menu entry
- **THEN** the new page appears with the menu and header staying in place, without a full page reload

### Requirement: Navigation works without a site URL
When the build is given no site URL, every menu entry and link SHALL still navigate correctly using ordinary page loads.

#### Scenario: Click menu entry without a site URL
- **WHEN** the site was built without a site URL and a visitor clicks a menu entry
- **THEN** the target page loads with its menu, search, and math working
