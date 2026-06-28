#!/usr/bin/env python3

import os
import re
import sys

FETCH_FILE = "fetch.txt"
M3U_FILE = "channels.m3u"


def error(msg):
    print(f"ERROR: {msg}")
    sys.exit(1)


# Check fetch.txt
if not os.path.isfile(FETCH_FILE):
    error(f"{FETCH_FILE} not found.")

# Read token
with open(FETCH_FILE, "r", encoding="utf-8") as f:
    text = f.read().strip()

match = re.search(r"__hdnea__=(.+)", text)

if not match:
    error("No __hdnea__ token found in fetch.txt.")

token = match.group(1).strip()

if not token:
    error("HDNEA token is empty.")

print("Fetched token successfully.")

# Check channels.m3u
if not os.path.isfile(M3U_FILE):
    error(f"{M3U_FILE} not found.")

# Read playlist
with open(M3U_FILE, "r", encoding="utf-8") as f:
    playlist = f.read()

# Replace all existing __hdnea__ values
new_playlist = re.sub(
    r"__hdnea__=[^&\r\n\"' ]+",
    "__hdnea__=" + token,
    playlist
)

# If no existing token exists, append it to every URL
if new_playlist == playlist:
    updated_lines = []

    for line in playlist.splitlines():
        if line.startswith("http://") or line.startswith("https://"):
            if "?" in line:
                line += "&__hdnea__=" + token
            else:
                line += "?__hdnea__=" + token
        updated_lines.append(line)

    new_playlist = "\n".join(updated_lines)

# Save updated playlist
with open(M3U_FILE, "w", encoding="utf-8", newline="\n") as f:
    f.write(new_playlist)

print("channels.m3u updated successfully.")
print("HDNEA Token:")
print(token)
