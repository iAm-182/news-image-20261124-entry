#!/usr/bin/env python3
"""Render the 24 November 2026 front page for make.fun news-image-20261124 (v3).

77 stories (8 features + 69 briefs), every one verified as happening or
first reported on Tuesday 24 November 2026. v3 changes vs v2 (71 stories):
  * NEW feature: Russian drone slips into Poland again (overnight 23-24 Nov,
    Warsaw holds fire; NATO sends AWACS) -- replaces the unverified
    South-Africa-vote feature.
  * NEW feature: Tyson Fury reveals schizophrenia diagnosis (reported 24 Nov).
  * FIXED: "Kenya clears last Ebola case" dropped -- that discharge was 11 Nov.
  * FIXED: "COP31 talks stall" dropped -- the summit collapsed 22 Nov; replaced
    by the 24-Nov Pacific reaction (nations go it alone; Elders accuse Australia).
  * FIXED: "Tanzania opposition figure charged, treason" dropped -- Lissu verdict
    was 6 Nov, Pambalu charged in October.
  * FIXED: SpaceX-Tesla brief reworded to the 24-Nov news: five directors named
    to steer the merger talks (FT, Tuesday).
  * FIXED: "Shenzhen rallies listed firms" dropped (same 19-Nov declaration
    story v2 already excluded); replaced by Lilly's $291m college-AI grants.
  * FIXED: numbers band "5,300+ DRC Ebola deaths" dropped (11-Nov figure);
    replaced by 11 wounded in the Zaporizhzhia bombing (early 24 Nov).
  * NEW briefs: Trump "could have gained up to $15m" on Nvidia (FT, 24 Nov);
    Kushner says he urged Trump to ease pressure on Zelenskyy (24 Nov);
    Pope Leo XIV to vote by mail (24 Nov); Fiji closes schools 5 days
    (El Nino drought, 24 Nov); Kanton Island evacuated (24 Nov);
    Zaporizhzhia bombing wounds 11 (24 Nov); Colts cut QB Daniel Jones (24 Nov);
    Megaspeed blacklist demoted from feature to brief.
  * NOT added, date-checked and rejected: CrowdStrike-Zscaler deal (23 Nov),
    Trump credit-card cap vow (21 Nov), Jimmy Gomez resignation (23 Nov),
    South Sudan attack (22 Nov), Novoshakhtinsk refinery strike (23 Nov),
    Ohio baby-shower shooting (21 Nov), Delta outage (22 Nov),
    Nepal-India $1.62bn package (23 Nov), Kushner guarantees post (22 Nov).

Writes entry.png (1024x1024, deterministic) next to this file.

Run:  python3 render.py            -> entry.png
       python3 render.py --check    -> also prints size + sha256 + story count
"""
import hashlib
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 246, 238)
INK = (18, 18, 18)
SOFT = (58, 55, 48)
MUTED = (96, 92, 82)
RED = (172, 30, 30)
RULE = (52, 50, 44)
HAIR = (204, 198, 186)
NAVY = (22, 30, 46)

FONTDIR = "/usr/share/fonts/truetype/dejavu"


def _load(name, size):
    return ImageFont.truetype(os.path.join(FONTDIR, name), size)


def serif_b(size):
    return _load("DejaVuSerif-Bold.ttf", size)


def serif(size):
    return _load("DejaVuSerif.ttf", size)


def sans_b(size):
    return _load("DejaVuSans-Bold.ttf", size)


def sans(size):
    return _load("DejaVuSans.ttf", size)


def wrap_text(draw, text, font, width):
    """Greedy word wrap returning lines that fit `width` pixels."""
    out, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= width:
            cur = trial
        else:
            if cur:
                out.append(cur)
            cur = word
    if cur:
        out.append(cur)
    return out


def shorten(draw, text, font, width):
    """Clip text with an ellipsis so it fits `width` on one line."""
    if draw.textlength(text, font=font) <= width:
        return text
    while text and draw.textlength(text + "\u2026", font=font) > width:
        text = text[:-1]
    return text + "\u2026"


# ------------------------------------------------------------------ content
FEATURES = [
    ("TECH  \u00b7  MARKETS", (29, 78, 216),
     "Huang walks back into Nvidia HQ",
     "Board reinstates Jensen Huang as CEO after a spy inquiry. "
     "Shares jump 31% in a day."),
    ("WAR  \u00b7  THE TOLL", (124, 45, 18),
     "Russian war dead near 700,000",
     "Leaked government data puts the toll far above the official count."),
    ("EUROPE  \u00b7  NATO", (150, 20, 20),
     "Russian drone slips into Poland again",
     "Warsaw holds fire to spare civilians; NATO rushes an AWACS "
     "radar plane east."),
    ("ASIA  \u00b7  DISASTER", (185, 28, 28),
     "24 killed as fire rips through candy factory",
     "Blaze sweeps an Indonesian candy factory; rescuers search "
     "for around 30 people still missing."),
    ("EUROPE  \u00b7  MONEY", (6, 95, 70),
     "Lagarde resigns as ECB chief",
     "EU launches the search for a successor."),
    ("MIDDLE EAST", (159, 18, 57),
     "Oxfam: Gaza is now a \u2018toxic wasteland\u2019",
     "Report finds likely contamination across almost all of Gaza."),
    ("UNITED STATES", (6, 95, 70),
     "Appeals court may erase Trump conviction",
     "Federal appeals judges open the way to challenge the "
     "hush-money conviction."),
    ("SPORT  \u00b7  HEALTH", (29, 78, 216),
     "Fury reveals schizophrenia diagnosis",
     "Boxer kept the diagnosis secret for a decade; "
     "Netflix film out on Friday."),
]

BIG_NUMBERS = [
    ("700,000", "Russian war dead, leaked toll"),
    ("+31%", "Nvidia shares in a single day"),
    ("24", "dead in the Indonesia factory fire"),
    ("11", "wounded in Zaporizhzhia bombing"),
]

BRIEF_COLUMNS = [
    ("AMERICAS & EUROPE", [
        ("Zelenskyy: drone hit warship", "in Libya"),
        ("US holds Patriot shipments", "60 await OK"),
        ("Norway voids oil licences", "court rules"),
        ("Pentagon rebukes Canada", "F-35 gaps"),
        ("Melat Kiros in Congress", "first Gen Z woman"),
        ("Two NJ women indicted", "staged attack"),
        ("Princeton scientist held", "by ICE in DC"),
        ("ICE detains father, daughter", "in Seattle"),
        ("Trump pauses Army blasts", "in Iowa"),
        ("Trump targets Newsom", "548 commutations"),
        ("Patel\u2019s $41m fraud probe", "Minnesota raids"),
        ("Ex-Jackson mayor jailed", "37 months, bribery"),
        ("O\u2019Hare ground stop", "brief Thanksgiving halt"),
        ("Moscow warns Estonia", "\u2018verge of open war\u2019"),
        ("US Treasury unmasks $15bn", "shadow banks"),
        ("US banks curb AI agents", "limits over security"),
        ("Car bomb wrecks buildings", "in Colombia"),
        ("Trump to meet NATO chief", "on Wednesday"),
        ("Le Pen\u2019s three scenarios", "incl. world war"),
        ("France condemns settlers", "village attacks"),
        ("Trump \u2018up to $15m\u2019 on Nvidia", "FT estimate"),
        ("Kushner urged Trump to ease off", "on Zelenskyy"),
        ("Pope Leo XIV to vote by mail", "in US midterms"),
    ]),
    ("MIDDLE EAST \u00b7 AFRICA \u00b7 ASIA", [
        ("Vance, Rubio meet Qatari PM", "on Iran"),
        ("Israeli strikes kill 3 in Gaza", "incl. UN worker"),
        ("Drone strike on Gaza police post", "3 killed"),
        ("Hurt Gaza children reach UK", "2nd group"),
        ("Houthi attacks kill 2 in Taiz", "8 injured"),
        ("Iran files rights cases", "in US and EU courts"),
        ("Hormuz attacks at peak", "highest since war"),
        ("Iran eyed in ship cyberattacks", "WSJ reports"),
        ("23 Israeli soldiers\u2019 suicides", "16-year high"),
        ("RSF drones hit Sudan power", "mass blackouts"),
        ("DRC president signs reform", "charter change"),
        ("Sahel states reopen talks", "with ECOWAS"),
        ("Kenya wins 293,600 Saudi jobs", "in doubt"),
        ("Ghana\u2019s new banknotes", "honours Nkrumah"),
        ("China sentences official to death", "for spying"),
        ("India keeps Asia rank 3", "influence grows"),
        ("India\u2013NZ Test ends in draw", "Wellington"),
        ("Pacific nations go it alone", "after COP31 collapse"),
        ("Pacific Elders accuse Australia", "over COP31"),
        ("Fiji closes all schools 5 days", "El Ni\u00f1o drought"),
        ("Kanton Island evacuated", "a day\u2019s notice"),
        ("Zaporizhzhia bombing", "11 wounded, flats hit"),
        ("Iran warns over US blockade", "vows response"),
    ]),
    ("MARKETS \u00b7 TECH \u00b7 SCIENCE \u00b7 SPORT", [
        ("SpaceX, Tesla name 5 directors", "merger talks"),
        ("US to blacklist AI firm Megaspeed", "chip row"),
        ("Asia markets jump", "Huang returns to Nvidia"),
        ("SK hynix surges 20%", "on Huang comeback"),
        ("Seoul slides on AI fears", "bubble worries"),
        ("Sensex falls 1,484 points", "closes 82,435"),
        ("Oil down about 3%", "Libya pipeline reopens"),
        ("Malaysia curbs blacklisted firms", "must cut ties"),
        ("Lilly gives $291m for college AI", "Indiana grants"),
        ("Korea cracks down on shorting", "task force"),
        ("European fertiliser plants shut", "energy costs"),
        ("AI reads mammograms", "Cambridge NHS trial"),
        ("Genome screening hope", "more patients"),
        ("Parkinson\u2019s clue", "stem-cell model"),
        ("Plants brew cancer drug", "Nature Chem. Biol."),
        ("Tooth pain costs $2.1bn", "in Australia"),
        ("Connected cars \u2018a risk\u2019", "can track victims"),
        ("World-first \u2018megafire\u2019 sim", "UNSW AI training"),
        ("UCL tonight", "Arsenal, City, Real in action"),
        ("Bayern legend speaks out", "over Musiala"),
        ("Odhiang: model of year", "refugee-born star"),
        ("Grammy hopes: Tyla, Tems", "noms near"),
        ("Colts cut QB Daniel Jones", "after QB change"),
    ]),
]

DATE_CHECK = ("DATE CHECK \u2014 Not today\u2019s news, so not on this page: the COP31 collapse "
              "(22 Nov), the CrowdStrike\u2013Zscaler deal (23 Nov), Kenya\u2019s last Ebola "
              "discharge (11 Nov), the Tanzania treason charge (Oct). Every story here "
              "happened or was first reported on Tuesday 24 November 2026.")


# ------------------------------------------------------------------ drawing
class Page:
    """A 1024x1024 front page drawn top to bottom with a running cursor."""

    def __init__(self):
        self.img = Image.new("RGB", (W, H), PAPER)
        self.d = ImageDraw.Draw(self.img)
        self.x0, self.x1 = 30, W - 30
        self.y = 24

    def rule(self, weight=2, gap_before=0, gap_after=0):
        self.y += gap_before
        self.d.line([self.x0, self.y, self.x1, self.y], fill=RULE, width=weight)
        self.y += weight + gap_after

    def hairline(self, x_a, x_b, y):
        self.d.line([x_a, y, x_b, y], fill=HAIR, width=1)

    def masthead(self, story_total):
        d = self.d
        title = "THE WORLD IN ONE DAY"
        f_title = serif_b(56)
        tw = d.textlength(title, font=f_title)
        d.text(((W - tw) / 2, self.y), title, font=f_title, fill=INK)
        self.y += 60
        self.rule(weight=2, gap_after=7)
        f_date = sans_b(25)
        date = "TUESDAY  24  NOVEMBER  2026"
        dw = d.textlength(date, font=f_date)
        d.text(((W - dw) / 2, self.y), date, font=f_date, fill=RED)
        self.y += 31
        f_tag = sans(15)
        tag = (f"{story_total} stories from a single day \u2014 every one happened "
               "or was first reported today")
        gw = d.textlength(tag, font=f_tag)
        d.text(((W - gw) / 2, self.y), tag, font=f_tag, fill=MUTED)
        self.y += 22
        self.rule(weight=2, gap_after=9)

    def features(self):
        d = self.d
        col_w = (self.x1 - self.x0 - 24) // 2
        row_h = 88
        f_kick = sans_b(12)
        f_head = serif_b(18)
        f_deck = sans(12)
        for i, (kicker, colour, head, deck) in enumerate(FEATURES):
            cx = self.x0 + (i % 2) * (col_w + 24)
            cy = self.y + (i // 2) * row_h
            d.rectangle([cx, cy + 2, cx + 5, cy + row_h - 12], fill=colour)
            tx = cx + 14
            d.text((tx, cy), kicker, font=f_kick, fill=colour)
            lines = wrap_text(d, head, f_head, col_w - 14)[:2]
            hy = cy + 16
            for ln in lines:
                d.text((tx, hy), ln, font=f_head, fill=INK)
                hy += 21
            dlines = wrap_text(d, deck, f_deck, col_w - 14)
            dy = hy + 1
            for ln in dlines[:2]:
                d.text((tx, dy), ln, font=f_deck, fill=SOFT)
                dy += 15
            if i % 2 == 0:
                d.line([cx + col_w + 12, cy + 2, cx + col_w + 12, cy + row_h - 10],
                       fill=HAIR, width=1)
            if i // 2 < 3:
                self.hairline(cx, cx + col_w, cy + row_h - 5)
        self.y += 4 * row_h + 2
        self.rule(weight=2, gap_after=8)

    def numbers_band(self):
        d = self.d
        band_h = 52
        d.rectangle([self.x0, self.y, self.x1, self.y + band_h], fill=NAVY)
        seg = (self.x1 - self.x0) // 4
        f_num = sans_b(29)
        f_lab = sans(12)
        for i, (num, lab) in enumerate(BIG_NUMBERS):
            cx = self.x0 + i * seg + seg // 2
            nw = d.textlength(num, font=f_num)
            d.text((cx - nw / 2, self.y + 2), num, font=f_num, fill=(255, 255, 255))
            lw = d.textlength(lab, font=f_lab)
            d.text((cx - lw / 2, self.y + 34), lab, font=f_lab, fill=(198, 202, 216))
            if i:
                d.line([self.x0 + i * seg, self.y + 8,
                        self.x0 + i * seg, self.y + band_h - 8],
                       fill=(92, 100, 122), width=1)
        self.y += band_h + 8
        self.rule(weight=2, gap_after=7)

    def briefs(self):
        d = self.d
        col_w = (self.x1 - self.x0 - 2 * 20) // 3
        f_sec = sans_b(13)
        f_lead = sans_b(11)
        f_det = sans(11)
        for ci, (section, _items) in enumerate(BRIEF_COLUMNS):
            cx = self.x0 + ci * (col_w + 20)
            d.text((cx, self.y), section, font=f_sec, fill=RED)
        self.y += 19
        self.rule(weight=1, gap_after=5)
        row_h = 14
        top = self.y
        rows = max(len(items) for _, items in BRIEF_COLUMNS)
        for ci, (_section, items) in enumerate(BRIEF_COLUMNS):
            cx = self.x0 + ci * (col_w + 20)
            for ri, (lead, detail) in enumerate(items):
                ry = top + ri * row_h
                lead_w = d.textlength(lead, font=f_lead)
                tail = " \u2014 " + detail
                if lead_w + 6 + d.textlength(tail, font=f_det) > col_w - 10:
                    tail = shorten(d, tail, f_det, col_w - 10 - lead_w - 6)
                d.text((cx, ry), "\u2022 ", font=f_det, fill=RED)
                d.text((cx + 10, ry), lead, font=f_lead, fill=INK)
                d.text((cx + 10 + lead_w + 4, ry), tail, font=f_det, fill=SOFT)
            if ci < 2:
                d.line([cx + col_w + 10, top - 2,
                        cx + col_w + 10, top + rows * row_h - 2],
                       fill=HAIR, width=1)
        self.y = top + rows * row_h + 7
        self.rule(weight=2, gap_after=7)

    def footer(self):
        d = self.d
        box_top = self.y
        box_h = H - 24 - box_top
        d.rectangle([self.x0, box_top, self.x1, box_top + box_h],
                    outline=RED, width=2)
        f_dc = sans_b(13)
        lines = wrap_text(d, DATE_CHECK, f_dc, self.x1 - self.x0 - 30)
        ly = box_top + (box_h - len(lines) * 17) // 2
        for ln in lines:
            lw = d.textlength(ln, font=f_dc)
            d.text(((W - lw) / 2, ly), ln, font=f_dc, fill=(120, 20, 20))
            ly += 17
        self.y = box_top + box_h

    def frame(self):
        d = self.d
        d.rectangle([6, 6, W - 7, H - 7], outline=RULE, width=2)
        d.rectangle([12, 12, W - 13, H - 13], outline=HAIR, width=1)


def story_total():
    return len(FEATURES) + sum(len(items) for _, items in BRIEF_COLUMNS)


def build():
    page = Page()
    page.masthead(story_total())
    page.features()
    page.numbers_band()
    page.briefs()
    page.footer()
    page.frame()
    if page.y > H - 20:
        raise SystemExit(f"layout overflow: final y={page.y}")
    return page.img


def main():
    img = build()
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    if "--check" in sys.argv:
        data = open(out, "rb").read()
        print("size:", len(data), "bytes (limit 1048576)")
        print("dims:", img.size)
        print("sha256:", hashlib.sha256(data).hexdigest())
        print("stories:", story_total(),
              f"({len(FEATURES)} features + "
              f"{sum(len(it) for _, it in BRIEF_COLUMNS)} briefs)")


if __name__ == "__main__":
    main()
