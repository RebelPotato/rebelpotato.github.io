import os
from pathlib import Path


THINGS_DIR = Path("things")
SITE_DIR = Path("site")
SCRIPTS_DIR = Path("scripts")


def task_build():
    for src_path in THINGS_DIR.rglob("*"):
        if src_path.is_file():
            rel_path = src_path.relative_to(THINGS_DIR)
            dest_file = (
                rel_path.with_suffix(".html") if src_path.suffix == ".md" else rel_path
            )
            dest_path = SITE_DIR / dest_file

            yield {
                "name": str(rel_path),
                "actions": [
                    (os.makedirs, (dest_path.parent,), {"exist_ok": True}),
                    f'pandoc --lua-filter "{SCRIPTS_DIR / "links.lua"}" -f markdown -t html5 "{src_path}" -o "{dest_path}"',
                ],
                "file_dep": [src_path],
                "targets": [dest_path],
            }
