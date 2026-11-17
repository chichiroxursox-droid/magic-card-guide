# magic-card-guide

A single-file, printable visual ID guide to 81 valuable 1990s Magic: The Gathering cards, built from the Scryfall API.

## Why it exists

Sorting a shoebox of old cards by typing names into a search box one at a time is slow. A grid of card scans with set, Reserved List status and price lets you sort by eye, or print it and bring it to a card shop.

## How it works

- **Exact printings, not card names.** Each card is a specific printing (Alpha, Unlimited, Revised, Arabian Nights through Urza's block), because the same card is worth very different amounts in different sets. Every figure links to that printing's Scryfall page.
- **Data comes from Scryfall's public API.** Prices are Scryfall's `prices.usd` (TCGplayer market, non-foil, near mint). The red **RL** badge comes from Scryfall's `reserved` flag (Reserved List cards are never reprinted, so supply is fixed).
- **Honest gaps.** Alpha cards with no active listings say "get it appraised", or show the Unlimited price as a labeled floor, instead of guessing.
- **Grouped for the hunt.** Cards are grouped by set or theme (for example, the ten Revised dual lands), each group with a running "if you had all of them" total and, where it matters, a note on what to look for. The guide totals $40,840 across 81 cards.
- **One file, no build.** Plain HTML and CSS: a responsive `auto-fill` grid, card-shaped image corners, dark mode via `prefers-color-scheme`, and a print stylesheet that avoids splitting a section across pages.
- **Scans are downloaded once, not hotlinked.** `fetch_images.py` reads each figure's Scryfall link from `guide.html`, requests that exact printing's 488x680 scan from the API, skips files already on disk, and waits 100 ms between requests as Scryfall asks.

The guide itself was built in a Claude Code session. The original fetch step was done conversationally and not saved as a script, so `fetch_images.py` was added when the project was published to restore the scans after a clone. It reproduces the original images byte for byte.

## Stack

HTML and CSS, Python 3 standard library, [Scryfall API](https://scryfall.com/docs/api). Built with Claude Code.

## Run it

Card scans are not in this repo (see Credits). Download them, then open the guide:

```bash
python3 fetch_images.py   # about 81 requests, saves to images/
open guide.html
```

## Status and limits

- Prices are a snapshot from July 2026, not live. Condition and centering move old-card prices a lot, so treat them as a starting point.
- The card list and group notes are hand-curated in `guide.html`. Adding a card means adding a figure by hand and re-running `fetch_images.py`.

## Credits

- Card data, prices and images: [Scryfall](https://scryfall.com). Card links keep Scryfall's `utm_source=api` attribution.
- Magic: The Gathering is a trademark of Wizards of the Coast LLC. Card images and names are property of Wizards of the Coast. This is unofficial Fan Content permitted under the [Fan Content Policy](https://company.wizards.com/en/legal/fancontentpolicy). Not approved or endorsed by Wizards. Portions of the materials used are property of Wizards of the Coast. © Wizards of the Coast LLC.
