from datetime import datetime, timezone
import re
from pathlib import Path

year = datetime.now(timezone.utc).year
start = datetime(year, 1, 1, tzinfo=timezone.utc)
end = datetime(year, 12, 31, 23, 59, 59, tzinfo=timezone.utc)
now = datetime.now(timezone.utc)

pct = (now - start).total_seconds() / (end - start).total_seconds() * 100
capacity = 25
filled = int(pct / 100 * capacity)
bar = "█" * filled + "─" * (capacity - filled)
date_str = now.strftime("%d-%b-%Y")

line = f"⏳ **Year Progress:** `{{{bar}}}` **{pct:.2f}%** as on ⏰ **{date_str}**"

readme = Path("README.md")
content = readme.read_text()
pattern = r"<!--YEAR_PROGRESS_START-->.*?<!--YEAR_PROGRESS_END-->"
if not re.search(pattern, content, flags=re.DOTALL):
    raise SystemExit("Year progress markers not found in README.md")

updated = re.sub(
    pattern,
    f"<!--YEAR_PROGRESS_START-->\n{line}\n<!--YEAR_PROGRESS_END-->",
    content,
    count=1,
    flags=re.DOTALL,
)

readme.write_text(updated)
