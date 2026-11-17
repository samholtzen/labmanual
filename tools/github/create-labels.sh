#!/usr/bin/env bash
# Create or update the repository's issue and PR labels on GitHub.
#
# Requires the GitHub CLI (https://cli.github.com), logged in with `gh auth login`.
# Run from anywhere inside the repo:
#     bash tools/github/create-labels.sh
# Safe to re-run: --force updates the color and description of existing labels.
set -euo pipefail

label() { gh label create "$1" --color "$2" --description "$3" --force; }

# Type of contribution (the issue forms apply the first three automatically)
label "correction"       "d73a4a" "A mistake in the Manual"
label "new-material"     "0e8a16" "Proposal for a new chapter, protocol, or unit"
label "topic-request"    "1d76db" "Request for a topic to be covered"
label "structural"       "5319e7" "Moving, splitting, or renaming content; nav or style guide"
label "glossary"         "c5def5" "Glossary entries"
label "citation-needed"  "fbca04" "A claim that needs a source"
label "figure"           "bfd4f2" "New or improved figures"

# Triage status, matching the three responses in CONTRIBUTING.md
label "needs-triage"       "ededed" "Waiting for an admin to respond"
label "go-ahead"           "0e8a16" "Approved: the assignee can start drafting"
label "needs-scope-change" "fbca04" "Approved once the scope is changed or drafts are added"
label "does-not-fit"       "000000" "Outside the scope of the Manual"

# Review flags
label "safety"           "b60205" "Hazards, PPE, waste handling, or dosing: needs extra review"
label "good first issue" "7057ff" "A good place for new contributors to start"

# Units
label "unit:cloning"         "c2e0c6" "Molecular Cloning unit"
label "unit:bacteria"        "c2e0c6" "Bacterial Cell Culture unit"
label "unit:mammalian-cells" "c2e0c6" "Mammalian Cell Culture unit"
label "unit:foundations"     "c2e0c6" "Foundations unit"
label "protocols"            "c2e0c6" "Protocols"
