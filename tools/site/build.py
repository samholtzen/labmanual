#!/usr/bin/env python3
"""Build the lab manual as a static website.

Usage (from anywhere):
    python3 tools/site/build.py            # build into _site/
    python3 tools/site/build.py --serve    # build, then serve on localhost:8000
    python3 tools/site/build.py --site-url https://example.org/labmanual/

What it does:
    1. Makes sure a project-local virtualenv has the pinned tooling.
    2. Copies an allowlist of the Markdown sources into _build/docs/ (the
       originals are never modified).
    3. Rewrites root-relative links in the copies so they work at any base path.
    4. Runs `mkdocs build --strict` to produce _site/.

--site-url is optional. Without it the output is host-agnostic (works at any
base path, pages load normally). With it, the theme's instant navigation is
enabled and the sitemap uses that URL; use it for the deployed build.

Only the standard library is used here so the script can bootstrap itself.
"""

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REQUIREMENTS = HERE / "requirements.txt"
MKDOCS_CONFIG = HERE / "mkdocs.yml"
ASSETS = HERE / "assets"
STAGE = ROOT / "_build" / "docs"
OUTPUT = ROOT / "_site"

# Only these paths are published. Everything else (lab_manual.md, AGENTS.md,
# COMMENTS.md, openspec/, tools/, ...) is deliberately left out.
ALLOWED_DIRS = ["subsections", "protocols", "media"]
HOME_SOURCE = "README.md"
HOME_TARGET = "index.md"

# Markdown link/image target that starts with "/" (root-relative), e.g.
# ](/media/x.png) or ](/protocols/pcr.md#step-2). Group 1 = path, 2 = anchor.
ROOT_RELATIVE = re.compile(r"\]\(\s*/([^)\s#]*)(#[^)\s]*)?\s*\)")


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def normalize_site_url(value):
    """Validate an http(s) URL and make sure it ends with a slash."""
    parts = urlsplit(value)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        fail(
            "--site-url must be an http(s) URL such as https://example.org/labmanual/ "
            "(got %r)." % value
        )
    return value if value.endswith("/") else value + "/"


def write_site_url_config(site_url):
    """Write a config that inherits the main one and sets site_url."""
    path = ROOT / "_build" / "mkdocs.site-url.yml"
    path.write_text(
        "INHERIT: %s\n"
        "docs_dir: %s\n"
        "site_dir: %s\n"
        "site_url: %s\n" % (MKDOCS_CONFIG, STAGE, OUTPUT, site_url),
        encoding="utf-8",
    )
    return path


def venv_python(venv):
    sub = "Scripts" if os.name == "nt" else "bin"
    return venv / sub / ("python.exe" if os.name == "nt" else "python")


def ensure_venv(venv):
    """Create the venv and install pinned requirements when they changed."""
    if sys.version_info < (3, 8):
        fail("Python 3.8 or newer is required (found %s)." % sys.version.split()[0])

    wanted = hashlib.sha256(REQUIREMENTS.read_bytes()).hexdigest()
    stamp = venv / ".requirements.sha256"
    py = venv_python(venv)

    if py.exists() and stamp.exists() and stamp.read_text().strip() == wanted:
        return py

    hint = (
        "Install manually with:\n"
        "  python3 -m venv %s\n"
        "  %s -m pip install -r %s" % (venv, py, REQUIREMENTS)
    )
    try:
        if not py.exists():
            print("Creating virtualenv at %s" % venv)
            subprocess.run([sys.executable, "-m", "venv", str(venv)], check=True)
        print("Installing pinned requirements")
        subprocess.run(
            [str(py), "-m", "pip", "install", "-q", "-r", str(REQUIREMENTS)],
            check=True,
        )
    except (subprocess.CalledProcessError, OSError) as exc:
        fail("could not set up the build tooling (%s).\n%s" % (exc, hint))

    stamp.write_text(wanted + "\n")
    return py


def rewrite_links(text, page_rel, staged_files):
    """Turn root-relative link targets into paths relative to the page.

    page_rel: staged page path relative to the stage root (posix), e.g.
              "subsections/cloning.md".
    staged_files: set of staged file paths (posix, relative to the stage).
    """
    page_dir = PurePosixPath(page_rel).parent

    def replace(match):
        target, anchor = match.group(1), match.group(2) or ""
        if target == HOME_SOURCE:
            target = HOME_TARGET
        if target not in staged_files:
            # Unknown target: leave it alone so mkdocs/strict reports it.
            return match.group(0)
        rel = os.path.relpath(target, start=str(page_dir))
        return "](%s%s)" % (PurePosixPath(rel).as_posix(), anchor)

    return ROOT_RELATIVE.sub(replace, text)


def stage_sources():
    """Copy the allowlisted sources into a clean stage; return staged paths."""
    if STAGE.exists():
        shutil.rmtree(STAGE)
    STAGE.mkdir(parents=True)

    home = ROOT / HOME_SOURCE
    if not home.is_file():
        fail("%s not found in %s" % (HOME_SOURCE, ROOT))
    shutil.copyfile(home, STAGE / HOME_TARGET)

    ignore = shutil.ignore_patterns(".DS_Store")
    for name in ALLOWED_DIRS:
        src = ROOT / name
        if not src.is_dir():
            fail("expected directory %s is missing" % src)
        shutil.copytree(src, STAGE / name, ignore=ignore)

    # Site assets (e.g. the KaTeX hook) live with the tooling, not the content.
    shutil.copytree(ASSETS / "javascripts", STAGE / "javascripts")

    staged = {
        p.relative_to(STAGE).as_posix() for p in STAGE.rglob("*") if p.is_file()
    }
    for rel in sorted(staged):
        if not rel.endswith(".md"):
            continue
        page = STAGE / rel
        original = page.read_text(encoding="utf-8")
        updated = rewrite_links(original, rel, staged)
        if updated != original:
            page.write_text(updated, encoding="utf-8")

    # Anything still root-relative could not be resolved; fail loudly.
    leftovers = []
    for rel in sorted(staged):
        if rel.endswith(".md"):
            text = (STAGE / rel).read_text(encoding="utf-8")
            for m in ROOT_RELATIVE.finditer(text):
                leftovers.append("%s: /%s" % (rel, m.group(1)))
    if leftovers:
        fail("unresolved root-relative links:\n  " + "\n  ".join(leftovers))
    return staged


def check_output():
    """Fail if the built HTML has internal root-relative href/src values."""
    bad = []
    pattern = re.compile(r'(?:href|src)="/(?!/)')
    for page in OUTPUT.rglob("*.html"):
        # The theme's 404 page is served from arbitrary paths, so it always
        # uses a root base; it is not a content page.
        if page.name == "404.html":
            continue
        if pattern.search(page.read_text(encoding="utf-8", errors="ignore")):
            bad.append(page.relative_to(OUTPUT).as_posix())
    if bad:
        fail("root-relative href/src found in output:\n  " + "\n  ".join(bad))


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--serve", action="store_true", help="serve _site/ after building")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument(
        "--site-url",
        help="public URL of the site (enables instant navigation); optional",
    )
    parser.add_argument(
        "--venv", type=Path, default=ROOT / ".venv", help="virtualenv location"
    )
    args = parser.parse_args()

    site_url = normalize_site_url(args.site_url) if args.site_url else None
    py = ensure_venv(args.venv)
    stage_sources()
    config = write_site_url_config(site_url) if site_url else MKDOCS_CONFIG

    print("Building site" + (" for %s" % site_url if site_url else ""))
    result = subprocess.run(
        [str(py), "-m", "mkdocs", "build", "--strict", "-f", str(config)]
    )
    if result.returncode != 0:
        fail("mkdocs build failed (see output above).")
    check_output()
    print("Site written to %s" % OUTPUT)

    if args.serve:
        print("Serving at http://localhost:%d (Ctrl+C to stop)" % args.port)
        try:
            subprocess.run(
                [str(py), "-m", "http.server", str(args.port), "--directory", str(OUTPUT)]
            )
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
