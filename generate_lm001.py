from pathlib import Path
import base64
from config import SVG_DIR, create_output_folders

LOGO_PATH = Path("assets/logos/little-monk-logo.png")
OUTPUT_FILE = SVG_DIR / "LM-001-30-Day-Kaizen-Tracker-V2.svg"


def image_to_base64(path):
    with open(path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")


def generate_lm001():
    create_output_folders()

    if not LOGO_PATH.exists():
        raise FileNotFoundError(f"Logo not found at: {LOGO_PATH.resolve()}")

    logo_base64 = image_to_base64(LOGO_PATH)

    svg = f'''<svg width="297mm" height="420mm" viewBox="0 0 297 420" xmlns="http://www.w3.org/2000/svg">

  <rect width="297" height="420" fill="#F5F7FA"/>

  <!-- Header Background -->
  <rect x="10" y="8" width="277" height="48" rx="8" fill="#E3F2FD" stroke="#1E88E5" stroke-width="0.6"/>

  <!-- Logo -->
  <image href="data:image/png;base64,{logo_base64}" x="16" y="13" width="38" height="38"/>

  <!-- Header Text -->
  <text x="62" y="23" font-family="Poppins, Arial" font-size="7" font-weight="bold" fill="#1E88E5">LM-001 | VERSION 1.0</text>
  <text x="62" y="38" font-family="Poppins, Arial" font-size="17" font-weight="bold" fill="#263238">30-Day Kaizen Tracker</text>
  <text x="62" y="49" font-family="Inter, Arial" font-size="6.5" fill="#263238">I can improve anything if I follow a system.</text>

  <!-- Kaizen Quote -->
  <rect x="10" y="62" width="277" height="26" rx="7" fill="#F9A825"/>
  <text x="148.5" y="73" text-anchor="middle" font-family="Poppins, Arial" font-size="11" font-weight="bold" fill="#263238">KAIZEN</text>
  <text x="148.5" y="83" text-anchor="middle" font-family="Inter, Arial" font-size="6.3" font-weight="bold" fill="#263238">Small improvements repeated daily create extraordinary progress.</text>

  <!-- Improvement Project -->
  <rect x="10" y="94" width="277" height="34" rx="7" fill="#FFFFFF" stroke="#BBDEFB" stroke-width="0.8"/>
  <text x="17" y="107" font-family="Poppins, Arial" font-size="8" font-weight="bold" fill="#1E88E5">My Improvement Project</text>
  <line x1="17" y1="117" x2="280" y2="117" stroke="#263238" stroke-width="0.35" stroke-dasharray="2,2"/>
  <line x1="17" y1="125" x2="280" y2="125" stroke="#263238" stroke-width="0.35" stroke-dasharray="2,2"/>

  <!-- Current Target Actual -->
  <rect x="10" y="134" width="277" height="28" rx="7" fill="#FFF8E1" stroke="#F9A825" stroke-width="0.8"/>
  <text x="17" y="148" font-family="Inter, Arial" font-size="6.5" font-weight="bold" fill="#263238">Current State:</text>
  <line x1="59" y1="148" x2="100" y2="148" stroke="#263238" stroke-width="0.35"/>
  <text x="107" y="148" font-family="Inter, Arial" font-size="6.5" font-weight="bold" fill="#263238">Target State:</text>
  <line x1="148" y1="148" x2="190" y2="148" stroke="#263238" stroke-width="0.35"/>
  <text x="197" y="148" font-family="Inter, Arial" font-size="6.5" font-weight="bold" fill="#263238">Actual Result:</text>
  <line x1="241" y1="148" x2="280" y2="148" stroke="#263238" stroke-width="0.35"/>

  <!-- My System -->
  <rect x="10" y="168" width="136" height="52" rx="7" fill="#FFFFFF" stroke="#C8E6C9" stroke-width="0.8"/>
  <rect x="10" y="168" width="136" height="13" rx="7" fill="#43A047"/>
  <text x="17" y="177" font-family="Poppins, Arial" font-size="7.5" font-weight="bold" fill="#FFFFFF">My System</text>
  <text x="17" y="191" font-family="Inter, Arial" font-size="6.7" fill="#263238">1. __________________________</text>
  <text x="17" y="204" font-family="Inter, Arial" font-size="6.7" fill="#263238">2. __________________________</text>
  <text x="17" y="217" font-family="Inter, Arial" font-size="6.7" fill="#263238">3. __________________________</text>

  <!-- Trigger Box -->
  <rect x="152" y="168" width="135" height="52" rx="7" fill="#FFFFFF" stroke="#FFE0B2" stroke-width="0.8"/>
  <rect x="152" y="168" width="135" height="13" rx="7" fill="#FB8C00"/>
  <text x="159" y="177" font-family="Poppins, Arial" font-size="7.5" font-weight="bold" fill="#FFFFFF">Trigger Box</text>
  <text x="159" y="191" font-family="Inter, Arial" font-size="6.7" fill="#263238">When: __________________</text>
  <text x="159" y="204" font-family="Inter, Arial" font-size="6.7" fill="#263238">Where: _________________</text>
  <text x="159" y="217" font-family="Inter, Arial" font-size="6.7" fill="#263238">After: __________________</text>

  <!-- Score Guide -->
  <rect x="10" y="226" width="277" height="20" rx="6" fill="#E8F5E9" stroke="#43A047" stroke-width="0.7"/>
  <text x="17" y="239" font-family="Inter, Arial" font-size="6.2" font-weight="bold" fill="#263238">
    Daily Score: 0 Not Done | 1 Poor | 2 Below Target | 3 Acceptable | 4 Good | 5 Excellent
  </text>

  <!-- Daily Progress Header -->
  <text x="10" y="258" font-family="Poppins, Arial" font-size="8.5" font-weight="bold" fill="#263238">Daily Progress Score</text>

  <g font-family="Inter, Arial" font-size="6.3" fill="#263238">
'''

    start_x = 10
    start_y = 264
    box_w = 52
    box_h = 18
    gap_x = 4
    gap_y = 4

    day = 1
    for row in range(6):
        for col in range(5):
            x = start_x + col * (box_w + gap_x)
            y = start_y + row * (box_h + gap_y)

            svg += f'''
    <rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="3" fill="#FFFFFF" stroke="#BBDEFB" stroke-width="0.6"/>
    <text x="{x + 3}" y="{y + 7}" font-weight="bold">Day {day:02d}</text>
    <text x="{x + 3}" y="{y + 15}" font-size="6.2">0   1   2   3   4   5</text>
'''
            day += 1

    svg += '''
  </g>

  <!-- Monthly Summary -->
  <rect x="10" y="397" width="277" height="12" rx="4" fill="#ECEFF1"/>
  <text x="17" y="405" font-family="Inter, Arial" font-size="6.2" font-weight="bold" fill="#263238">
    Week Avg: W1 _____  W2 _____  W3 _____  W4 _____   Month Avg _____ / 5
  </text>

  <!-- Footer -->
  <text x="148.5" y="417" text-anchor="middle" font-family="Inter, Arial" font-size="5" fill="#263238">
    Little Monk Life System | Goal → System → Action → Measure → Reflect → Improve
  </text>

</svg>'''

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(svg)

    print(f"Created: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    generate_lm001()
