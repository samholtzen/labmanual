# site-build Specification

## Purpose

Defines how the manual's Markdown sources are turned into a static website that can be hosted on any static file host, while the Markdown files remain the single source of truth.

## Requirements

### Requirement: Markdown is the source of truth
The build SHALL generate the site from `README.md`, `subsections/`, `protocols/`, and `media/`, and SHALL NOT modify any of those source files.

#### Scenario: Sources unchanged after a build
- **WHEN** the build is run on a clean checkout
- **THEN** `git status` shows no modified or new tracked files other than ignored build output

#### Scenario: Content edit is reflected on rebuild
- **WHEN** a sentence in a chapter's Markdown is edited and the build is re-run
- **THEN** the edited sentence appears in that chapter's HTML page

### Requirement: Non-content files are excluded
The build SHALL NOT publish `lab_manual.md`, `AGENTS.md`, `COMMENTS.md`, `openspec/`, or the build tooling itself.

#### Scenario: Excluded files absent from output
- **WHEN** the build completes
- **THEN** the output contains no page or file derived from the excluded paths

### Requirement: Output is plain static files
The build SHALL produce a self-contained folder of HTML, CSS, JavaScript, and images that works when served by any static file host, without server-side code or host-specific rewrite rules.

#### Scenario: Deep link loads directly
- **WHEN** a visitor requests the URL of any chapter or protocol page directly
- **THEN** the host returns that page's full content without a redirect to the home page

### Requirement: Links resolve under any base path
The build SHALL rewrite root-relative links and image paths (e.g. `/media/x.png`, `/protocols/pcr.md`) and `.md` links so they resolve correctly whether the site is served at the domain root or under a subpath.

#### Scenario: Site served under a subpath
- **WHEN** the output is served at `/labmanual/`
- **THEN** every image displays and every internal link navigates to the matching page

#### Scenario: Broken internal link
- **WHEN** a source file links to an internal page or image that does not exist
- **THEN** the build reports the broken link in its output

### Requirement: Math renders as typeset
The build SHALL render inline `$...$` and display `$$...$$` math as typeset equations.

#### Scenario: Bicarbonate buffer equation
- **WHEN** the mammalian cell culture page is opened
- **THEN** the `$CO_{2}$` text shows a subscript and the `$$` block shows a formatted equation, with no literal dollar signs

### Requirement: GitHub-compatible heading anchors
The build SHALL generate heading anchors with the same scheme GitHub uses, so existing in-page links keep working.

#### Scenario: Existing anchor resolves
- **WHEN** the link `#112-restriction-enzymes` in the cloning chapter is followed
- **THEN** the page scrolls to the "1.1.2 Restriction Enzymes" heading

### Requirement: Optional site URL
The build SHALL accept an optional public site URL. Without it, the output SHALL be host-agnostic. With it, the output SHALL use the URL for site-level metadata and enable instant navigation, and the build SHALL reject a value that is not an http(s) URL.

#### Scenario: Build without a site URL
- **WHEN** the build is run with no site URL
- **THEN** it succeeds and the output works at any base path

#### Scenario: Build with a site URL
- **WHEN** the build is run with `--site-url https://example.org/labmanual/`
- **THEN** it succeeds and the sitemap lists pages under that URL

#### Scenario: Invalid site URL
- **WHEN** the build is run with a site URL that is not http(s)
- **THEN** it exits non-zero with a message explaining the expected form

### Requirement: Reusable single-command build
The build SHALL be runnable with a single documented command from the repository root that installs nothing outside the project and can be re-run without manual cleanup.

#### Scenario: Repeat build
- **WHEN** the build command is run twice in a row
- **THEN** both runs succeed and the output reflects the current sources

#### Scenario: Missing dependency
- **WHEN** the build is run without the required tooling installed
- **THEN** it exits non-zero with a message saying how to install it
