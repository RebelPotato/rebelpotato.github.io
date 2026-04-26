import os
from pathlib import Path
from shutil import copy2

THINGS_DIR = Path("things")
SITE_DIR = Path("site")
SCRIPTS_DIR = Path("scripts")
TEMPLATES_DIR = Path("templates")
STYLE_CSS = THINGS_DIR / "style.css"


def _copy2(src: Path, dest: Path):
    copy2(src, dest)


def task_build():
    for src_path in THINGS_DIR.rglob("*"):
        if src_path.is_file():
            rel_path = src_path.relative_to(THINGS_DIR)
            dest_path = SITE_DIR / rel_path

            if src_path.suffix == ".md":
                # Convert markdown files to HTML using template
                html_dest = dest_path.with_suffix(".html")
                create_action = (
                    f'pandoc --template "{TEMPLATES_DIR / "page.html"}" '
                    f'--lua-filter "{SCRIPTS_DIR / "links.lua"}" '
                    f'-f markdown -t html5 "{src_path}" -o "{html_dest}"'
                )
                file_deps = [src_path, TEMPLATES_DIR / "page.html"]
                targets = [html_dest]
            else:
                # Copy non-markdown files to the site directory
                create_action = (_copy2, (src_path, dest_path))
                file_deps = [src_path]
                targets = [dest_path]

            yield {
                "name": str(rel_path),
                "actions": [
                    (os.makedirs, (dest_path.parent,), {"exist_ok": True}),
                    create_action,
                ],
                "file_dep": file_deps,
                "targets": targets,
                "clean": True,
            }
