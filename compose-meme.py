#!/usr/bin/env python3
"""Compose the final GTA 6 meme: top/bottom captions over the AI-made base art.

Caption text is drawn here (not by the image model) so every word is spelled
right and stays readable when the judge shrinks the picture to 480x480.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WORK = Path(__file__).resolve().parent
BASE = WORK / "media-generation-gta6-meme-base-0-44e5a5fd-5f76-41c8-b9e0-9fd0fdd43235.png"
OUT = WORK / "meme.png"

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def draw_caption(draw, text, font, cx, y, fill="white", stroke="black", stroke_w=10):
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_w)
    w = bbox[2] - bbox[0]
    draw.text((cx - w / 2, y), text, font=font, fill=fill,
              stroke_fill=stroke, stroke_width=stroke_w)


def main():
    im = Image.open(BASE).convert("RGB")
    assert im.size == (1600, 1600), im.size
    draw = ImageDraw.Draw(im)

    top_font = ImageFont.truetype(FONT_PATH, 118)
    bottom_font = ImageFont.truetype(FONT_PATH, 104)

    # Top caption over the sky.
    draw_caption(draw, "WAITED 13 YEARS", top_font, 800, 36)
    draw_caption(draw, "FOR GTA 6", top_font, 800, 168)

    # Bottom caption over the street.
    draw_caption(draw, "MY AI AGENT GOT PAID", bottom_font, 800, 1330)
    draw_caption(draw, "ON MAKE.FUN TODAY", bottom_font, 800, 1452)

    im.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
