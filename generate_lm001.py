"""
LM-001 V5 — 30-Day Kaizen Tracker
Little Monk Life System

Pure Python SVG generator — no external dependencies.
Output: A3 print-ready SVG (297mm x 420mm at 96dpi = 1122.5 x 1587.4 px)
Uses viewBox 0 0 794 1123 (A4 proportion scaled to A3)

Run: python generate_lm001_v5.py
"""

from pathlib import Path
import base64
import math

# ── Output path ──────────────────────────────────────────────────────────────
OUTPUT_DIR = Path("output/svg")
OUTPUT_FILE = OUTPUT_DIR / "LM-001-30-Day-Kaizen-Tracker-V5.svg"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

LOGO_PATH = Path("assets/logos/little-monk-logo.png")

# ── Canvas ────────────────────────────────────────────────────────────────────
W = 794   # viewBox width  (≈ A3 at 96dpi, portrait)
H = 1123  # viewBox height

# ── Brand Colours ─────────────────────────────────────────────────────────────
C = {
    "sky_top":      "#B8E4F9",
    "sky_mid":      "#FFF8DC",
    "sky_bot":      "#E8F4FD",
    "deep_blue":    "#0D2B6B",
    "ink_blue":     "#1A3A8F",
    "mid_blue":     "#1565C0",
    "light_blue":   "#E3F2FD",
    "saffron":      "#D4720A",
    "gold":         "#FFD966",
    "gold_light":   "#FFF3CD",
    "torii_red":    "#C0392B",
    "green_dk":     "#2E7D32",
    "green_md":     "#43A047",
    "green_bg":     "#F1F8E9",
    "orange_dk":    "#E65100",
    "orange_md":    "#FB8C00",
    "orange_bg":    "#FFF3E0",
    "purple_dk":    "#6A1B9A",
    "purple_md":    "#8E24AA",
    "purple_bg":    "#F3E5F5",
    "ink":          "#1A1A2E",
    "slate":        "#263238",
    "parchment":    "#FFFDF5",
    "white":        "#FFFFFF",
    "mountain":     "#4A6FA5",
    "mist":         "#D6E4F0",
}


def b64(path: Path) -> str:
    if path.exists():
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""


def x_(v): return round(v, 2)
def y_(v): return round(v, 2)


# ═══════════════════════════════════════════════════════════════════════════════
# SVG BUILDER
# ═══════════════════════════════════════════════════════════════════════════════

def build_svg() -> str:
    logo_b64 = b64(LOGO_PATH)
    logo_img = f'<image href="data:image/png;base64,{logo_b64}" x="28" y="22" width="90" height="90"/>' if logo_b64 else ''

    parts = []

    # ── SVG open + defs ──────────────────────────────────────────────────────
    parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  width="297mm" height="420mm"
  viewBox="0 0 {W} {H}">

<defs>
  <!-- Sky gradient background -->
  <linearGradient id="gSky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="{C['sky_top']}"/>
    <stop offset="45%"  stop-color="{C['sky_mid']}"/>
    <stop offset="100%" stop-color="{C['sky_bot']}"/>
  </linearGradient>

  <!-- Gold banner gradient -->
  <linearGradient id="gGold" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="{C['gold_light']}"/>
    <stop offset="30%"  stop-color="{C['gold']}"/>
    <stop offset="70%"  stop-color="{C['gold']}"/>
    <stop offset="100%" stop-color="{C['gold_light']}"/>
  </linearGradient>

  <!-- Parchment gradient for scroll -->
  <linearGradient id="gParchment" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#FFF8E7"/>
    <stop offset="100%" stop-color="#F5E6C8"/>
  </linearGradient>

  <!-- Section header blue -->
  <linearGradient id="gBlueHdr" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="{C['deep_blue']}"/>
    <stop offset="100%" stop-color="{C['ink_blue']}"/>
  </linearGradient>

  <!-- Footer gradient -->
  <linearGradient id="gFooter" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#0D2B6B"/>
    <stop offset="100%" stop-color="#091A45"/>
  </linearGradient>

  <!-- Drop shadow -->
  <filter id="fShadow" x="-5%" y="-5%" width="115%" height="125%">
    <feDropShadow dx="0" dy="3" stdDeviation="4"
      flood-color="#000000" flood-opacity="0.18"/>
  </filter>

  <!-- Soft shadow for cards -->
  <filter id="fCard" x="-3%" y="-3%" width="110%" height="115%">
    <feDropShadow dx="0" dy="2" stdDeviation="3"
      flood-color="#000000" flood-opacity="0.10"/>
  </filter>

  <!-- Glow for gold text -->
  <filter id="fGlow">
    <feGaussianBlur stdDeviation="2" result="blur"/>
    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>

  <style>
    /* Google Fonts loaded via SVG foreignObject trick is unreliable in print.
       We embed font stacks that look great across platforms. */
    .f-title  {{ font-family: "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
                 font-weight: 900; }}
    .f-brush  {{ font-family: "Segoe Script", "Comic Sans MS", "Bradley Hand ITC",
                 "Brush Script MT", cursive; font-style: italic; }}
    .f-head   {{ font-family: "Trebuchet MS", "Arial Narrow", Arial, sans-serif;
                 font-weight: 700; letter-spacing: 0.5px; }}
    .f-body   {{ font-family: "Trebuchet MS", Arial, sans-serif; }}
    .f-mono   {{ font-family: "Courier New", Courier, monospace; }}
    .f-code   {{ font-family: "Trebuchet MS", Arial, sans-serif; font-weight: 600; }}
    .dash     {{ stroke-dasharray: 4,3; stroke-linecap: round; }}
  </style>
</defs>
''')

    # ════════════════════════════════════════════════════════════════════════
    # 0. FULL BACKGROUND
    # ════════════════════════════════════════════════════════════════════════
    parts.append(f'''
<!-- ═══ BACKGROUND ═══ -->
<rect width="{W}" height="{H}" fill="url(#gSky)"/>

<!-- Subtle parchment texture overlay -->
<rect width="{W}" height="{H}" fill="{C['parchment']}" opacity="0.35"/>

<!-- Top border line -->
<rect x="0" y="0" width="{W}" height="6" fill="{C['deep_blue']}"/>
''')

    # ════════════════════════════════════════════════════════════════════════
    # 0b. DECORATIVE ILLUSTRATION — TOP LANDSCAPE
    # ════════════════════════════════════════════════════════════════════════
    parts.append(f'''
<!-- ═══ TOP ILLUSTRATION STRIP ═══ -->
<!-- Sky wash behind header -->
<rect x="0" y="6" width="{W}" height="155" fill="url(#gSky)" opacity="0.6"/>

<!-- Distant hills / ground -->
<ellipse cx="650" cy="148" rx="220" ry="45" fill="#8BC34A" opacity="0.5"/>
<ellipse cx="150" cy="155" rx="180" ry="38" fill="#A5D6A7" opacity="0.4"/>

<!-- Ground strip -->
<rect x="0" y="138" width="{W}" height="22" fill="#7CB342" opacity="0.35"/>

<!-- TORII GATE — right side -->
<!-- Posts -->
<rect x="660" y="78" width="8" height="68" rx="2" fill="{C['torii_red']}"/>
<rect x="710" y="78" width="8" height="68" rx="2" fill="{C['torii_red']}"/>
<!-- Kasagi (top crossbeam) -->
<rect x="645" y="70" width="90" height="12" rx="3" fill="{C['torii_red']}"/>
<!-- Slight curve on kasagi ends -->
<path d="M645 70 Q640 65 645 70" fill="{C['torii_red']}"/>
<path d="M735 70 Q740 65 735 70" fill="{C['torii_red']}"/>
<!-- Nuki (lower crossbeam) -->
<rect x="655" y="92" width="68" height="8" rx="2" fill="{C['torii_red']}"/>
<!-- Shimagi (top rail curve) -->
<path d="M645 72 Q690 58 735 72" stroke="{C['torii_red']}" stroke-width="5"
  fill="none" stroke-linecap="round"/>

<!-- Pine tree next to torii -->
<rect x="742" y="108" width="6" height="34" rx="1" fill="#5D4037"/>
<polygon points="745,68 726,118 764,118" fill="#2E7D32"/>
<polygon points="745,80 729,122 761,122" fill="#388E3C"/>
<polygon points="745,95 731,128 759,128" fill="#43A047"/>

<!-- BIRDS flying across sky (simple M-shape birds) -->
<path d="M90,38 Q96,32 102,38 Q108,32 114,38" stroke="{C['deep_blue']}" stroke-width="2.2"
  fill="none" stroke-linecap="round"/>
<path d="M130,28 Q135,23 140,28 Q145,23 150,28" stroke="{C['deep_blue']}" stroke-width="2"
  fill="none" stroke-linecap="round"/>
<path d="M165,42 Q169,37 173,42 Q177,37 181,42" stroke="{C['deep_blue']}" stroke-width="1.8"
  fill="none" stroke-linecap="round"/>
<path d="M195,22 Q199,17 203,22 Q207,17 211,22" stroke="{C['deep_blue']}" stroke-width="1.6"
  fill="none" stroke-linecap="round"/>
<path d="M220,35 Q223,31 226,35 Q229,31 232,35" stroke="{C['deep_blue']}" stroke-width="1.5"
  fill="none" stroke-linecap="round"/>

<!-- Clouds -->
<g opacity="0.82" fill="{C['white']}">
  <ellipse cx="310" cy="35" rx="40" ry="18"/>
  <ellipse cx="340" cy="28" rx="35" ry="14"/>
  <ellipse cx="280" cy="40" rx="28" ry="12"/>
  <ellipse cx="510" cy="48" rx="32" ry="14"/>
  <ellipse cx="540" cy="40" rx="28" ry="12"/>
  <ellipse cx="485" cy="52" rx="24" ry="10"/>
</g>
''')

    # ════════════════════════════════════════════════════════════════════════
    # 1. HEADER — Logo + Title + Quote
    # ════════════════════════════════════════════════════════════════════════
    parts.append(f'''
<!-- ═══ SECTION 1: HEADER ═══ -->

<!-- Logo block -->
{logo_img}

<!-- If no logo file, draw placeholder monk -->
{"" if logo_b64 else monk_placeholder(28, 22, 90)}

<!-- LM code -->
<text x="130" y="45" class="f-head" font-size="13" fill="{C['mid_blue']}"
  letter-spacing="2">LM-001  |  VERSION 1.0</text>

<!-- MAIN TITLE: 30-DAY -->
<text x="130" y="92" class="f-title" font-size="52" fill="{C['ink']}"
  filter="url(#fShadow)">30-DAY</text>

<!-- KAIZEN — brush ink style -->
<text x="352" y="92" class="f-brush" font-size="58" fill="{C['deep_blue']}"
  filter="url(#fShadow)">Kaizen</text>

<!-- TRACKER -->
<text x="130" y="122" class="f-head" font-size="18" fill="{C['slate']}"
  letter-spacing="12">T R A C K E R</text>

<!-- Decorative line under title -->
<line x1="130" y1="130" x2="{W-28}" y2="130" stroke="{C['mid_blue']}"
  stroke-width="1.5" stroke-dasharray="8,4"/>

<!-- Quote / sub-headline -->
<text x="{W//2}" y="152" text-anchor="middle" class="f-brush"
  font-size="17" fill="{C['deep_blue']}" font-style="italic">
  ✦  If I follow a system, I can improve anything.  ✦
</text>
''')

    # ════════════════════════════════════════════════════════════════════════
    # 2. KAIZEN BANNER — parchment scroll
    # ════════════════════════════════════════════════════════════════════════
    parts.append(f'''
<!-- ═══ SECTION 2: KAIZEN BANNER (Parchment Scroll) ═══ -->

<!-- Scroll shadow -->
<rect x="18" y="166" width="{W-36}" height="72" rx="10"
  fill="#C8A84B" opacity="0.4" filter="url(#fShadow)"/>

<!-- Scroll body -->
<rect x="18" y="162" width="{W-36}" height="72" rx="10"
  fill="url(#gParchment)" stroke="{C['saffron']}" stroke-width="2.5"/>

<!-- Scroll end rolls (left & right) -->
<ellipse cx="18" cy="198" rx="10" ry="36" fill="#D4A855" opacity="0.7"/>
<ellipse cx="{W-18}" cy="198" rx="10" ry="36" fill="#D4A855" opacity="0.7"/>
<ellipse cx="18" cy="198" rx="5" ry="32" fill="#C8A030" opacity="0.5"/>
<ellipse cx="{W-18}" cy="198" rx="5" ry="32" fill="#C8A030" opacity="0.5"/>

<!-- KAIZEN big brush text -->
<text x="52" y="212" class="f-brush" font-size="42" fill="{C['ink']}"
  opacity="0.92">KAIZEN</text>

<!-- Vertical divider -->
<line x1="268" y1="172" x2="268" y2="226"
  stroke="{C['saffron']}" stroke-width="1.5" opacity="0.7"/>

<!-- Inkwell + brushes illustration (SVG drawn) -->
<g transform="translate(610, 168)">
  <!-- Ink pot -->
  <ellipse cx="30" cy="42" rx="22" ry="10" fill="#2C2C2C" opacity="0.8"/>
  <rect x="8" y="22" width="44" height="20" rx="5" fill="#1A1A1A"/>
  <ellipse cx="30" cy="22" rx="22" ry="8" fill="#2C2C2C"/>
  <ellipse cx="30" cy="22" rx="16" ry="5" fill="#0D47A1" opacity="0.6"/>
  <!-- Brushes -->
  <line x1="30" y1="8" x2="20" y2="-10" stroke="#8B6914" stroke-width="2.5"
    stroke-linecap="round"/>
  <polygon points="20,-10 17,-20 23,-10" fill="#1A1A1A"/>
  <line x1="36" y1="6" x2="50" y2="-12" stroke="#8B6914" stroke-width="2.5"
    stroke-linecap="round"/>
  <polygon points="50,-12 47,-22 53,-12" fill="#1A1A1A"/>
  <line x1="42" y1="10" x2="58" y2="2" stroke="#6B4F14" stroke-width="2"
    stroke-linecap="round"/>
  <polygon points="58,2 56,-6 62,2" fill="#1A1A1A"/>
</g>

<!-- Philosophy text -->
<text x="284" y="194" class="f-head" font-size="15.5" fill="{C['slate']}">
  Small improvements repeated daily
</text>
<text x="284" y="216" class="f-head" font-size="15.5" fill="{C['slate']}">
  create extraordinary progress.
</text>
''')

    # ════════════════════════════════════════════════════════════════════════
    # 3. MY IMPROVEMENT PROJECT
    # ════════════════════════════════════════════════════════════════════════
    parts.append(f'''
<!-- ═══ SECTION 3: MY IMPROVEMENT PROJECT ═══ -->

<rect x="18" y="246" width="{W-36}" height="66" rx="10"
  fill="{C['white']}" stroke="{C['mid_blue']}" stroke-width="1.8"
  filter="url(#fCard)"/>

<!-- Blue left accent bar -->
<rect x="18" y="246" width="7" height="66" rx="5"
  fill="{C['mid_blue']}"/>

<!-- Bullseye target icon -->
<circle cx="52" cy="279" r="18" fill="{C['light_blue']}" stroke="{C['mid_blue']}" stroke-width="1.5"/>
<circle cx="52" cy="279" r="12" fill="none" stroke="{C['mid_blue']}" stroke-width="1.5"/>
<circle cx="52" cy="279" r="6" fill="{C['mid_blue']}"/>
<circle cx="52" cy="279" r="2" fill="{C['white']}"/>

<!-- Label -->
<text x="82" y="264" class="f-head" font-size="13" fill="{C['mid_blue']}"
  letter-spacing="1">MY IMPROVEMENT PROJECT</text>

<!-- Write line 1 -->
<line x1="82" y1="282" x2="{W-28}" y2="282"
  stroke="{C['slate']}" stroke-width="1" class="dash"/>
<text x="82" y="278" class="f-body" font-size="10" fill="{C['slate']}" opacity="0.45">
  Project name (e.g. Lose 3 Kg · Study 2 Hours Daily · Walk 5000 Steps)
</text>

<!-- Write line 2 -->
<line x1="82" y1="302" x2="{W-28}" y2="302"
  stroke="{C['slate']}" stroke-width="1" class="dash"/>
''')

    # ════════════════════════════════════════════════════════════════════════
    # 4. STATE ROW — Current / Target / Actual
    # ════════════════════════════════════════════════════════════════════════
    col_w = (W - 56) // 3
    states = [
        ("Current State",  "⚑", C['mid_blue'],   C['light_blue'],  C['mid_blue'],  28),
        ("Target State",   "◎", C['green_dk'],   C['green_bg'],    C['green_md'],  28 + col_w + 10),
        ("Actual Result",  "★", C['orange_dk'],  C['orange_bg'],   C['orange_md'], 28 + (col_w+10)*2),
    ]

    parts.append(f'''
<!-- ═══ SECTION 4: STATE ROW ═══ -->
''')
    for label, icon, txt_c, bg_c, border_c, sx in states:
        parts.append(f'''
<rect x="{sx}" y="322" width="{col_w}" height="58" rx="9"
  fill="{bg_c}" stroke="{border_c}" stroke-width="1.8" filter="url(#fCard)"/>
<text x="{sx+16}" y="344" class="f-head" font-size="11" fill="{txt_c}">{icon}  {label}</text>
<line x1="{sx+16}" y1="360" x2="{sx+col_w-12}" y2="360"
  stroke="{txt_c}" stroke-width="1" class="dash"/>
<line x1="{sx+16}" y1="374" x2="{sx+col_w-12}" y2="374"
  stroke="{txt_c}" stroke-width="0.8" class="dash"/>
''')

    # ════════════════════════════════════════════════════════════════════════
    # 5. SYSTEM + TRIGGER CARDS
    # ════════════════════════════════════════════════════════════════════════
    card_w = (W - 56) // 2 - 5
    parts.append(f'''
<!-- ═══ SECTION 5: MY SYSTEM + TRIGGER BOX ═══ -->

<!-- MY SYSTEM — green card -->
<rect x="28" y="390" width="{card_w}" height="110" rx="12"
  fill="{C['green_bg']}" stroke="{C['green_md']}" stroke-width="2"
  filter="url(#fCard)"/>

<!-- Green header bar -->
<rect x="28" y="390" width="{card_w}" height="36" rx="12"
  fill="{C['green_md']}"/>
<rect x="28" y="408" width="{card_w}" height="18" fill="{C['green_md']}"/>

<!-- Gear icon circle -->
<circle cx="54" cy="408" r="15" fill="{C['green_dk']}"/>
<text x="54" y="414" text-anchor="middle" font-size="16" fill="{C['white']}">⚙</text>

<!-- MY SYSTEM label -->
<text x="76" y="413" class="f-head" font-size="14" fill="{C['white']}"
  letter-spacing="1">MY SYSTEM</text>

<!-- 3 lines -->
<text x="44" y="450" class="f-body" font-size="12" fill="{C['green_dk']}">1.</text>
<line x1="60" y1="452" x2="{28+card_w-12}" y2="452"
  stroke="{C['green_md']}" stroke-width="1" class="dash"/>
<text x="44" y="474" class="f-body" font-size="12" fill="{C['green_dk']}">2.</text>
<line x1="60" y1="476" x2="{28+card_w-12}" y2="476"
  stroke="{C['green_md']}" stroke-width="1" class="dash"/>
<text x="44" y="498" class="f-body" font-size="12" fill="{C['green_dk']}">3.</text>
<line x1="60" y1="500" x2="{28+card_w-12}" y2="500"
  stroke="{C['green_md']}" stroke-width="1" class="dash"/>

<!-- TRIGGER BOX — orange card -->
<rect x="{28+card_w+10}" y="390" width="{card_w}" height="110" rx="12"
  fill="{C['orange_bg']}" stroke="{C['orange_md']}" stroke-width="2"
  filter="url(#fCard)"/>

<!-- Orange header bar -->
<rect x="{28+card_w+10}" y="390" width="{card_w}" height="36" rx="12"
  fill="{C['orange_md']}"/>
<rect x="{28+card_w+10}" y="408" width="{card_w}" height="18"
  fill="{C['orange_md']}"/>

<!-- Lightning icon circle -->
<circle cx="{28+card_w+10+26}" cy="408" r="15" fill="{C['orange_dk']}"/>
<text x="{28+card_w+10+26}" y="414" text-anchor="middle" font-size="16"
  fill="{C['white']}">⚡</text>

<!-- TRIGGER BOX label -->
<text x="{28+card_w+10+48}" y="413" class="f-head" font-size="14"
  fill="{C['white']}" letter-spacing="1">TRIGGER BOX</text>

<!-- 3 trigger lines -->
<text x="{28+card_w+10+16}" y="450" class="f-head" font-size="11"
  fill="{C['orange_dk']}">When:</text>
<line x1="{28+card_w+10+72}" y1="452" x2="{28+card_w*2+10-12}" y2="452"
  stroke="{C['orange_md']}" stroke-width="1" class="dash"/>

<text x="{28+card_w+10+16}" y="474" class="f-head" font-size="11"
  fill="{C['orange_dk']}">Where:</text>
<line x1="{28+card_w+10+76}" y1="476" x2="{28+card_w*2+10-12}" y2="476"
  stroke="{C['orange_md']}" stroke-width="1" class="dash"/>

<text x="{28+card_w+10+16}" y="498" class="f-head" font-size="11"
  fill="{C['orange_dk']}">After:</text>
<line x1="{28+card_w+10+68}" y1="500" x2="{28+card_w*2+10-12}" y2="500"
  stroke="{C['orange_md']}" stroke-width="1" class="dash"/>
''')

    # ════════════════════════════════════════════════════════════════════════
    # 6. DAILY PROGRESS SCORE GRID — 30 days, 5 stars each
    # ════════════════════════════════════════════════════════════════════════
    grid_y = 514
    hdr_h  = 36
    cell_cols = 6
    cell_rows = 5   # 6×5 = 30 days
    cell_w = (W - 56) / cell_cols
    cell_h = 52

    parts.append(f'''
<!-- ═══ SECTION 6: DAILY PROGRESS SCORE ═══ -->

<!-- Section header -->
<rect x="18" y="{grid_y}" width="{W-36}" height="{hdr_h}" rx="10"
  fill="url(#gBlueHdr)"/>
<rect x="18" y="{grid_y+hdr_h-10}" width="{W-36}" height="10"
  fill="{C['deep_blue']}"/>

<text x="{W//2}" y="{grid_y+23}" text-anchor="middle" class="f-head"
  font-size="14" fill="{C['white']}" letter-spacing="2">
  ★  DAILY PROGRESS SCORE  ★
</text>
<text x="{W//2}" y="{grid_y+34}" text-anchor="middle" class="f-body"
  font-size="9.5" fill="{C['gold']}" letter-spacing="1">
  Shade the stars based on your daily score  (0 to 5)
</text>

<!-- Grid background -->
<rect x="18" y="{grid_y+hdr_h}" width="{W-36}" height="{cell_rows*cell_h}"
  fill="{C['white']}" stroke="{C['mid_blue']}" stroke-width="1.5"/>
''')

    # Draw 30 day cells
    for day in range(1, 31):
        row = (day - 1) // cell_cols
        col = (day - 1) % cell_cols
        cx = 18 + col * cell_w
        cy = grid_y + hdr_h + row * cell_h

        # Alternate row tinting
        row_fill = C['light_blue'] if row % 2 == 0 else C['white']

        # Cell border
        parts.append(f'''
<rect x="{x_(cx)}" y="{y_(cy)}" width="{x_(cell_w)}" height="{y_(cell_h)}"
  fill="{row_fill}" stroke="{C['mid_blue']}" stroke-width="0.6" opacity="0.5"/>
''')
        # Day number
        parts.append(f'''
<text x="{x_(cx + cell_w/2)}" y="{y_(cy + 16)}" text-anchor="middle"
  class="f-head" font-size="10" fill="{C['deep_blue']}">Day {day:02d}</text>
''')
        # 5 stars — nicely spaced
        star_total_w = 5 * 16
        star_start = cx + (cell_w - star_total_w) / 2
        for s in range(5):
            sx = star_start + s * 16 + 7
            parts.append(f'''
<text x="{x_(sx)}" y="{y_(cy+38)}" text-anchor="middle"
  font-size="16" fill="{C['gold']}" opacity="0.75">☆</text>
''')

    # ════════════════════════════════════════════════════════════════════════
    # 7. WEEKLY & MONTHLY AVERAGES
    # ════════════════════════════════════════════════════════════════════════
    avg_y = grid_y + hdr_h + cell_rows * cell_h + 14
    weeks = [
        ("WEEK 1",  C['green_dk'],  C['green_md'],  C['green_bg']),
        ("WEEK 2",  C['green_dk'],  C['green_md'],  C['green_bg']),
        ("WEEK 3",  C['orange_dk'], C['orange_md'], C['orange_bg']),
        ("WEEK 4",  C['purple_dk'], C['purple_md'], C['purple_bg']),
        ("MONTH",   C['deep_blue'], C['mid_blue'],  C['light_blue']),
    ]
    pill_w = (W - 56) / 5 - 6
    pill_h = 62

    parts.append(f'''
<!-- ═══ SECTION 7: WEEKLY & MONTHLY AVERAGE ═══ -->

<!-- Sub-header -->
<rect x="18" y="{avg_y-2}" width="{W-36}" height="24" rx="6"
  fill="{C['light_blue']}" stroke="{C['mid_blue']}" stroke-width="1"/>
<text x="{W//2}" y="{avg_y+14}" text-anchor="middle" class="f-head"
  font-size="13" fill="{C['deep_blue']}" letter-spacing="1">
  ★  WEEKLY &amp; MONTHLY AVERAGE  /5
</text>
''')

    for i, (label, txt_c, border_c, bg_c) in enumerate(weeks):
        px = 28 + i * (pill_w + 6)
        py = avg_y + 28

        parts.append(f'''
<rect x="{x_(px)}" y="{y_(py)}" width="{x_(pill_w)}" height="{pill_h}"
  rx="10" fill="{bg_c}" stroke="{border_c}" stroke-width="2"
  filter="url(#fCard)"/>
<text x="{x_(px + pill_w/2)}" y="{y_(py+20)}" text-anchor="middle"
  class="f-head" font-size="11" fill="{txt_c}">{label}</text>
<text x="{x_(px + pill_w/2)}" y="{y_(py+36)}" text-anchor="middle"
  class="f-body" font-size="9" fill="{txt_c}" opacity="0.7">AVG SCORE</text>
<!-- Score box -->
<rect x="{x_(px+10)}" y="{y_(py+42)}" width="{x_(pill_w-20)}" height="14"
  rx="4" fill="{C['white']}" stroke="{border_c}" stroke-width="1.2"/>
<text x="{x_(px + pill_w/2)}" y="{y_(py+53)}" text-anchor="middle"
  class="f-body" font-size="9" fill="{txt_c}" opacity="0.5">___ / 5</text>
''')

    # ════════════════════════════════════════════════════════════════════════
    # 8. REFLECT & IMPROVE
    # ════════════════════════════════════════════════════════════════════════
    ref_y = avg_y + 28 + pill_h + 14
    ref_col_w = (W - 66) // 3

    parts.append(f'''
<!-- ═══ SECTION 8: REFLECT & IMPROVE ═══ -->

<rect x="18" y="{ref_y}" width="{W-36}" height="106" rx="12"
  fill="{C['purple_bg']}" stroke="{C['purple_md']}" stroke-width="2"
  filter="url(#fCard)"/>

<!-- Purple header bar -->
<rect x="18" y="{ref_y}" width="{W-36}" height="30" rx="12"
  fill="{C['purple_md']}"/>
<rect x="18" y="{ref_y+18}" width="{W-36}" height="12"
  fill="{C['purple_md']}"/>

<!-- Lotus icon + Title -->
<text x="42" y="{ref_y+21}" font-size="16" fill="{C['white']}">✿</text>
<text x="66" y="{ref_y+22}" class="f-head" font-size="13" fill="{C['white']}"
  letter-spacing="2">REFLECT &amp; IMPROVE</text>
''')

    ref_cols = [
        ("💡 What helped?",           C['purple_dk']),
        ("⚠ What got in the way?",    C['purple_dk']),
        ("📈 Next small improvement", C['purple_dk']),
    ]
    for i, (label, tc) in enumerate(ref_cols):
        rx2 = 28 + i * (ref_col_w + 5)
        ry2 = ref_y + 36
        parts.append(f'''
<text x="{x_(rx2)}" y="{y_(ry2+12)}" class="f-head" font-size="11"
  fill="{tc}">{label}</text>
<line x1="{x_(rx2)}" y1="{y_(ry2+24)}" x2="{x_(rx2+ref_col_w-6)}" y2="{y_(ry2+24)}"
  stroke="{C['purple_md']}" stroke-width="1" class="dash"/>
<line x1="{x_(rx2)}" y1="{y_(ry2+40)}" x2="{x_(rx2+ref_col_w-6)}" y2="{y_(ry2+40)}"
  stroke="{C['purple_md']}" stroke-width="1" class="dash"/>
<line x1="{x_(rx2)}" y1="{y_(ry2+56)}" x2="{x_(rx2+ref_col_w-6)}" y2="{y_(ry2+56)}"
  stroke="{C['purple_md']}" stroke-width="1" class="dash"/>
''')

    # ════════════════════════════════════════════════════════════════════════
    # 9. BOTTOM FOOTER — Mountain silhouette + Brand bar
    # ════════════════════════════════════════════════════════════════════════
    footer_y = H - 90
    parts.append(f'''
<!-- ═══ SECTION 9: FOOTER ILLUSTRATION + BRAND BAR ═══ -->

<!-- Misty sky base behind mountains -->
<rect x="0" y="{footer_y-20}" width="{W}" height="110"
  fill="{C['mist']}" opacity="0.6"/>

<!-- Mountain silhouettes — far back (lighter) -->
<polygon points="0,{H} 120,{footer_y+10} 240,{H}"
  fill="{C['mountain']}" opacity="0.25"/>
<polygon points="100,{H} 260,{footer_y-10} 420,{H}"
  fill="{C['mountain']}" opacity="0.28"/>
<polygon points="370,{H} 520,{footer_y+5} 650,{H}"
  fill="{C['mountain']}" opacity="0.25"/>
<polygon points="550,{H} 700,{footer_y-15} {W},{H}"
  fill="{C['mountain']}" opacity="0.28"/>

<!-- Mountain silhouettes — front (darker) -->
<polygon points="0,{H} 80,{footer_y+20} 200,{H}"
  fill="{C['deep_blue']}" opacity="0.45"/>
<polygon points="140,{H} 310,{footer_y+8} 460,{H}"
  fill="{C['deep_blue']}" opacity="0.50"/>
<polygon points="400,{H} 580,{footer_y+5} 720,{H}"
  fill="{C['deep_blue']}" opacity="0.45"/>
<polygon points="620,{H} {W-60},{footer_y+18} {W},{H}"
  fill="{C['deep_blue']}" opacity="0.48"/>

<!-- PAGODA / TEMPLE — left side of footer -->
<g transform="translate(38, {footer_y-8})" opacity="0.85">
  <!-- Body levels -->
  <rect x="18" y="36" width="44" height="30" fill="{C['deep_blue']}"/>
  <rect x="12" y="26" width="56" height="12" rx="1" fill="{C['deep_blue']}"/>
  <rect x="22" y="16" width="36" height="12" rx="1" fill="{C['deep_blue']}"/>
  <rect x="28" y="8"  width="24" height="10" rx="1" fill="{C['deep_blue']}"/>
  <!-- Roof curves per level -->
  <path d="M10 38 Q40 28 70 38" fill="none" stroke="{C['deep_blue']}" stroke-width="4"/>
  <path d="M14 28 Q40 20 66 28" fill="none" stroke="{C['deep_blue']}" stroke-width="3.5"/>
  <path d="M20 18 Q40 11 60 18" fill="none" stroke="{C['deep_blue']}" stroke-width="3"/>
  <!-- Finial -->
  <line x1="40" y1="8" x2="40" y2="-4" stroke="{C['deep_blue']}" stroke-width="2.5"/>
  <circle cx="40" cy="-6" r="3" fill="{C['deep_blue']}"/>
  <!-- Door -->
  <rect x="31" y="48" width="18" height="18" rx="2" fill="{C['mist']}" opacity="0.4"/>
</g>

<!-- Mist layer over mountains -->
<rect x="0" y="{H-56}" width="{W}" height="30"
  fill="{C['white']}" opacity="0.22"/>

<!-- BRAND BAR — solid dark indigo -->
<rect x="0" y="{H-42}" width="{W}" height="42"
  fill="url(#gFooter)"/>

<!-- Meditating monk silhouette — left -->
<g transform="translate(22, {H-40})" opacity="0.9">
  <!-- Body -->
  <ellipse cx="18" cy="26" rx="12" ry="10" fill="{C['white']}" opacity="0.85"/>
  <!-- Head -->
  <circle cx="18" cy="12" r="9" fill="{C['white']}" opacity="0.85"/>
  <!-- Arms in meditation -->
  <path d="M6,24 Q2,30 8,32" stroke="{C['white']}" stroke-width="2.5"
    fill="none" stroke-linecap="round" opacity="0.85"/>
  <path d="M30,24 Q34,30 28,32" stroke="{C['white']}" stroke-width="2.5"
    fill="none" stroke-linecap="round" opacity="0.85"/>
  <!-- Hands together -->
  <ellipse cx="18" cy="33" rx="8" ry="4" fill="{C['white']}" opacity="0.7"/>
</g>

<!-- Brand name -->
<text x="{W//2}" y="{H-22}" text-anchor="middle" class="f-brush"
  font-size="17" fill="{C['white']}">Little Monk Life System</text>

<!-- Workflow line -->
<text x="{W//2}" y="{H-8}" text-anchor="middle" class="f-body"
  font-size="9.5" fill="{C['gold']}" letter-spacing="1">
  Goal  ➔  System  ➔  Action  ➔  Measure  ➔  Reflect  ➔  Improve
</text>

<!-- Golden heart — right -->
<text x="{W-40}" y="{H-16}" text-anchor="middle"
  font-size="20" fill="{C['gold']}">♡</text>

<!-- Bottom border line -->
<rect x="0" y="{H-3}" width="{W}" height="3" fill="{C['saffron']}"/>
''')

    # ── Close SVG ────────────────────────────────────────────────────────────
    parts.append("</svg>")

    return "\n".join(parts)


def monk_placeholder(x, y, size):
    """Draw a simple monk silhouette when no logo file exists."""
    cx = x + size // 2
    cy = y + size // 3
    return f'''
<g opacity="0.85">
  <circle cx="{cx}" cy="{cy}" r="{size//4}" fill="{C['deep_blue']}"/>
  <ellipse cx="{cx}" cy="{cy + size//3}" rx="{size//3}" ry="{size//4}"
    fill="{C['deep_blue']}"/>
  <text x="{cx}" y="{y+size}" text-anchor="middle"
    class="f-head" font-size="8" fill="{C['mid_blue']}">LITTLE MONK</text>
</g>'''


def main():
    print("Building LM-001 V5...")
    svg = build_svg()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg)

    size_kb = OUTPUT_FILE.stat().st_size / 1024
    print(f"✓  Saved: {OUTPUT_FILE.resolve()}")
    print(f"   Size:  {size_kb:.1f} KB")
    print()
    print("Next steps:")
    print("  1. Open output/svg/LM-001-30-Day-Kaizen-Tracker-V5.svg in a browser")
    print("  2. Screenshot or print-to-PDF for review")
    print("  3. For print-ready PDF: open in Inkscape → Save As PDF")
    print("     or use Chrome: File → Print → Save as PDF → A3 paper")


if __name__ == "__main__":
    main()
