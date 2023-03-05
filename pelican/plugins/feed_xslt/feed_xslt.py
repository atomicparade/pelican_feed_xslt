"""This plug-in turns post IDs and GUIDs in RSS and Atom feeds into permalinks."""

import logging

from pathlib import Path
from typing import Any, Union

from pelican import Pelican, signals  # type: ignore
from pelican.writers import Atom1Feed, Rss201rev2Feed  # type: ignore

logger = logging.getLogger(__name__)

Context = dict[str, Any]
Feed = Union[Atom1Feed, Rss201rev2Feed]


XSLT_PATH_ATOM: str = ""
XSLT_PATH_RSS: str = ""


def initalize_plugin(pelican_: Pelican) -> None:
    global XSLT_PATH_ATOM
    global XSLT_PATH_RSS

    XSLT_PATH_ATOM = pelican_.settings.get("XSLT_PATH_ATOM", "").strip()
    XSLT_PATH_RSS = pelican_.settings.get("XSLT_PATH_RSS", "").strip()


def process_feed(path: str, context: Context, feed: Feed) -> None:
    """Change RSS post GUIDs to indicate that they are permalinks."""

    if isinstance(feed, Atom1Feed):
        if len(XSLT_PATH_ATOM) > 0:
            xslt_path = XSLT_PATH_ATOM
        else:
            return
    elif isinstance(feed, Rss201rev2Feed):
        if len(XSLT_PATH_RSS) > 0:
            xslt_path = XSLT_PATH_RSS
        else:
            return
    else:
        return

    file_path = Path(path)

    with open(file_path, encoding="utf-8", mode="r+") as file:
        contents = file.read()

        lines = contents.split("\n")
        lines.insert(1, f'<?xml-stylesheet href="{xslt_path}" type="text/xsl"?>')

        file.seek(0)
        file.write("\n".join(lines))

        file.close()


def register() -> None:
    """Register the plug-in with Pelican."""
    signals.initialized.connect(initalize_plugin)
    signals.feed_written.connect(process_feed)
