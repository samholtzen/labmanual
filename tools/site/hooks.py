"""MkDocs hooks for the lab manual site.

build.py stages README.md as index.md, so the default "Edit this page" link
for the home page would point at a file that does not exist in the repo.
Point it at README.md instead. Keep these names in sync with build.py.
"""

HOME_SOURCE = "README.md"
HOME_TARGET = "index.md"


def on_page_context(context, page, config, nav):
    if page.file.src_uri == HOME_TARGET and page.edit_url:
        page.edit_url = page.edit_url[: -len(HOME_TARGET)] + HOME_SOURCE
    return context
