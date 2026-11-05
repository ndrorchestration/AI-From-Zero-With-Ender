#!/usr/bin/env python3
"""Validate the public episode index against its provenance-aware register.

Read-only, standard-library-only. This checks structural consistency, not
YouTube publication status, rights clearance, exact upload dates, or analytics.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

VIDEO_ID_RE = re.compile(
    r"^https://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)"
    r"([A-Za-z0-9_-]{11})(?:[&#?].*)?$"
)
ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|")


def rows(path: Path, expected_columns: int) -> dict[int, list[str]]:
    result: dict[int, list[str]] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not ROW_RE.match(line):
            continue
        columns = [cell.strip() for cell in line.strip().strip("|").split("|")]
        try:
            number = int(columns[0])
        except (ValueError, IndexError) as exc:
            raise ValueError(f"{path}:{line_number}: invalid episode number") from exc
        if len(columns) != expected_columns:
            raise ValueError(
                f"{path}:{line_number}: expected {expected_columns} columns, "
                f"got {len(columns)}"
            )
        if number in result:
            raise ValueError(f"{path}:{line_number}: duplicate episode {number}")
        result[number] = columns
    if not result:
        raise ValueError(f"{path}: episode table is empty")
    if sorted(result) != list(range(1, max(result) + 1)):
        raise ValueError(f"{path}: episode numbering has gaps or does not start at 1")
    return result


def checked_video_id(url: str) -> str | None:
    match = VIDEO_ID_RE.fullmatch(url.strip())
    return match.group(1) if match else None


def validate(root: Path) -> list[str]:
    failures: list[str] = []
    try:
        readme = rows(root / "README.md", 3)
        register = rows(root / "episodes" / "README.md", 5)
    except (ValueError, OSError) as exc:
        return [str(exc)]
    if readme.keys() != register.keys():
        failures.append(
            f"episode set mismatch: README={sorted(readme)} "
            f"register={sorted(register)}"
        )
    for number in sorted(readme.keys() & register.keys()):
        summary, detail = readme[number], register[number]
        status, url, title = detail[1], detail[2], detail[3]
        if not status.strip() or not title.strip():
            failures.append(f"episode {number}: empty publication status or title")
        if not summary[1].strip():
            failures.append(f"episode {number}: empty README description")
        if url.startswith("https://"):
            video_id = checked_video_id(url)
            if not video_id:
                failures.append(f"episode {number}: invalid canonical YouTube watch URL")
            elif video_id not in summary[1]:
                failures.append(
                    f"episode {number}: register watch ID not linked in README"
                )
        elif "pending" not in url.lower():
            failures.append(
                f"episode {number}: missing watch URL must say Pending verification"
            )
        base_title = re.sub(r"\s+\(Studio snapshot(?: \d{4}-\d{2}-\d{2})?\)$", "", title)
        if base_title and base_title not in summary[1]:
            failures.append(
                f"episode {number}: register title differs from README description"
            )
    return failures


def self_test() -> None:
    assert checked_video_id("https://www.youtube.com/watch?v=ftpILoSfH3M") == "ftpILoSfH3M"
    assert checked_video_id("https://youtu.be/ftpILoSfH3M") == "ftpILoSfH3M"
    assert checked_video_id("https://example.org/watch?v=ftpILoSfH3M") is None
    assert checked_video_id("https://www.youtube.com/watch?v=NOT_A_REAL_VALID_ID_") is None
    print("PASS: validator self-tests")


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    failures = validate(Path(__file__).resolve().parent.parent)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        sys.exit(1)
    print("PASS: README and episodes/README.md have matching, coherent episode indexes")
    print("NOTE: publication, video playback, source rights, and release remain unverified")
