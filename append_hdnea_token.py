import json
import os

FETCH_FILE = "fetch.txt"
CHANNELS_FILE = "channels.json"

# Read token
if not os.path.exists(FETCH_FILE):
    raise FileNotFoundError("fetch.txt not found")

with open(FETCH_FILE, "r") as f:
    token = f.read().strip()

if not token.startswith("__hdnea__="):
    raise ValueError("Invalid hdnea token format")

# Load channels.json
if not os.path.exists(CHANNELS_FILE):
    raise FileNotFoundError("channels.json not found")

with open(CHANNELS_FILE, "r", encoding="utf-8") as f:
    channels = json.load(f)

# Update token in each channel
for channel in channels:
    channel["hdnea"] = token

# Save updated channels.json
with open(CHANNELS_FILE, "w", encoding="utf-8") as f:
    json.dump(channels, f, indent=2)

print("channels.json updated successfully")
