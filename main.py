import os

# Verified count: 150 characters (150 UTF-8 bytes, no trailing newline).
LINE = "Patch v2.4.1: Fixed human sleep. Humans now shut down at night instead of doomscrolling until 4 a.m. Side effect: mornings may feel suspiciously good."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

with open(output_path, "wb") as f:
    f.write(LINE.encode("utf-8"))
