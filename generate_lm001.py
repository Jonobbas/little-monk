"""
LM-001 V5.1 — 30-Day Kaizen Tracker
Little Monk Life System

Corrections applied:
  - Logo: robust base64 embed with clear error message
  - Mountains: natural rolling curves (not sharp triangles)
  - Daily grid: compact — Day + stars on SAME ROW, cell h=36px
  - Heart: artistic SVG Enso-style ornamental heart
  - Overall: Japanese Zen spiritual theme throughout
  - Brighter, more vivid colour palette
  - Artistic torii, cherry blossom, ink brush decorations

Run: python generate_lm001_v5.py
Output: output/svg/LM-001-30-Day-Kaizen-Tracker-V5.1.svg
"""

from pathlib import Path
import base64

OUTPUT_DIR = Path("output/svg")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "LM-001-30-Day-Kaizen-Tracker-V5.1.svg"

# Logo search — checks multiple locations
LOGO_CANDIDATES = [
    Path("assets/logos/little-monk-logo.png"),
    Path("assets/logos/little-monk-logo.svg"),
    Path("little-monk-logo.png"),
    Path("logo.png"),
]

W, H = 794, 1123

C = {
    "sky_dawn":     "#FFE0B2",
    "sky_mid":      "#B3E5FC",
    "sky_top":      "#E1F5FE",
    "deep_blue":    "#0D2B6B",
    "ink_blue":     "#1A3A8F",
    "mid_blue":     "#1565C0",
    "bright_blue":  "#1976D2",
    "light_blue":   "#E3F2FD",
    "pale_blue":    "#F0F8FF",
    "torii":        "#C62828",
    "torii_dk":     "#8B0000",
    "gold":         "#FFD600",
    "gold_warm":    "#FFAB00",
    "gold_pale":    "#FFF8DC",
    "saffron":      "#FF6F00",
    "green_dk":     "#1B5E20",
    "green_md":     "#388E3C",
    "green_lt":     "#A5D6A7",
    "green_bg":     "#F1F8E9",
    "orange_dk":    "#BF360C",
    "orange_md":    "#E64A19",
    "orange_bg":    "#FBE9E7",
    "purple_dk":    "#4A148C",
    "purple_md":    "#7B1FA2",
    "purple_lt":    "#CE93D8",
    "purple_bg":    "#F3E5F5",
    "cherry":       "#F48FB1",
    "cherry_dk":    "#C2185B",
    "ink":          "#0A0A1A",
    "slate":        "#1C2B3A",
    "parchment":    "#FFF8E7",
    "cream":        "#FFFEF5",
    "white":        "#FFFFFF",
    "mountain_far": "#7B9CCF",
    "mountain_mid": "#4A6FA5",
    "mountain_nea": "#1E3A5F",
    "mist":         "#E8F4FD",
}


def load_logo():
    for p in LOGO_CANDIDATES:
        if p.exists():
            ext = p.suffix.lower()
            with open(p, "rb") as f:
                data = base64.b64encode(f.read()).decode("utf-8")
            mime = "image/svg+xml" if ext == ".svg" else "image/png"
            print(f"  ✓ Logo found: {p}")
            return f'<image href="data:{mime};base64,{data}" x="24" y="18" width="95" height="95"/>'
    print("  ⚠ Logo not found — searched:")
    for p in LOGO_CANDIDATES:
        print(f"    {p.resolve()}")
    print("  Using drawn placeholder. Place logo at: assets/logos/little-monk-logo.png")
    return drawn_monk(24, 18, 95)


def drawn_monk(x, y, size):
    cx = x + size // 2
    return f'''
<g>
  <circle cx="{cx}" cy="{y+28}" r="{size//4}" fill="{C['deep_blue']}"/>
  <ellipse cx="{cx}" cy="{y+62}" rx="{size//3}" ry="{size//4}" fill="{C['deep_blue']}"/>
  <path d="M{cx-18},{y+58} Q{cx-24},{y+72} {cx-16},{y+76}"
    stroke="{C['deep_blue']}" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M{cx+18},{y+58} Q{cx+24},{y+72} {cx+16},{y+76}"
    stroke="{C['deep_blue']}" stroke-width="3" fill="none" stroke-linecap="round"/>
  <ellipse cx="{cx}" cy="{y+77}" rx="10" ry="5" fill="{C['deep_blue']}"/>
</g>'''


def ornamental_heart(cx, cy, size=24):
    """Artistic Enso-inspired heart with calligraphy brush strokes."""
    s = size / 24
    return f'''
<g transform="translate({cx},{cy}) scale({s})">
  <path d="M0,6 C-2,0 -10,-4 -10,3 C-10,10 0,18 0,22
           C0,18 10,10 10,3 C10,-4 2,0 0,6 Z"
    fill="{C['gold']}" opacity="0.92"/>
  <path d="M0,8 C-1,4 -6,-1 -6,3 C-6,8 0,15 0,19
           C0,15 6,8 6,3 C6,-1 1,4 0,8 Z"
    fill="{C['gold_warm']}" opacity="0.7"/>
  <path d="M-10,3 C-12,-4 -4,-8 0,0"
    stroke="{C['saffron']}" stroke-width="1.5" fill="none"
    stroke-linecap="round" opacity="0.6"/>
  <circle cx="0" cy="12" r="1.5" fill="{C['white']}" opacity="0.6"/>
</g>'''


def cherry_blossom(cx, cy, r=10):
    """5-petal cherry blossom."""
    petals = ""
    for i in range(5):
        angle = i * 72 - 90
        import math
        rad = math.radians(angle)
        px = cx + r * math.cos(rad)
        py = cy + r * math.sin(rad)
        petals += f'''
<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{r*0.55:.1f}" ry="{r*0.38:.1f}"
  transform="rotate({angle+90},{px:.1f},{py:.1f})"
  fill="{C['cherry']}" opacity="0.88"/>'''
    return f'''
<g>
{petals}
<circle cx="{cx}" cy="{cy}" r="{r*0.25:.1f}" fill="{C['gold']}" opacity="0.9"/>
<circle cx="{cx}" cy="{cy}" r="{r*0.12:.1f}" fill="{C['white']}" opacity="0.8"/>
</g>'''


# ─────────────────────────────────────────────────────────────────────────────
def build():
    logo_svg = load_logo()
    parts = []

    # ── SVG OPEN + DEFS ──────────────────────────────────────────────────────
    parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg"
  xmlns:xlink="http://www.w3.org/1999/xlink"
  width="297mm" height="420mm" viewBox="0 0 {W} {H}">
<defs>
  <linearGradient id="gSky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"  stop-color="{C['sky_top']}"/>
    <stop offset="40%" stop-color="{C['sky_mid']}"/>
    <stop offset="75%" stop-color="{C['sky_dawn']}"/>
    <stop offset="100%" stop-color="{C['parchment']}"/>
  </linearGradient>
  <linearGradient id="gGold" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="{C['gold_pale']}"/>
    <stop offset="25%"  stop-color="{C['gold']}"/>
    <stop offset="75%"  stop-color="{C['gold']}"/>
    <stop offset="100%" stop-color="{C['gold_pale']}"/>
  </linearGradient>
  <linearGradient id="gParchment" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#FFF9EE"/>
    <stop offset="100%" stop-color="#F2DFA0"/>
  </linearGradient>
  <linearGradient id="gBlueHdr" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="{C['deep_blue']}"/>
    <stop offset="50%"  stop-color="{C['bright_blue']}"/>
    <stop offset="100%" stop-color="{C['deep_blue']}"/>
  </linearGradient>
  <linearGradient id="gFooter" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#0D2B6B"/>
    <stop offset="100%" stop-color="#050F2A"/>
  </linearGradient>
  <linearGradient id="gGreen" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#43A047"/>
    <stop offset="100%" stop-color="#1B5E20"/>
  </linearGradient>
  <linearGradient id="gOrange" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#FF7043"/>
    <stop offset="100%" stop-color="#BF360C"/>
  </linearGradient>
  <linearGradient id="gPurple" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#AB47BC"/>
    <stop offset="100%" stop-color="#4A148C"/>
  </linearGradient>
  <filter id="fShadow">
    <feDropShadow dx="0" dy="3" stdDeviation="5"
      flood-color="#000" flood-opacity="0.20"/>
  </filter>
  <filter id="fCard">
    <feDropShadow dx="0" dy="2" stdDeviation="3"
      flood-color="#000" flood-opacity="0.12"/>
  </filter>
  <filter id="fGlow">
    <feGaussianBlur stdDeviation="3" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <style>
    .ft  {{ font-family:"Palatino Linotype",Palatino,Georgia,serif; font-weight:900; }}
    .fb  {{ font-family:"Segoe Script","Bradley Hand ITC","Comic Sans MS",cursive;
            font-style:italic; }}
    .fh  {{ font-family:"Trebuchet MS",Arial,sans-serif; font-weight:700; }}
    .fo  {{ font-family:"Trebuchet MS",Arial,sans-serif; }}
    .dash{{ stroke-dasharray:4,3; stroke-linecap:round; }}
  </style>
</defs>
''')

    # ── BACKGROUND ───────────────────────────────────────────────────────────
    parts.append(f'''
<rect width="{W}" height="{H}" fill="url(#gSky)"/>
<rect width="{W}" height="{H}" fill="{C['parchment']}" opacity="0.28"/>
<rect x="0" y="0" width="{W}" height="5" fill="{C['deep_blue']}"/>
''')

    # ── TOP ILLUSTRATION: SKY, CLOUDS, BIRDS, TORII ─────────────────────────
    parts.append(f'''
<!-- ══ HEADER ILLUSTRATION ══ -->
<!-- Soft horizon glow -->
<ellipse cx="{W//2}" cy="100" rx="380" ry="90"
  fill="{C['gold_pale']}" opacity="0.45"/>

<!-- Clouds -->
<g fill="{C['white']}" opacity="0.85">
  <ellipse cx="290" cy="38" rx="52" ry="20"/>
  <ellipse cx="328" cy="30" rx="42" ry="16"/>
  <ellipse cx="258" cy="44" rx="34" ry="14"/>
  <ellipse cx="490" cy="52" rx="44" ry="18"/>
  <ellipse cx="528" cy="42" rx="36" ry="14"/>
  <ellipse cx="460" cy="56" rx="28" ry="12"/>
  <ellipse cx="120" cy="62" rx="30" ry="12"/>
  <ellipse cx="148" cy="55" rx="26" ry="10"/>
</g>

<!-- Birds — SVG path M-shapes -->
<g stroke="{C['deep_blue']}" stroke-width="2.2" fill="none" stroke-linecap="round">
  <path d="M85,44 Q92,37 99,44 Q106,37 113,44"/>
  <path d="M132,32 Q138,26 144,32 Q150,26 156,32"/>
  <path d="M170,50 Q175,44 180,50 Q185,44 190,50"/>
  <path d="M200,25 Q205,19 210,25 Q215,19 220,25"/>
  <path d="M228,40 Q232,35 236,40 Q240,35 244,40"/>
</g>

<!-- TORII GATE — architectural SVG -->
<g filter="url(#fShadow)">
  <!-- Ground / grass mound -->
  <ellipse cx="695" cy="152" rx="80" ry="18" fill="#558B2F" opacity="0.6"/>
  <!-- Post left -->
  <rect x="656" y="72" width="10" height="82" rx="3" fill="{C['torii']}"/>
  <!-- Post right -->
  <rect x="712" y="72" width="10" height="82" rx="3" fill="{C['torii']}"/>
  <!-- Kasagi — top curved beam -->
  <path d="M638,68 Q678,52 695,56 Q712,52 740,68"
    stroke="{C['torii']}" stroke-width="12" fill="none" stroke-linecap="round"/>
  <!-- Kasagi flat part -->
  <rect x="638" y="62" width="102" height="13" rx="2" fill="{C['torii']}"/>
  <!-- Kasagi end upturns -->
  <path d="M638,62 Q632,56 638,62" fill="{C['torii']}"/>
  <path d="M740,62 Q746,56 740,62" fill="{C['torii']}"/>
  <!-- Shimagi — second beam -->
  <rect x="649" y="82" width="80" height="8" rx="2" fill="{C['torii']}"/>
  <!-- Inner shine on posts -->
  <rect x="659" y="78" width="3" height="70" rx="1" fill="{C['torii_dk']}" opacity="0.35"/>
  <rect x="715" y="78" width="3" height="70" rx="1" fill="{C['torii_dk']}" opacity="0.35"/>
</g>

<!-- Pine tree by torii -->
<rect x="752" y="108" width="7" height="46" rx="1" fill="#4E342E"/>
<polygon points="755,62 733,118 777,118" fill="{C['green_dk']}" opacity="0.9"/>
<polygon points="755,76 736,122 774,122" fill="{C['green_md']}" opacity="0.85"/>
<polygon points="755,92 738,126 772,126" fill="#43A047" opacity="0.8"/>

<!-- Cherry blossom trees — left side -->
<rect x="32" y="110" width="6" height="48" rx="1" fill="#6D4C41"/>
<rect x="22" y="96" width="6" height="52" rx="1" fill="#5D4037"/>
''')
    # Add cherry blossoms
    import math
    for bx, by in [(32,90),(22,80),(42,100),(18,92),(38,82)]:
        parts.append(cherry_blossom(bx, by, 9))
    for bx, by in [(62,108),(14,104),(50,95)]:
        parts.append(cherry_blossom(bx, by, 7))

    # ── HEADER TEXT ──────────────────────────────────────────────────────────
    parts.append(f'''
<!-- ══ HEADER TEXT ══ -->
{logo_svg}

<!-- LM code badge -->
<rect x="130" y="22" width="182" height="22" rx="6"
  fill="{C['deep_blue']}" opacity="0.12"/>
<text x="221" y="37" text-anchor="middle" class="fh" font-size="12"
  fill="{C['deep_blue']}" letter-spacing="2">LM-001  |  VERSION 1.0</text>

<!-- 30-DAY -->
<text x="130" y="90" class="ft" font-size="54" fill="{C['ink']}"
  filter="url(#fShadow)">30-DAY</text>

<!-- KAIZEN brush style -->
<text x="356" y="92" class="fb" font-size="60" fill="{C['deep_blue']}"
  filter="url(#fGlow)">Kaizen</text>

<!-- TRACKER spaced -->
<text x="130" y="122" class="fh" font-size="17" fill="{C['slate']}"
  letter-spacing="14">T R A C K E R</text>

<!-- Decorative ink brush stroke under title -->
<path d="M130,130 Q320,126 480,132 Q580,135 664,128"
  stroke="{C['saffron']}" stroke-width="2.5" fill="none"
  stroke-linecap="round" opacity="0.7"/>

<!-- Quote -->
<text x="{W//2}" y="157" text-anchor="middle" class="fb"
  font-size="16.5" fill="{C['deep_blue']}">
  ✦  If I follow a system, I can improve anything.  ✦
</text>
''')

    # ── KAIZEN SCROLL ─────────────────────────────────────────────────────────
    SY = 168
    parts.append(f'''
<!-- ══ KAIZEN PARCHMENT SCROLL ══ -->
<!-- Scroll drop shadow -->
<rect x="22" y="{SY+4}" width="{W-44}" height="74" rx="10"
  fill="#B8860B" opacity="0.3" filter="url(#fShadow)"/>
<!-- Main scroll body -->
<rect x="22" y="{SY}" width="{W-44}" height="74" rx="10"
  fill="url(#gParchment)" stroke="{C['saffron']}" stroke-width="2.2"/>
<!-- Scroll left roll -->
<ellipse cx="22" cy="{SY+37}" rx="11" ry="37" fill="#C8A44A" opacity="0.75"/>
<ellipse cx="22" cy="{SY+37}" rx="6"  ry="32" fill="#A0782A" opacity="0.5"/>
<!-- Scroll right roll -->
<ellipse cx="{W-22}" cy="{SY+37}" rx="11" ry="37" fill="#C8A44A" opacity="0.75"/>
<ellipse cx="{W-22}" cy="{SY+37}" rx="6"  ry="32" fill="#A0782A" opacity="0.5"/>
<!-- Scroll top/bottom edge lines -->
<line x1="33" y1="{SY+2}" x2="{W-33}" y2="{SY+2}"
  stroke="{C['gold_warm']}" stroke-width="1" opacity="0.6"/>
<line x1="33" y1="{SY+72}" x2="{W-33}" y2="{SY+72}"
  stroke="{C['gold_warm']}" stroke-width="1" opacity="0.6"/>

<!-- KAIZEN big brush -->
<text x="52" y="{SY+50}" class="fb" font-size="44"
  fill="{C['ink']}" opacity="0.9">KAIZEN</text>

<!-- Vertical divider with ornament -->
<line x1="272" y1="{SY+10}" x2="272" y2="{SY+64}"
  stroke="{C['saffron']}" stroke-width="1.5" opacity="0.65"/>
<circle cx="272" cy="{SY+37}" r="3" fill="{C['saffron']}" opacity="0.5"/>

<!-- Inkwell illustration -->
<g transform="translate(618,{SY+8})">
  <ellipse cx="28" cy="52" rx="22" ry="9" fill="#1A1A1A" opacity="0.75"/>
  <path d="M6,30 Q6,52 28,52 Q50,52 50,30 Q50,16 28,16 Q6,16 6,30 Z"
    fill="#111" stroke="#333" stroke-width="1"/>
  <ellipse cx="28" cy="30" rx="18" ry="8" fill="{C['deep_blue']}" opacity="0.5"/>
  <ellipse cx="28" cy="30" rx="10" ry="4" fill="{C['mid_blue']}" opacity="0.4"/>
  <line x1="28" y1="16" x2="16" y2="-6" stroke="#8B6914" stroke-width="3" stroke-linecap="round"/>
  <ellipse cx="14" cy="-8" rx="3" ry="7"
    transform="rotate(-20,14,-8)" fill="#111"/>
  <line x1="32" y1="14" x2="46" y2="-8" stroke="#7A5C10" stroke-width="2.8" stroke-linecap="round"/>
  <ellipse cx="48" cy="-10" rx="2.5" ry="6"
    transform="rotate(15,48,-10)" fill="#111"/>
  <line x1="36" y1="18" x2="54" y2="8" stroke="#6B4F14" stroke-width="2.2" stroke-linecap="round"/>
  <ellipse cx="56" cy="7" rx="2" ry="5"
    transform="rotate(30,56,7)" fill="#111"/>
</g>

<!-- Philosophy text -->
<text x="290" y="{SY+34}" class="fh" font-size="15" fill="{C['slate']}">
  Small improvements repeated daily
</text>
<text x="290" y="{SY+55}" class="fh" font-size="15" fill="{C['slate']}">
  create extraordinary progress.
</text>
''')

    # ── IMPROVEMENT PROJECT ───────────────────────────────────────────────────
    IY = 252
    parts.append(f'''
<!-- ══ MY IMPROVEMENT PROJECT ══ -->
<rect x="20" y="{IY}" width="{W-40}" height="62" rx="10"
  fill="{C['white']}" stroke="{C['mid_blue']}" stroke-width="2"
  filter="url(#fCard)"/>
<rect x="20" y="{IY}" width="8" height="62" rx="5" fill="{C['mid_blue']}"/>

<!-- Bullseye -->
<circle cx="50" cy="{IY+31}" r="18" fill="{C['light_blue']}" stroke="{C['mid_blue']}" stroke-width="2"/>
<circle cx="50" cy="{IY+31}" r="12" fill="none" stroke="{C['mid_blue']}" stroke-width="1.8"/>
<circle cx="50" cy="{IY+31}" r="6"  fill="{C['mid_blue']}"/>
<circle cx="50" cy="{IY+31}" r="2"  fill="{C['white']}"/>

<text x="80" y="{IY+20}" class="fh" font-size="12.5" fill="{C['mid_blue']}"
  letter-spacing="1.5">MY IMPROVEMENT PROJECT</text>
<text x="80" y="{IY+32}" class="fo" font-size="9.5" fill="{C['slate']}" opacity="0.4">
  Project name · e.g. Lose 3 Kg  /  Study 2 Hours Daily  /  Walk 5000 Steps
</text>
<line x1="80" y1="{IY+43}" x2="{W-28}" y2="{IY+43}"
  stroke="{C['mid_blue']}" stroke-width="1.2" class="dash"/>
<line x1="80" y1="{IY+56}" x2="{W-28}" y2="{IY+56}"
  stroke="{C['mid_blue']}" stroke-width="0.8" class="dash" opacity="0.5"/>
''')

    # ── STATE ROW ──────────────────────────────────────────────────────────────
    SRY = 322
    col_w = (W - 52) // 3 - 4
    states = [
        ("Current State",  "⚑", C['mid_blue'],   C['light_blue'],  C['mid_blue'],  20),
        ("Target State",   "◎", C['green_dk'],   C['green_bg'],    C['green_md'],  20 + col_w + 8),
        ("Actual Result",  "★", C['orange_dk'],  C['orange_bg'],   C['orange_md'], 20 + (col_w+8)*2),
    ]
    for label, icon, tc, bgc, bdc, sx in states:
        parts.append(f'''
<rect x="{sx}" y="{SRY}" width="{col_w}" height="62" rx="9"
  fill="{bgc}" stroke="{bdc}" stroke-width="2" filter="url(#fCard)"/>
<rect x="{sx}" y="{SRY}" width="{col_w}" height="26" rx="9" fill="{bdc}" opacity="0.18"/>
<text x="{sx+14}" y="{SRY+18}" class="fh" font-size="11.5" fill="{tc}">
  {icon}   {label}
</text>
<line x1="{sx+12}" y1="{SRY+38}" x2="{sx+col_w-12}" y2="{SRY+38}"
  stroke="{bdc}" stroke-width="1.2" class="dash"/>
<line x1="{sx+12}" y1="{SRY+54}" x2="{sx+col_w-12}" y2="{SRY+54}"
  stroke="{bdc}" stroke-width="0.9" class="dash" opacity="0.6"/>
''')

    # ── SYSTEM + TRIGGER ───────────────────────────────────────────────────────
    CTY = 394
    cw = (W - 52) // 2 - 4
    parts.append(f'''
<!-- ══ MY SYSTEM ══ -->
<rect x="20" y="{CTY}" width="{cw}" height="106" rx="12"
  fill="{C['green_bg']}" stroke="{C['green_md']}" stroke-width="2"
  filter="url(#fCard)"/>
<rect x="20" y="{CTY}" width="{cw}" height="34" rx="12" fill="url(#gGreen)"/>
<rect x="20" y="{CTY+22}" width="{cw}" height="12" fill="url(#gGreen)"/>
<circle cx="44" cy="{CTY+17}" r="14" fill="{C['green_dk']}"/>
<text x="44" y="{CTY+23}" text-anchor="middle" font-size="15" fill="{C['white']}">⚙</text>
<text x="64" y="{CTY+22}" class="fh" font-size="13.5" fill="{C['white']}"
  letter-spacing="1">MY SYSTEM</text>
<text x="34" y="{CTY+55}" class="fh" font-size="11" fill="{C['green_dk']}">1.</text>
<line x1="50" y1="{CTY+57}" x2="{20+cw-14}" y2="{CTY+57}"
  stroke="{C['green_md']}" stroke-width="1.1" class="dash"/>
<text x="34" y="{CTY+77}" class="fh" font-size="11" fill="{C['green_dk']}">2.</text>
<line x1="50" y1="{CTY+79}" x2="{20+cw-14}" y2="{CTY+79}"
  stroke="{C['green_md']}" stroke-width="1.1" class="dash"/>
<text x="34" y="{CTY+99}" class="fh" font-size="11" fill="{C['green_dk']}">3.</text>
<line x1="50" y1="{CTY+101}" x2="{20+cw-14}" y2="{CTY+101}"
  stroke="{C['green_md']}" stroke-width="1.1" class="dash"/>

<!-- ══ TRIGGER BOX ══ -->
<rect x="{20+cw+8}" y="{CTY}" width="{cw}" height="106" rx="12"
  fill="{C['orange_bg']}" stroke="{C['orange_md']}" stroke-width="2"
  filter="url(#fCard)"/>
<rect x="{20+cw+8}" y="{CTY}" width="{cw}" height="34" rx="12" fill="url(#gOrange)"/>
<rect x="{20+cw+8}" y="{CTY+22}" width="{cw}" height="12" fill="url(#gOrange)"/>
<circle cx="{20+cw+8+24}" cy="{CTY+17}" r="14" fill="{C['orange_dk']}"/>
<text x="{20+cw+8+24}" y="{CTY+23}" text-anchor="middle" font-size="15" fill="{C['white']}">⚡</text>
<text x="{20+cw+8+44}" y="{CTY+22}" class="fh" font-size="13.5" fill="{C['white']}"
  letter-spacing="1">TRIGGER BOX</text>
<text x="{20+cw+8+14}" y="{CTY+55}" class="fh" font-size="10.5" fill="{C['orange_dk']}">When:</text>
<line x1="{20+cw+8+70}" y1="{CTY+57}" x2="{20+cw*2+8-14}" y2="{CTY+57}"
  stroke="{C['orange_md']}" stroke-width="1.1" class="dash"/>
<text x="{20+cw+8+14}" y="{CTY+77}" class="fh" font-size="10.5" fill="{C['orange_dk']}">Where:</text>
<line x1="{20+cw+8+76}" y1="{CTY+79}" x2="{20+cw*2+8-14}" y2="{CTY+79}"
  stroke="{C['orange_md']}" stroke-width="1.1" class="dash"/>
<text x="{20+cw+8+14}" y="{CTY+99}" class="fh" font-size="10.5" fill="{C['orange_dk']}">After:</text>
<line x1="{20+cw+8+68}" y1="{CTY+101}" x2="{20+cw*2+8-14}" y2="{CTY+101}"
  stroke="{C['orange_md']}" stroke-width="1.1" class="dash"/>
''')

    # ── DAILY PROGRESS GRID ────────────────────────────────────────────────────
    # COMPACT: Day label + 5 stars on SAME ROW, cell_h=36px, 6 cols x 5 rows
    GY   = 510
    HDR  = 40
    COLS = 6
    ROWS = 5
    cell_w = (W - 40) / COLS
    cell_h = 36

    parts.append(f'''
<!-- ══ DAILY PROGRESS SCORE ══ -->
<rect x="20" y="{GY}" width="{W-40}" height="{HDR}" rx="10"
  fill="url(#gBlueHdr)"/>
<rect x="20" y="{GY+HDR-12}" width="{W-40}" height="12" fill="{C['deep_blue']}"/>
<text x="{W//2}" y="{GY+22}" text-anchor="middle" class="fh" font-size="14"
  fill="{C['white']}" letter-spacing="2">★  DAILY PROGRESS SCORE  ★</text>
<text x="{W//2}" y="{GY+36}" text-anchor="middle" class="fo" font-size="9.5"
  fill="{C['gold']}" letter-spacing="0.5">
  Shade the stars based on your daily score  ( 0 to 5 )
</text>

<!-- Grid body -->
<rect x="20" y="{GY+HDR}" width="{W-40}" height="{ROWS*cell_h}"
  fill="{C['white']}" stroke="{C['mid_blue']}" stroke-width="1.5"/>
''')

    for day in range(1, 31):
        row = (day - 1) // COLS
        col = (day - 1) % COLS
        cx  = 20 + col * cell_w
        cy  = GY + HDR + row * cell_h
        row_fill = C['pale_blue'] if row % 2 == 0 else C['white']

        # Cell background + border
        parts.append(f'''
<rect x="{cx:.1f}" y="{cy}" width="{cell_w:.1f}" height="{cell_h}"
  fill="{row_fill}" stroke="{C['mid_blue']}" stroke-width="0.5" opacity="0.6"/>''')

        # Day label — LEFT side of cell, vertically centred
        parts.append(f'''
<text x="{cx+8:.1f}" y="{cy+cell_h//2+4}" class="fh" font-size="9.5"
  fill="{C['deep_blue']}">D{day:02d}</text>''')

        # 5 stars — RIGHT of label, same row, centred
        star_x_start = cx + 46
        star_spacing = (cell_w - 54) / 5
        for s in range(5):
            sx = star_x_start + s * star_spacing + star_spacing / 2
            parts.append(f'''
<text x="{sx:.1f}" y="{cy+cell_h//2+5}" text-anchor="middle"
  font-size="14" fill="{C['gold']}" opacity="0.8">☆</text>''')

    # ── WEEKLY AVERAGES ───────────────────────────────────────────────────────
    AVY = GY + HDR + ROWS * cell_h + 12
    weeks = [
        ("WEEK 1", "gGreen",  C['green_dk'],  C['green_bg']),
        ("WEEK 2", "gGreen",  C['green_dk'],  C['green_bg']),
        ("WEEK 3", "gOrange", C['orange_dk'], C['orange_bg']),
        ("WEEK 4", "gPurple", C['purple_dk'], C['purple_bg']),
        ("MONTH",  "gBlueHdr",C['deep_blue'], C['light_blue']),
    ]
    pw = (W - 50) / 5 - 5
    ph = 68

    parts.append(f'''
<!-- ══ WEEKLY & MONTHLY AVERAGES ══ -->
<rect x="20" y="{AVY}" width="{W-40}" height="22" rx="6"
  fill="{C['light_blue']}" stroke="{C['mid_blue']}" stroke-width="1.2"/>
<text x="{W//2}" y="{AVY+15}" text-anchor="middle" class="fh" font-size="12.5"
  fill="{C['deep_blue']}" letter-spacing="1.5">
  ★  WEEKLY &amp; MONTHLY AVERAGE  / 5
</text>
''')
    for i, (label, grad, tc, bgc) in enumerate(weeks):
        px = 24 + i * (pw + 5)
        py = AVY + 28
        parts.append(f'''
<rect x="{px:.1f}" y="{py}" width="{pw:.1f}" height="{ph}" rx="10"
  fill="{bgc}" stroke="none" filter="url(#fCard)"/>
<rect x="{px:.1f}" y="{py}" width="{pw:.1f}" height="26" rx="10"
  fill="url(#{grad})"/>
<rect x="{px:.1f}" y="{py+16}" width="{pw:.1f}" height="10" fill="url(#{grad})"/>
<text x="{px+pw/2:.1f}" y="{py+18}" text-anchor="middle" class="fh"
  font-size="11" fill="{C['white']}">{label}</text>
<text x="{px+pw/2:.1f}" y="{py+38}" text-anchor="middle" class="fo"
  font-size="9" fill="{tc}" opacity="0.7">AVG SCORE</text>
<rect x="{px+8:.1f}" y="{py+44}" width="{pw-16:.1f}" height="16" rx="4"
  fill="{C['white']}" stroke="{tc}" stroke-width="1.5" opacity="0.9"/>
<text x="{px+pw/2:.1f}" y="{py+55}" text-anchor="middle" class="fo"
  font-size="9" fill="{tc}" opacity="0.45">___ / 5</text>
''')

    # ── REFLECT & IMPROVE ─────────────────────────────────────────────────────
    RFY = AVY + 28 + ph + 12
    rcw = (W - 52) // 3 - 4
    parts.append(f'''
<!-- ══ REFLECT & IMPROVE ══ -->
<rect x="20" y="{RFY}" width="{W-40}" height="102" rx="12"
  fill="{C['purple_bg']}" stroke="{C['purple_md']}" stroke-width="2"
  filter="url(#fCard)"/>
<rect x="20" y="{RFY}" width="{W-40}" height="30" rx="12" fill="url(#gPurple)"/>
<rect x="20" y="{RFY+20}" width="{W-40}" height="10" fill="url(#gPurple)"/>
<text x="46" y="{RFY+20}" font-size="16" fill="{C['white']}">✿</text>
<text x="68" y="{RFY+21}" class="fh" font-size="13" fill="{C['white']}"
  letter-spacing="2">REFLECT  &amp;  IMPROVE</text>
''')
    rcols = [
        (f"20",              "💡 What helped?",           C['purple_dk']),
        (f"{20+rcw+6}",      "⚠  What got in the way?",   C['purple_dk']),
        (f"{20+(rcw+6)*2}",  "📈 Next small improvement", C['purple_dk']),
    ]
    for rx2, label, tc in rcols:
        ry2 = RFY + 38
        parts.append(f'''
<text x="{rx2}" y="{ry2+10}" class="fh" font-size="10.5" fill="{tc}">{label}</text>
<line x1="{rx2}" y1="{ry2+22}" x2="{int(rx2)+rcw-4}" y2="{ry2+22}"
  stroke="{C['purple_lt']}" stroke-width="1.2" class="dash"/>
<line x1="{rx2}" y1="{ry2+38}" x2="{int(rx2)+rcw-4}" y2="{ry2+38}"
  stroke="{C['purple_lt']}" stroke-width="1.1" class="dash"/>
<line x1="{rx2}" y1="{ry2+54}" x2="{int(rx2)+rcw-4}" y2="{ry2+54}"
  stroke="{C['purple_lt']}" stroke-width="1.0" class="dash"/>
''')

    # ── FOOTER — NATURAL ROLLING MOUNTAINS + PAGODA ───────────────────────────
    FY = RFY + 102 + 10

    # Natural curves using bezier paths — NOT sharp triangles
    parts.append(f'''
<!-- ══ FOOTER: NATURAL MOUNTAINS ══ -->

<!-- Misty background wash -->
<rect x="0" y="{FY}" width="{W}" height="{H-FY}"
  fill="{C['mist']}" opacity="0.7"/>

<!-- Far mountains — soft pale blue rolling hills -->
<path d="M0,{FY+50}
  C60,{FY+10} 120,{FY+30} 180,{FY+15}
  C240,{FY}   300,{FY+25} 380,{FY+8}
  C440,{FY-5} 500,{FY+20} 560,{FY+5}
  C620,{FY-8} 680,{FY+18} {W},{FY+12}
  L{W},{H} L0,{H} Z"
  fill="{C['mountain_far']}" opacity="0.30"/>

<!-- Mid mountains — medium blue -->
<path d="M0,{FY+62}
  C40,{FY+28} 90,{FY+48} 150,{FY+32}
  C200,{FY+18} 260,{FY+44} 320,{FY+24}
  C370,{FY+8}  430,{FY+38} 490,{FY+20}
  C545,{FY+6}  600,{FY+35} 660,{FY+18}
  C710,{FY+5}  750,{FY+28} {W},{FY+22}
  L{W},{H} L0,{H} Z"
  fill="{C['mountain_mid']}" opacity="0.42"/>

<!-- Near mountains — darker blue, tallest peaks -->
<path d="M0,{FY+72}
  C30,{FY+48} 70,{FY+60} 110,{FY+44}
  C145,{FY+30} 185,{FY+55} 230,{FY+38}
  C268,{FY+24} 310,{FY+52} 355,{FY+34}
  C392,{FY+20} 435,{FY+50} 480,{FY+30}
  C520,{FY+14} 565,{FY+46} 610,{FY+28}
  C648,{FY+14} 695,{FY+42} 740,{FY+26}
  C765,{FY+16} 785,{FY+34} {W},{FY+28}
  L{W},{H} L0,{H} Z"
  fill="{C['mountain_nea']}" opacity="0.55"/>

<!-- Mist layer blending mountains into footer -->
<rect x="0" y="{H-68}" width="{W}" height="35"
  fill="{C['white']}" opacity="0.20"/>

<!-- PAGODA — left, elegant multi-tiered -->
<g transform="translate(36,{FY+14})" opacity="0.88">
  <!-- Foundation -->
  <rect x="14" y="54" width="52" height="8" rx="1" fill="{C['deep_blue']}"/>
  <!-- Level 1 body -->
  <rect x="22" y="38" width="36" height="18" fill="{C['deep_blue']}"/>
  <!-- Level 1 roof curve -->
  <path d="M12,40 Q40,28 68,40" fill="{C['deep_blue']}" stroke="none"/>
  <path d="M12,40 Q40,30 68,40 L68,44 Q40,32 12,44 Z" fill="{C['deep_blue']}"/>
  <!-- Level 2 body -->
  <rect x="26" y="24" width="28" height="16" fill="{C['deep_blue']}"/>
  <!-- Level 2 roof -->
  <path d="M18,26 Q40,16 62,26 L62,30 Q40,20 18,30 Z" fill="{C['deep_blue']}"/>
  <!-- Level 3 body -->
  <rect x="30" y="13" width="20" height="13" fill="{C['deep_blue']}"/>
  <!-- Level 3 roof -->
  <path d="M22,15 Q40,5 58,15 L58,19 Q40,9 22,19 Z" fill="{C['deep_blue']}"/>
  <!-- Spire -->
  <line x1="40" y1="13" x2="40" y2="-2" stroke="{C['deep_blue']}" stroke-width="3"/>
  <circle cx="40" cy="-4" r="4" fill="{C['deep_blue']}"/>
  <circle cx="40" cy="-4" r="2" fill="{C['gold']}" opacity="0.7"/>
  <!-- Door -->
  <path d="M35,50 Q40,44 45,50 L45,56 L35,56 Z" fill="{C['mist']}" opacity="0.35"/>
  <!-- Roof highlights -->
  <path d="M12,40 Q40,28 68,40" stroke="{C['mountain_far']}" stroke-width="1"
    fill="none" opacity="0.4"/>
  <path d="M18,26 Q40,16 62,26" stroke="{C['mountain_far']}" stroke-width="1"
    fill="none" opacity="0.4"/>
</g>

<!-- Small cherry blossom near pagoda -->
''')
    for bx2, by2 in [(108,FY+30),(116,FY+20),(100,FY+38),(122,FY+42)]:
        parts.append(cherry_blossom(bx2, by2, 8))
    parts.append(f'<rect x="110" y="{FY+38}" width="5" height="24" rx="1" fill="#5D4037" opacity="0.7"/>')

    # ── BRAND BAR ──────────────────────────────────────────────────────────────
    parts.append(f'''
<!-- ══ BRAND BAR ══ -->
<rect x="0" y="{H-42}" width="{W}" height="42" fill="url(#gFooter)"/>

<!-- Decorative gold top line on bar -->
<line x1="0" y1="{H-42}" x2="{W}" y2="{H-42}"
  stroke="{C['gold']}" stroke-width="1.5" opacity="0.5"/>

<!-- Meditating monk silhouette — left -->
<g transform="translate(20,{H-41})">
  <circle cx="18" cy="11" r="9" fill="{C['white']}" opacity="0.82"/>
  <ellipse cx="18" cy="28" rx="12" ry="9" fill="{C['white']}" opacity="0.82"/>
  <path d="M6,24 Q1,31 8,34" stroke="{C['white']}" stroke-width="3"
    fill="none" stroke-linecap="round" opacity="0.82"/>
  <path d="M30,24 Q35,31 28,34" stroke="{C['white']}" stroke-width="3"
    fill="none" stroke-linecap="round" opacity="0.82"/>
  <ellipse cx="18" cy="35" rx="9" ry="4" fill="{C['white']}" opacity="0.7"/>
</g>

<!-- Brand name -->
<text x="{W//2}" y="{H-22}" text-anchor="middle" class="fb"
  font-size="17" fill="{C['white']}">Little Monk Life System</text>

<!-- Workflow -->
<text x="{W//2}" y="{H-8}" text-anchor="middle" class="fo"
  font-size="9.5" fill="{C['gold']}" letter-spacing="1">
  Goal  ➔  System  ➔  Action  ➔  Measure  ➔  Reflect  ➔  Improve
</text>

<!-- ORNAMENTAL HEART — right side -->
{ornamental_heart(W-40, H-24, 26)}

<!-- Bottom saffron border -->
<rect x="0" y="{H-3}" width="{W}" height="3" fill="{C['saffron']}"/>
</svg>''')

    return "\n".join(parts)


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import math  # needed for cherry_blossom
    print("Building LM-001 V5.1...")
    svg = build()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg)
    kb = OUTPUT_FILE.stat().st_size / 1024
    print(f"✓  Saved : {OUTPUT_FILE.resolve()}")
    print(f"   Size  : {kb:.1f} KB")
    print()
    print("Preview:")
    print("  Chrome  → open SVG file → Ctrl+P → Save as PDF → A3 paper")
    print("  Inkscape→ File → Export PNG (300dpi) for high-res image")
    print()
    print("Logo fix:")
    print("  Place your logo at:  assets/logos/little-monk-logo.png")
    print("  OR:                  assets/logos/little-monk-logo.svg")
    print("  Then re-run this script — logo embeds automatically.")
