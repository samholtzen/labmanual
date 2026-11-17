# Contributing to Lab Manual

Since science is constantly evolving, and new approaches are constantly being developed, and I am unfortunately one person with a tiny human brain, I simply cannot keep up. My vision for this repository is for scientists from all career stages to edit, write, proof, and otherwise contribute to this living textbook. If you are interested in contributing, give this page a read. If you're new to Git or GitHub but still want to contribute, feel free to reach out and I can give you a quick tutorial on how to use these tools for contributing.

## AI statement

I use Claude for scaffolding the website builds and for proofreading, but none of the prose in this repository is AI generated. That means that I (or any contributor) write the text that the users actually read. If you are interested in contributing, I ask that you refrain from using AI agents to generate text that is published to this repository. Proofreading of text is fine, but make sure that you are the person doing the typing.

## Ways to contribute

There are so many ways that you can contribute to the Manual! Whether you write an entire unit or you find a typo, **YOU ARE CONTRIBUTING**! We will credit you with any changes you make to the Manual. A few are below:

1. **Writing:** If you are an expert in a particular area and you find a gap in the content of the course, we would love to have you write a chapter or create a new unit.
2. **Technical review:** someone who is not necessarily interested in writing chapters or units can instead review new PRs, exiting prose, and other aspects of the content! This is such a helpful role, since we all know how hard it is to find good reviewers in science.
3. **Figures:** Generating figures that are rigorous and elegant is an art in itself. If you are an artist who has a passion for scientific figures, we would love to have you collaborate with us.
4. **Citations:** Adding and editing references for claims that are uncited, marking claims for review, or finding better primary sources are also some often overlooked items that we take for granted.
5. **The Glossary:** If you are new to contributing and want to dip your feet into the environment, start out with reviewing or editing the glossary items! These are small changes that can have a big impact on the book's readability.

## Can I contribute without code?

Absolutely! You have a couple of options:

**Option 1, Open an issue:**: Instead of contributing by cloning the repo, branching, editing, and opening a PR, you can open an [issue](https://github.com/samholtzen/labmanual/issues). For example, if you find a typo, an unclear step, or want to contribute an entire new chapter, just open an issue. All you need is a GitHub account, which is free.

**Option 2, Send me text:** I am happy to do the legwork of porting your text over and attributing you as the source author! Feel free to send me an email with the documents you'd like converted to Markdown and incorporated into the textbook! In this case, I will convert the document whole cloth and it will undergo the same PR/review process.

**Option 3, Partner up:** If you feel like neither of those are speaking to you, or you want a mentor to help you out with learning the Git ropes, find an admin or collaborator on the repository and reach out!

## The structure of this repository

The Lab Manual is broken up into several "Units" which cover a different model organism and common technique for molecular biology at the bench. The Units are broken down into chapters, which cover one concept and are stored as individual Markdown files (one per chapter). For example, the "Bacteria" unit contains chapters discussing culturing bacteria, selecting the right strain for your job, and genetic manipulation of bacteria.

Protocols are stored as Markdown files in a separate folder called `protocols`. These protocols can be linked directly to chapters in units using in-line links, or at the end in "suggested readings."

Images you want to add to your files can be stored in `media` and can be embedded in your Markdown file.

## PRs vs Issues

We use a pull request (PR)/review/merge workflow of publishing new changes to The Lab Manual. Before you begin on your change, consider the scope of the problem and its fix. Answering the following questions can help point you down the right direction.

| Change | Route | Examples |
|---|---|---|
| Fixes | PR | Typos, grammar, broken links, formatting, a clearer sentence, a citation for an existing claim |
| Small content edits | PR | Correcting a number, time, or temperature; adding a missing step or note; a glossary entry; a better figure |
| New material | Issue | New chapter, protocol, or unit; anything over about 3 paragraphs |
| Structural changes | Issue | Moving or splitting chapters, renaming files, changing the nav or style guide |
| Safety-relevant changes | PR, flagged | Hazards, PPE, waste handling, dosing. Extra review regardless of size |


**Help, it's complicated!** Don't worry:

- If you are unsure which direction you should take, open an issue.
- If it's under 15 minutes of work, open a PR, if it's more than that, open an issue!
- A number correction is a small edit, but cite the source in the PR.

## PRs for small edits

Did you find a typo? Is there a problem with one of the steps that you can fix with a couple of line edits? Open a PR! Changing one line of a Markdown file is a tiny change in the grand scheme of things. Feel free to fork and branch without opening an issue first. When you're satisfied with it, go through the [PR template](.github/pull_request_template.md) and fill in all of the fields. This step shouldn't take long since your edits should be small. If you find that it's taking a long time to fill in, consider widening the scope of the edit and open an issue instead.

## Issues for large work

Are you interested in seeing a new topic be added to the Manual? Are you a subject matter expert who wants to communicate the basic science of your work to a wider audience? It seems like you should open an issue! You can find templates for opening issues regarding a correction, new material proposal, or a topic request.

I or one of the admins will respond as soon as we can. Once we've reviewed your proposal, you will get one of three responses:

1. **Go ahead!** If your change is adequately specified, with a detailed issue document with (preferrably) some drafts already written, we will approve this issue and assign it to you. This will be your go-ahead to draft changes to the Manual, and open a PR. The PR is not the final stage of the edit! You will be asked to go through rounds of revision by our admins, so think if it like a first submission to a journal.
2. **Go ahead, but with changes to the scope** If your change lacks either an adequate scope (i.e. a large change to several Units) or you do not have any drafts written, we will give you the go ahead, but request changes to the scope. When you have provided these in follow-up comments, we will give you the **Go ahead!** and assign the issue to you.
3. **Does not fit** If your proposed content change is either too niche, outside of the scope of the Manual, or contains banned material or prose generated with AI, we will close your issue with a reason. This does not always mean you can't submit another with a narrowed scope! It just means that particular issue is not correctly scoped.

## A typical workflow

### Fork the repository

Unless you have write access to the repository, you will have to fork the repo to your own GitHub account, do your edits on a local clone of your forked repo, then start a PR once you are ready to submit for review. For first-timers, fork the repo. Otherwise, if you're a veteran, make sure your repo is up to date with `main` before creating a branch.

Make sure your GitHub credentials are in your `.bashrc` or `.zshrc`. If you don't know how to do this, follow [this guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh) from GitHub Docs that steps you through what SSH is, how to generate and add a new SSH key so you can clone this repository.

When you have your SSH credentials set up, open up a terminal and navigate to a folder you want to do your development in. After, run the following command:

```bash
git clone git@github.com:<your_github_username>/labmanual.git
cd labmanual
```

This may take a moment to download. When it's done, you can nagivate into the repo. If you're using an integrated development environment, you will see that you are currently on the `main` branch. We never develop on `main`! Instead, we generate branches, develop, then create pull requests before review and merging.

#### Version control and branching

A branch is essentially a new environment to edit the code base without worrying that you will disrupt the functionality of the code on `main`. To generate a new branch, run the following command:

```bash
git checkout -b my_new_branch
```

This will put you on a brand new branch for you to edit! Create, edit, or re-arrange to your heart's content.

#### Getting your development environment up and running

Since Markdown is a very common format for generating documentation for code, there are packages that convert markdown into HTML for rendering on a website. We use MkDocs to build our website, which is controlled by `tools/site/mkdocs.yml`. The build script, which is based on Python, can be run with a virtual environment `.venv` for local development.

When you're ready to test your changes, make the virtual environment and install the requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r tools/site/requirements.txt
```

When it finishes installing, run a test build to make sure your environment installed correctly:

```bash
python tools/site/build.py --serve
```

This will serve to `localhost:8000` if available, otherwise it will print the port it's serving the website on. Open that in your browser and click around!

#### Commit your changes

Once you're satisfied with your work, you will need to `git add` and `git commit` with a commit message to save your work. After doing this, run `git status` to check that all of your active changes are added and committed.

Once you've checked that your changes are committed, run

```bash
git push -u origin my_new_branch
```

This copies your branch to GitHub, and allows for others to review your changes.

Head to the GitHub and create a pull request (PR). You will not be able to merge this PR until one of the admins reviews it and approves it.
