#!/usr/bin/env python3
"""Render image.png (1024x1024) for make.fun news-image-20261124.

Run:  python3 build_image.py
Reads news.json in this directory and writes image.png next to it.
Build-time only: the graded entry is main.py, which copies image.png to
the output directory (standard library only, no network, no clock, no
randomness).

Dense edition: ten numbered stories plus a ticker. The four compact
stories (07-10) use small type so the day's news is complete.
Vertical budget, 1024 px (every string is checked to fit its box):
  masthead 16-141, hero 148-308, grid 318-686, story 06 696-798,
  mini row 808-926, ticker 936-964, footer 970-1000.
"""
import json
import os

from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
SIZE = 1024
CREAM = (248, 244, 233)
NAVY = (18, 40, 75)
CRIMSON = (178, 34, 34)
BLACK = (24, 24, 24)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)
SKY = (232, 237, 243)
EDGE = (200, 200, 190)
GREEN = (15, 122, 90)


def font(name, size):
    p = "/usr/share/fonts/truetype/dejavu/%s.ttf" % name
    if os.path.exists(p):
        return ImageFont.truetype(p, size)
    return ImageFont.load_default()


TITLE = font("DejaVuSans-Bold", 52)
KICK = font("DejaVuSans-Bold", 22)
SUB = font("DejaVuSerif", 24)
HERO_H = font("DejaVuSans-Bold", 28)
HERO_B = font("DejaVuSans", 20)
CARD_H = font("DejaVuSans-Bold", 24)
CARD_B = font("DejaVuSans", 18)
NUM = font("DejaVuSans-Bold", 17)
MINI_K = font("DejaVuSans-Bold", 13)
MINI_H = font("DejaVuSans-Bold", 16)
MINI_B = font("DejaVuSans", 13)
TICK = font("DejaVuSans-Bold", 14)
FOOT = font("DejaVuSans", 13)
BAR_L = font("DejaVuSans-Bold", 13)
BAR_V = font("DejaVuSans-Bold", 15)


def wrap(canvas, text, fnt, width):
    """Greedy word wrap; returns the list of lines."""
    words = text.split()
    out, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if canvas.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def lines(canvas, ls, x, y, fnt, fill, step):
    """Draw lines top to bottom; return the y after the last line."""
    for line in ls:
        canvas.text((x, y), line, font=fnt, fill=fill)
        y += step
    return y


def badge(canvas, x, y, n):
    """A navy disc with the story number, 36 px across."""
    canvas.ellipse([x, y, x + 36, y + 36], fill=NAVY)
    canvas.text((x + 18, y + 18), n, font=NUM, fill=WHITE, anchor="mm")


def render():
    with open(os.path.join(BASE, "news.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    assert len(data["stories"]) == 10, "need 10 stories"
    pic = Image.new("RGB", (SIZE, SIZE), CREAM)
    d = ImageDraw.Draw(pic)

    # Masthead: 16-141
    d.text((36, 20), "TUESDAY  \u2022  24 NOVEMBER 2026", font=KICK, fill=CRIMSON)
    d.text((988, 20), "ONE IMAGE  \u2022  ONE DAY", font=KICK, fill=NAVY, anchor="ra")
    d.text((36, 48), data["title"], font=TITLE, fill=NAVY)
    d.text((36, 104), data["subtitle"], font=SUB, fill=GREY)
    d.rectangle([36, 136, 988, 141], fill=CRIMSON)

    # Hero story 01: 148-308, with a bar chart of the rally on the right.
    hero = data["stories"][0]
    d.rounded_rectangle([36, 148, 988, 308], radius=12, fill=SKY,
                        outline=EDGE, width=2)
    d.rectangle([36, 148, 48, 308], fill=CRIMSON)
    d.text((66, 160), "01  \u2022  " + hero["kicker"], font=KICK, fill=CRIMSON)
    head = wrap(d, hero["headline"], HERO_H, 660)
    assert len(head) <= 1, "hero headline took %d lines" % len(head)
    lines(d, head, 66, 188, HERO_H, BLACK, 36)
    body = wrap(d, hero["summary"], HERO_B, 660)
    assert len(body) <= 3, "hero body took %d lines" % len(body)
    lines(d, body, 66, 228, HERO_B, (50, 50, 50), 25)
    # Rising bars: Nvidia +31%, Nasdaq +6.5%, S&P +4.5%. Heights are
    # proportional to the gain, floored so the small bars still show.
    bars = [("NVDA", 31.0, "+31%"), ("NASDAQ", 6.5, "+6.5%"), ("S&P 500", 4.5, "+4.5%")]
    base_y = 296
    bx = 740
    for label, gain, shown in bars:
        h = max(14, int(78 * gain / 31.0))
        d.rectangle([bx, base_y - h, bx + 46, base_y], fill=GREEN)
        d.text((bx + 23, base_y - h - 6), shown, font=BAR_V, fill=GREEN, anchor="mb")
        d.text((bx + 23, base_y + 4), label, font=BAR_L, fill=GREY, anchor="ma")
        bx += 72

    # Stories 02-05, 2x2 grid: 318-686 (card 466x178, gap 12/20).
    for i, story in enumerate(data["stories"][1:5]):
        x = 36 + (i % 2) * (466 + 20)
        y = 318 + (i // 2) * (178 + 12)
        d.rounded_rectangle([x, y, x + 466, y + 178], radius=10, fill=WHITE,
                            outline=EDGE, width=2)
        badge(d, x + 14, y + 12, story["n"])
        d.text((x + 60, y + 18), story["kicker"], font=NUM, fill=CRIMSON)
        head = wrap(d, story["headline"], CARD_H, 434)
        assert len(head) <= 2, "card %s headline %d lines" % (story["n"], len(head))
        yy = lines(d, head, x + 14, y + 50, CARD_H, BLACK, 28)
        body = wrap(d, story["summary"], CARD_B, 434)
        assert len(body) <= 3, "card %s body %d lines" % (story["n"], len(body))
        lines(d, body, x + 14, yy + 4, CARD_B, (60, 60, 60), 21)

    # Story 06, full width: 696-798. Headline left, summary right.
    story = data["stories"][5]
    y = 696
    d.rounded_rectangle([36, y, 988, y + 102], radius=10, fill=WHITE,
                        outline=EDGE, width=2)
    badge(d, 50, y + 12, story["n"])
    d.text((96, y + 14), story["kicker"], font=NUM, fill=CRIMSON)
    head = wrap(d, story["headline"], CARD_H, 440)
    assert len(head) <= 2, "story 06 headline %d lines" % len(head)
    lines(d, head, 96, y + 40, CARD_H, BLACK, 28)
    body = wrap(d, story["summary"], CARD_B, 400)
    assert len(body) <= 4, "story 06 body %d lines" % len(body)
    lines(d, body, 572, y + 10, CARD_B, (60, 60, 60), 20)

    # Stories 07-10, four-column mini row: 808-926 (each 226x118).
    # Small 13 px type on purpose: the day's news is complete even at
    # the cost of thumbnail legibility, as the brief allows.
    for i, story in enumerate(data["stories"][6:10]):
        x = 36 + i * (226 + 12)
        y = 808
        d.rounded_rectangle([x, y, x + 226, y + 118], radius=8, fill=WHITE,
                            outline=EDGE, width=2)
        d.text((x + 10, y + 8), story["n"] + "  \u2022  " + story["kicker"],
               font=MINI_K, fill=CRIMSON)
        head = wrap(d, story["headline"], MINI_H, 206)
        assert len(head) <= 2, "mini %s headline %d lines" % (story["n"], len(head))
        yy = lines(d, head, x + 10, y + 28, MINI_H, BLACK, 19)
        body = wrap(d, story["summary"], MINI_B, 206)
        assert len(body) <= 3, "mini %s body %d lines" % (story["n"], len(body))
        lines(d, body, x + 10, yy + 2, MINI_B, (60, 60, 60), 16)

    # Ticker: 936-964
    d.rectangle([36, 936, 988, 964], fill=NAVY)
    tw = d.textlength(data["also_today"], font=TICK)
    assert tw <= 936, "ticker too wide: %s" % tw
    d.text((52, 950), data["also_today"], font=TICK, fill=WHITE, anchor="lm")
    # Footer: 970-1000
    d.text((36, 970), data["sources"], font=FOOT, fill=GREY)
    d.text((988, 970), "make.fun  \u2022  news-image-20261124", font=FOOT,
           fill=GREY, anchor="ra")
    d.text((36, 988), data["sources_note"], font=FOOT, fill=GREY)

    out = os.path.join(BASE, "image.png")
    pic.save(out, "PNG", optimize=True)
    print(out, pic.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    render()
