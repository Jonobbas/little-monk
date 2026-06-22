from pathlib import Path
import base64
from config import SVG_DIR, create_output_folders

LOGO_PATH = Path("assets/logos/little-monk-logo.png")
OUTPUT_FILE = SVG_DIR / "LM-001-30-Day-Kaizen-Tracker-V3.svg"


def image_to_base64(path):
    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")


def star_row(x, y, size=6, gap=8):
    return "".join(
        f'<text x="{x + i * gap}" y="{y}" font-family="Arial" font-size="{size}" fill="#263238">☆</text>'
        for i in range(5)
    )


def generate_lm001():
    create_output_folders()

    if not LOGO_PATH.exists():
        raise FileNotFoundError(f"Logo not found: {LOGO_PATH.resolve()}")

    logo = image_to_base64(LOGO_PATH)

    svg = f'''<svg width="297mm" height="420mm" viewBox="0 0 297 420" xmlns="http://www.w3.org/2000/svg">

  <!-- Bright Background -->
  <rect width="297" height="420" fill="#EAF8FF"/>
  <rect x="0" y="0" width="297" height="420" fill="#FFF8E1" opacity="0.32"/>

  <!-- Decorative Clouds -->
  <circle cx="245" cy="30" r="18" fill="#FFFFFF" opacity="0.6"/>
  <circle cx="265" cy="32" r="22" fill="#FFFFFF" opacity="0.55"/>
  <circle cx="20" cy="72" r="16" fill="#FFFFFF" opacity="0.55"/>
  <circle cx="39" cy="74" r="20" fill="#FFFFFF" opacity="0.45"/>

  <!-- Header -->
  <image href="data:image/png;base64,{logo}" x="12" y="10" width="45" height="45"/>

  <text x="66" y="19" font-family="Poppins, Arial" font-size="7.5" font-weight="bold" fill="#0D47A1">LM-001 | VERSION 1.0</text>
  <text x="66" y="38" font-family="Poppins, Arial" font-size="21" font-weight="bold" fill="#102A43">30-DAY KAIZEN</text>
  <text x="87" y="51" font-family="Poppins, Arial" font-size="8" letter-spacing="4" font-weight="bold" fill="#263238">TRACKER</text>
  <text x="66" y="63" font-family="Merriweather, Georgia" font-size="7.2" font-style="italic" fill="#0D47A1">✦ If I follow a system, I can improve anything.</text>

  <!-- Kaizen Banner -->
  <rect x="10" y="74" width="277" height="30" rx="8" fill="#FFF3CD" stroke="#F9A825" stroke-width="1.2"/>
  <text x="22" y="94" font-family="Poppins, Arial" font-size="18" font-weight="bold" font-style="italic" fill="#1B1B1B">KAIZEN</text>
  <line x1="105" y1="81" x2="105" y2="98" stroke="#FB8C00" stroke-width="0.7"/>
  <text x="116" y="87" font-family="Poppins, Arial" font-size="7.5" font-weight="bold" fill="#263238">Small improvements</text>
  <text x="116" y="96" font-family="Poppins, Arial" font-size="7.5" font-weight="bold" fill="#263238">repeated daily create extraordinary progress.</text>
  <text x="259" y="94" font-family="Arial" font-size="17" fill="#263238">🖌</text>

  <!-- Improvement Project -->
  <rect x="10" y="113" width="277" height="35" rx="8" fill="#FFFFFF" stroke="#1565C0" stroke-width="0.8"/>
  <text x="18" y="133" font-family="Poppins, Arial" font-size="17" fill="#1565C0">◎</text>
  <text x="36" y="127" font-family="Merriweather, Georgia" font-size="9" font-style="italic" font-weight="bold" fill="#0D47A1">My Improvement Project</text>
  <line x1="36" y1="137" x2="278" y2="137" stroke="#263238" stroke-width="0.35" stroke-dasharray="2,2"/>
  <line x1="36" y1="145" x2="278" y2="145" stroke="#263238" stroke-width="0.35" stroke-dasharray="2,2"/>

  <!-- Current Target Actual -->
  <rect x="10" y="154" width="277" height="28" rx="8" fill="#FFFDF5" stroke="#F9A825" stroke-width="0.8"/>
  <text x="17" y="171" font-family="Arial" font-size="12" fill="#1565C0">⚑</text>
  <text x="31" y="166" font-family="Poppins, Arial" font-size="6.8" font-weight="bold" fill="#0D47A1">Current State</text>
  <line x1="31" y1="176" x2="84" y2="176" stroke="#263238" stroke-width="0.35"/>

  <text x="103" y="171" font-family="Arial" font-size="12" fill="#43A047">◎</text>
  <text x="118" y="166" font-family="Poppins, Arial" font-size="6.8" font-weight="bold" fill="#2E7D32">Target State</text>
  <line x1="118" y1="176" x2="174" y2="176" stroke="#263238" stroke-width="0.35"/>

  <text x="194" y="171" font-family="Arial" font-size="12" fill="#FB8C00">★</text>
  <text x="210" y="166" font-family="Poppins, Arial" font-size="6.8" font-weight="bold" fill="#E65100">Actual Result</text>
  <line x1="210" y1="176" x2="278" y2="176" stroke="#263238" stroke-width="0.35"/>

  <!-- My System -->
  <rect x="10" y="190" width="136" height="50" rx="8" fill="#F1F8E9" stroke="#43A047" stroke-width="0.9"/>
  <circle cx="24" cy="202" r="10" fill="#43A047"/>
  <text x="24" y="207" text-anchor="middle" font-family="Arial" font-size="11" fill="#FFFFFF">⚙</text>
  <text x="40" y="205" font-family="Poppins, Arial" font-size="8.5" font-weight="bold" fill="#2E7D32">MY SYSTEM</text>
  <text x="18" y="219" font-family="Inter, Arial" font-size="6.6" fill="#263238">1. __________________________</text>
  <text x="18" y="229" font-family="Inter, Arial" font-size="6.6" fill="#263238">2. __________________________</text>
  <text x="18" y="239" font-family="Inter, Arial" font-size="6.6" fill="#263238">3. __________________________</text>

  <!-- Trigger -->
  <rect x="152" y="190" width="135" height="50" rx="8" fill="#FFF3E0" stroke="#FB8C00" stroke-width="0.9"/>
  <circle cx="166" cy="202" r="10" fill="#FB8C00"/>
  <text x="166" y="207" text-anchor="middle" font-family="Arial" font-size="12" fill="#FFFFFF">⚡</text>
  <text x="182" y="205" font-family="Poppins, Arial" font-size="8.5" font-weight="bold" fill="#E65100">TRIGGER BOX</text>
  <text x="160" y="219" font-family="Inter, Arial" font-size="6.6" fill="#263238">When: __________________</text>
  <text x="160" y="229" font-family="Inter, Arial" font-size="6.6" fill="#263238">Where: _________________</text>
  <text x="160" y="239" font-family="Inter, Arial" font-size="6.6" fill="#263238">After: __________________</text>

  <!-- Daily Progress -->
  <rect x="10" y="248" width="277" height="17" rx="6" fill="#1565C0"/>
  <text x="18" y="260" font-family="Poppins, Arial" font-size="8.5" font-weight="bold" fill="#FFFFFF">DAILY PROGRESS SCORE</text>
  <text x="102" y="260" font-family="Arial" font-size="8" fill="#FFFFFF">★</text>
  <text x="113" y="260" font-family="Inter, Arial" font-size="6.2" font-weight="bold" fill="#FFFFFF">Shade stars based on your score</text>

  <rect x="10" y="265" width="277" height="84" rx="0" fill="#FFFFFF" stroke="#1565C0" stroke-width="0.6"/>
  <g font-family="Inter, Arial" fill="#0D47A1">
'''

    start_x = 13
    start_y = 277
    cell_w = 53.5
    cell_h = 13
    day = 1

    for row in range(6):
        for col in range(5):
            x = start_x + col * cell_w
            y = start_y + row * cell_h
            svg += f'''
    <line x1="{x - 3}" y1="{y - 10}" x2="{x - 3}" y2="{y + 2}" stroke="#BBDEFB" stroke-width="0.4"/>
    <text x="{x}" y="{y - 2}" font-size="5.8" font-weight="bold">Day {day:02d}</text>
    {star_row(x + 22, y - 2, size=6, gap=6)}
'''
            day += 1

    svg += '''
  </g>

  <!-- Weekly Monthly Average -->
  <rect x="10" y="356" width="277" height="35" rx="8" fill="#FFFFFF" stroke="#1565C0" stroke-width="0.8"/>
  <rect x="10" y="356" width="277" height="10" rx="8" fill="#E3F2FD"/>
  <text x="148.5" y="364" text-anchor="middle" font-family="Poppins, Arial" font-size="7.3" font-weight="bold" fill="#0D47A1">★ WEEKLY &amp; MONTHLY AVERAGE  / 5</text>

  <g font-family="Poppins, Arial" font-size="6.2" font-weight="bold">
    <text x="24" y="375" fill="#0D47A1">WEEK 1</text>
    <rect x="18" y="379" width="38" height="8" rx="2" fill="#FFFDF5" stroke="#1565C0" stroke-width="0.5"/>

    <text x="80" y="375" fill="#2E7D32">WEEK 2</text>
    <rect x="74" y="379" width="38" height="8" rx="2" fill="#FFFDF5" stroke="#43A047" stroke-width="0.5"/>

    <text x="136" y="375" fill="#E65100">WEEK 3</text>
    <rect x="130" y="379" width="38" height="8" rx="2" fill="#FFFDF5" stroke="#FB8C00" stroke-width="0.5"/>

    <text x="192" y="375" fill="#6A1B9A">WEEK 4</text>
    <rect x="186" y="379" width="38" height="8" rx="2" fill="#FFFDF5" stroke="#8E24AA" stroke-width="0.5"/>

    <text x="247" y="375" fill="#0D47A1">MONTH</text>
    <rect x="242" y="379" width="38" height="8" rx="2" fill="#FFFDF5" stroke="#1565C0" stroke-width="0.5"/>
  </g>

  <!-- Reflect Improve -->
  <rect x="10" y="397" width="277" height="18" rx="7" fill="#F3E5F5" stroke="#8E24AA" stroke-width="0.7"/>
  <text x="18" y="408" font-family="Poppins, Arial" font-size="7" font-weight="bold" fill="#6A1B9A">REFLECT &amp; IMPROVE</text>
  <text x="75" y="408" font-family="Inter, Arial" font-size="5.8" fill="#263238">Helped: __________</text>
  <text x="139" y="408" font-family="Inter, Arial" font-size="5.8" fill="#263238">Got in the way: __________</text>
  <text x="222" y="408" font-family="Inter, Arial" font-size="5.8" fill="#263238">Next: ________</text>

  <!-- Footer -->
  <rect x="0" y="417" width="297" height="3" fill="#0D47A1"/>
  <text x="148.5" y="415" text-anchor="middle" font-family="Inter, Arial" font-size="5" font-weight="bold" fill="#263238">
    Little Monk Life System | Goal → System → Action → Measure → Reflect → Improve
  </text>

</svg>'''

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(svg)

    print(f"Created: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    generate_lm001()
