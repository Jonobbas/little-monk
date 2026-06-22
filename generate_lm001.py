from pathlib import Path
import base64
from config import SVG_DIR, create_output_folders

LOGO_PATH = Path("assets/logos/little-monk-logo.png")
OUTPUT_FILE = SVG_DIR / "LM-001-30-Day-Kaizen-Tracker-V4.svg"


def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def stars(x, y):
    return "".join(
        f'<text x="{x+i*7}" y="{y}" font-size="7" fill="#263238">☆</text>'
        for i in range(5)
    )


def generate_lm001():
    create_output_folders()

    if not LOGO_PATH.exists():
        raise FileNotFoundError(f"Logo not found: {LOGO_PATH.resolve()}")

    logo = image_to_base64(LOGO_PATH)

    svg = f'''<svg width="297mm" height="420mm" viewBox="0 0 297 420" xmlns="http://www.w3.org/2000/svg">

<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#BFEFFF"/>
    <stop offset="55%" stop-color="#FFF8E1"/>
    <stop offset="100%" stop-color="#E3F2FD"/>
  </linearGradient>

  <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#FFF3CD"/>
    <stop offset="50%" stop-color="#FFD966"/>
    <stop offset="100%" stop-color="#FFF3CD"/>
  </linearGradient>

  <filter id="shadow">
    <feDropShadow dx="0.8" dy="1.2" stdDeviation="1" flood-color="#000000" flood-opacity="0.25"/>
  </filter>

  <style>
    .title {{ font-family: Impact, Anton, Poppins, Arial; font-weight:900; letter-spacing:1px; }}
    .brush {{ font-family: Brush Script MT, Comic Sans MS, Georgia, serif; font-style:italic; font-weight:bold; }}
    .head {{ font-family:Poppins, Arial; font-weight:bold; }}
    .body {{ font-family:Inter, Arial; }}
    .line {{ stroke:#263238; stroke-width:0.35; stroke-dasharray:2,2; }}
  </style>
</defs>

<!-- Background -->
<rect width="297" height="420" fill="url(#sky)"/>

<!-- Clouds -->
<g opacity="0.75" fill="#FFFFFF">
  <circle cx="230" cy="28" r="13"/><circle cx="246" cy="25" r="17"/><circle cx="264" cy="31" r="14"/>
  <circle cx="20" cy="65" r="13"/><circle cx="36" cy="66" r="18"/><circle cx="54" cy="70" r="12"/>
</g>

<!-- Birds -->
<text x="250" y="45" font-size="8" fill="#0D47A1">⌒⌒</text>
<text x="268" y="34" font-size="7" fill="#0D47A1">⌒</text>

<!-- Logo -->
<image href="data:image/png;base64,{logo}" x="12" y="9" width="48" height="48"/>

<!-- Top Title -->
<text x="70" y="20" class="head" font-size="7.5" fill="#0D47A1">LM-001 | VERSION 1.0</text>
<text x="70" y="42" class="title" font-size="24" fill="#102A43" filter="url(#shadow)">30-DAY</text>
<text x="158" y="42" class="brush" font-size="28" fill="#1565C0" filter="url(#shadow)">KAIZEN</text>
<text x="104" y="58" class="head" font-size="8.5" letter-spacing="5" fill="#263238">TRACKER</text>
<text x="72" y="70" class="brush" font-size="8.5" fill="#0D47A1">✦ If I follow a system, I can improve anything.</text>

<!-- Small Torii / Zen symbol -->
<text x="257" y="70" font-size="21" fill="#BF360C">⛩</text>

<!-- Kaizen Gold Banner -->
<rect x="10" y="80" width="277" height="34" rx="8" fill="url(#gold)" stroke="#F9A825" stroke-width="1.2" filter="url(#shadow)"/>
<text x="22" y="103" class="brush" font-size="22" fill="#111111">KAIZEN</text>
<line x1="108" y1="87" x2="108" y2="107" stroke="#FB8C00" stroke-width="0.8"/>
<text x="118" y="94" class="head" font-size="7.5" fill="#263238">Small improvements repeated daily</text>
<text x="118" y="104" class="head" font-size="7.5" fill="#263238">create extraordinary progress.</text>
<text x="260" y="102" font-size="16">🖌</text>

<!-- Improvement Project -->
<rect x="10" y="122" width="277" height="34" rx="8" fill="#FFFFFF" stroke="#1565C0" stroke-width="0.8"/>
<text x="18" y="144" font-size="18" fill="#1565C0">◎</text>
<text x="38" y="136" class="brush" font-size="9.5" fill="#0D47A1">My Improvement Project</text>
<line x1="38" y1="146" x2="278" y2="146" class="line"/>
<line x1="38" y1="153" x2="278" y2="153" class="line"/>

<!-- State Row -->
<rect x="10" y="163" width="277" height="28" rx="8" fill="#FFFDF5" stroke="#F9A825" stroke-width="0.8"/>
<text x="19" y="180" font-size="12" fill="#1565C0">⚑</text>
<text x="34" y="176" class="head" font-size="6.7" fill="#0D47A1">Current State</text>
<line x1="34" y1="185" x2="86" y2="185" stroke="#263238" stroke-width="0.35"/>
<text x="103" y="180" font-size="12" fill="#43A047">◎</text>
<text x="119" y="176" class="head" font-size="6.7" fill="#2E7D32">Target State</text>
<line x1="119" y1="185" x2="174" y2="185" stroke="#263238" stroke-width="0.35"/>
<text x="193" y="180" font-size="12" fill="#FB8C00">★</text>
<text x="210" y="176" class="head" font-size="6.7" fill="#E65100">Actual Result</text>
<line x1="210" y1="185" x2="278" y2="185" stroke="#263238" stroke-width="0.35"/>

<!-- System + Trigger -->
<rect x="10" y="199" width="136" height="49" rx="8" fill="#F1F8E9" stroke="#43A047" stroke-width="0.9"/>
<circle cx="24" cy="211" r="10" fill="#43A047"/>
<text x="24" y="216" text-anchor="middle" font-size="12" fill="#FFFFFF">⚙</text>
<text x="42" y="214" class="head" font-size="8.5" fill="#2E7D32">MY SYSTEM</text>
<text x="18" y="228" class="body" font-size="6.6">1. __________________________</text>
<text x="18" y="238" class="body" font-size="6.6">2. __________________________</text>
<text x="18" y="247" class="body" font-size="6.6">3. __________________________</text>

<rect x="152" y="199" width="135" height="49" rx="8" fill="#FFF3E0" stroke="#FB8C00" stroke-width="0.9"/>
<circle cx="166" cy="211" r="10" fill="#FB8C00"/>
<text x="166" y="216" text-anchor="middle" font-size="12" fill="#FFFFFF">⚡</text>
<text x="183" y="214" class="head" font-size="8.5" fill="#E65100">TRIGGER BOX</text>
<text x="160" y="228" class="body" font-size="6.6">When: __________________</text>
<text x="160" y="238" class="body" font-size="6.6">Where: _________________</text>
<text x="160" y="247" class="body" font-size="6.6">After: __________________</text>

<!-- Daily Progress -->
<rect x="10" y="255" width="277" height="15" rx="6" fill="#1565C0"/>
<text x="18" y="266" class="head" font-size="8" fill="#FFFFFF">DAILY PROGRESS SCORE</text>
<text x="112" y="266" font-size="8" fill="#FFFFFF">★</text>
<text x="124" y="266" class="body" font-size="6" font-weight="bold" fill="#FFFFFF">Shade stars based on your daily score</text>

<rect x="10" y="270" width="277" height="80" fill="#FFFFFF" stroke="#1565C0" stroke-width="0.6"/>

<g class="body" fill="#0D47A1">
'''

    start_x, start_y = 14, 282
    cell_w, cell_h = 53, 12.5
    day = 1
    for row in range(6):
        for col in range(5):
            x = start_x + col * cell_w
            y = start_y + row * cell_h
            svg += f'''
  <text x="{x}" y="{y}" font-size="5.8" font-weight="bold">Day {day:02d}</text>
  {stars(x+23, y)}
'''
            day += 1

    svg += '''
</g>

<!-- Weekly Average -->
<rect x="10" y="356" width="277" height="35" rx="8" fill="#FFFFFF" stroke="#1565C0" stroke-width="0.8"/>
<rect x="10" y="356" width="277" height="10" rx="8" fill="#E3F2FD"/>
<text x="148.5" y="364" text-anchor="middle" class="head" font-size="7.2" fill="#0D47A1">★ WEEKLY & MONTHLY AVERAGE  / 5</text>

<g class="head" font-size="6.1">
  <text x="24" y="375" fill="#0D47A1">WEEK 1</text><rect x="18" y="379" width="38" height="8" rx="2" fill="#FFFDF5" stroke="#1565C0" stroke-width="0.5"/>
  <text x="80" y="375" fill="#2E7D32">WEEK 2</text><rect x="74" y="379" width="38" height="8" rx="2" fill="#FFFDF5" stroke="#43A047" stroke-width="0.5"/>
  <text x="136" y="375" fill="#E65100">WEEK 3</text><rect x="130" y="379" width="38" height="8" rx="2" fill="#FFFDF5" stroke="#FB8C00" stroke-width="0.5"/>
  <text x="192" y="375" fill="#6A1B9A">WEEK 4</text><rect x="186" y="379" width="38" height="8" rx="2" fill="#FFFDF5" stroke="#8E24AA" stroke-width="0.5"/>
  <text x="247" y="375" fill="#0D47A1">MONTH</text><rect x="242" y="379" width="38" height="8" rx="2" fill="#FFFDF5" stroke="#1565C0" stroke-width="0.5"/>
</g>

<!-- Reflection -->
<rect x="10" y="396" width="277" height="18" rx="7" fill="#F3E5F5" stroke="#8E24AA" stroke-width="0.7"/>
<text x="17" y="407" class="head" font-size="6.8" fill="#6A1B9A">REFLECT & IMPROVE</text>
<text x="73" y="407" class="body" font-size="5.5">Helped: __________</text>
<text x="137" y="407" class="body" font-size="5.5">Got in the way: __________</text>
<text x="224" y="407" class="body" font-size="5.5">Next: ______</text>

<!-- Bottom Zen Strip -->
<path d="M0 418 C45 390, 92 405, 140 390 C190 375, 240 402, 297 382 L297 420 L0 420 Z" fill="#0D47A1"/>
<text x="28" y="414" font-size="13" fill="#102A43">🧘</text>
<text x="148.5" y="414" text-anchor="middle" class="brush" font-size="8.5" fill="#FFFFFF">Little Monk Life System</text>
<text x="148.5" y="419" text-anchor="middle" class="body" font-size="4.8" fill="#FFFFFF">Goal → System → Action → Measure → Reflect → Improve</text>
<text x="270" y="414" font-size="11" fill="#FFD966">♡</text>

</svg>'''

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"Created: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    generate_lm001()
