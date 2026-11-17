"""Download the card scans guide.html expects into images/, from Scryfall.

Card art is copyrighted by Wizards of the Coast, so the scans are not in the repo.
Each figure in guide.html links its exact printing (scryfall.com/card/<set>/<number>/...),
so this asks Scryfall's API for that printing's "normal" (488x680) scan.
Run from this folder: python3 fetch_images.py
"""
import os, re, time, urllib.request

html = open("guide.html", encoding="utf-8").read()
cards = re.findall(r'href="https://scryfall\.com/card/([^/]+)/([^/]+)/[^"]*"[^>]*><img src="(images/[^"]+)"', html)
os.makedirs("images", exist_ok=True)
for set_code, number, path in cards:
    if os.path.exists(path):
        continue
    url = f"https://api.scryfall.com/cards/{set_code}/{number}?format=image&version=normal"
    req = urllib.request.Request(url, headers={"User-Agent": "magic-card-guide/1.0", "Accept": "image/*"})
    with urllib.request.urlopen(req) as r, open(path, "wb") as f:
        f.write(r.read())
    print("saved", path)
    time.sleep(0.1)  # Scryfall asks for 50-100 ms between API requests
