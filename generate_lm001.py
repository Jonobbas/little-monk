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

    logo_base64 = image_to_base64(LOGO_PATH)

    svg = f'''<svg width="297mm" height="420mm" viewBox="0 0 297 420" xmlns="http://www.w3.org/2000/svg">

  <rect width="297" height="420" fill="#F5F7FA"/>

  <!-- LOGO -->
  <image href="data:image/png;base64,{logo_base64}" x="15" y="10" width="32" height="32"/>

  <!-- HEADER -->
  <text x="55" y="22" font-family="Arial" font-size="8" font-weight="bold" fill="#1E88E5">LM-001 | VERSION 1.0</text>
  <text x="55" y="36" font-family="Arial" font-size="18" font-weight="bold" fill="#263238">30-Day Kaizen Tracker</text>
  <text x="55" y="47" font-family="Arial" font-size="7" fill="#263238">I can improve anything if I follow a system.</text>

  <!-- KAIZEN QUOTE -->
  <rect x="15" y="55" width="267" height="22" rx="5" fill="#F9A825"/>
  <text x="148.5" y="69" text-anchor="middle" font-family="Arial" font-size="8" font-weight="bold" fill="#263238">
    KAIZEN: Small improvements repeated daily create extraordinary progress.
  </text>

  <!-- PROJECT BOX -->
  <rect x="15" y="85" width="267" height="36" rx="6" fill="#FFFFFF" stroke="#ECEFF1"/>
  <text x="22" y="98" font-family="Arial" font-size="8" font-weight="bold" fill="#263238">My Improvement Project</text>
  <line x1="22" y1="108" x2="275" y2="108" stroke="#263238" stroke-width="0.4" stroke-dasharray="2,2"/>
  <line x1="22" y1="117" x2="275" y2="117" stroke="#263238" stroke-width="0.4" stroke-dasharray="2,2"/>

  <!-- CURRENT TARGET ACTUAL -->
  <rect x="15" y="128" width="267" height="26" rx="6" fill="#FFFFFF" stroke="#ECEFF1"/>
  <text x="22" y="143" font-family="Arial" font-size="7" fill="#263238">Current State: ____________</text>
  <text x="112" y="143" font-family="Arial" font-size="7" fill="#263238">Target State: ____________</text>
  <text x="202" y="143" font-family="Arial" font-size="7" fill="#263238">Actual Result: ____________</text>

  <!-- SYSTEM + TRIGGER -->
  <rect x="15" y="161" width="130" height="55" rx="6" fill="#FFFFFF" stroke="#ECEFF1"/>
  <text x="22" y="174" font-family="Arial" font-size="8" font-weight="bold" fill="#263238">My System</text>
  <text x="22" y="187" font-family="Arial" font-size="7" fill="#263238">1. ____________________</text>
  <text x="22" y="199" font-family="Arial" font-size="7" fill="#263238">2. ____________________</text>
  <text x="22" y="211" font-family="Arial" font-size="7" fill="#263238">3. ____________________</text>

  <rect x="152" y="161" width="130" height="55" rx="6" fill="#FFFFFF" stroke="#ECEFF1"/>
  <text x="159" y="174" font-family="Arial" font-size="8" font-weight="bold" fill="#263238">Trigger Box</text>
  <text x="159" y="187" font-family="Arial" font-size="7" fill="#263238">When: ______________</text>
  <text x="159" y="199" font-family="Arial" font-size="7" fill="#263238">Where: _____________</text>
  <text x="159" y="211" font-family="Arial" font-size="7" fill="#263238">After: ______________</text>

  <!-- SCORE GUIDE -->
  <rect x="15" y="223" width="267" height="20" rx="5" fill="#ECEFF1"/>
  <text x="22" y="236" font-family="Arial" font-size="6.5" fill="#263238">
    Daily Score: 0 Not Done | 1 Poor | 2 Below Target | 3 Acceptable | 4 Good | 5 Excellent
  </text>

  <!-- 30 DAY GRID -->
  <text x="15" y="256" font-family="Arial" font-size="9" font-weight="bold" fill="#263238">Daily Progress Score</text>

  <g font-family="Arial" font-size="6.5" fill="#263238">
'''

    start_x = 15
    start_y = 263
    box_w = 50
    box_h = 18
    gap_x = 4
    gap_y = 5

    day = 1
    for row in range(6):
        for col in range(5):
            x = start_x + col * (box_w + gap_x)
            y = start_y + row * (box_h + gap_y)
            svg += f'''
    <rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="3" fill="#FFFFFF" stroke="#ECEFF1"/>
    <text x="{x + 3}" y="{y + 7}">Day {day:02d}</text>
    <text x="{x + 3}" y="{y + 15}" font-size="6">0  1  2  3  4  5</text>
'''
            day += 1

    svg += '''
  </g>

  <!-- SUMMARY -->
  <rect x="15" y="404" width="267" height="1" fill="#ECEFF1"/>

  <text x="15" y="388" font-family="Arial" font-size="7" font-weight="bold" fill="#263238">
    Week Avg: W1 ____  W2 ____  W3 ____  W4 ____   Month Avg ____ / 5
  </text>

  <!-- FOOTER -->
  <text x="148.5" y="416" text-anchor="middle" font-family="Arial" font-size="5" fill="#263238">
    Little Monk Life System | Goal → System → Action → Measure → Reflect → Improve | A FlowCraft Creation
  </text>

</svg>'''

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write(svg)

    print(f"Created: {OUTPUT_FILE.resolve()}")


if __name__ == "__main__":
    generate_lm001()
