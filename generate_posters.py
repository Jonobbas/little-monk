import csv
from config import POSTER_CATALOG_FILE, SVG_DIR, create_output_folders


def load_posters():
    posters = []

    with open(POSTER_CATALOG_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            posters.append(row)

    return posters


def create_simple_svg(poster):
    poster_id = poster["poster_id"]
    title = poster["title"]
    category = poster["category"]
    audience = poster["audience"]
    size = poster["size"]
    poster_type = poster["poster_type"]

    if size == "A2":
        width_mm = 420
        height_mm = 594
    else:
        width_mm = 297
        height_mm = 420

    svg = f'''<svg width="{width_mm}mm" height="{height_mm}mm" viewBox="0 0 {width_mm} {height_mm}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{width_mm}" height="{height_mm}" fill="#F5F7FA"/>

  <rect x="15" y="15" width="{width_mm - 30}" height="45" rx="8" fill="#1E88E5"/>
  <circle cx="38" cy="37" r="13" fill="#F9A825"/>
  <text x="38" y="42" text-anchor="middle" font-family="Arial" font-size="10" font-weight="bold" fill="#263238">LM</text>

  <text x="60" y="34" font-family="Arial" font-size="16" font-weight="bold" fill="#FFFFFF">{title}</text>
  <text x="60" y="49" font-family="Arial" font-size="6" fill="#FFFFFF">{poster_id} | {category} | {audience}</text>

  <rect x="15" y="75" width="{width_mm - 30}" height="{height_mm - 150}" rx="8" fill="#FFFFFF" stroke="#ECEFF1" stroke-width="1"/>

  <text x="{width_mm / 2}" y="{height_mm / 2 - 20}" text-anchor="middle" font-family="Arial" font-size="14" font-weight="bold" fill="#1E88E5">
    {poster_type} Poster Area
  </text>

  <text x="{width_mm / 2}" y="{height_mm / 2}" text-anchor="middle" font-family="Arial" font-size="8" fill="#263238">
    Tracker layout will be generated here
  </text>

  <rect x="15" y="{height_mm - 55}" width="{width_mm - 30}" height="25" rx="6" fill="#F9A825"/>
  <text x="{width_mm / 2}" y="{height_mm - 39}" text-anchor="middle" font-family="Arial" font-size="7" font-weight="bold" fill="#263238">
    Kaizen Wisdom: Small daily improvements create extraordinary progress.
  </text>

  <text x="{width_mm / 2}" y="{height_mm - 12}" text-anchor="middle" font-family="Arial" font-size="5" fill="#263238">
    Little Monk Life System | A FlowCraft Creation
  </text>
</svg>'''

    return svg


def safe_filename(text):
    return (
        text.replace(" ", "-")
        .replace("/", "-")
        .replace("&", "and")
        .replace(":", "")
        .replace(",", "")
    )


def generate_svg_files(posters):
    create_output_folders()

    for poster in posters:
        svg_content = create_simple_svg(poster)

        filename = f"{poster['poster_id']}-{safe_filename(poster['title'])}.svg"
        output_path = SVG_DIR / filename

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(svg_content)

        print(f"Created: {output_path}")


def main():
    posters = load_posters()

    print("\nLittle Monk Poster Factory")
    print("-" * 40)
    print(f"Total Posters Found : {len(posters)}")
    print("Generating SVG files...\n")

    generate_svg_files(posters)

    print("\nBatch generation completed.")


if __name__ == "__main__":
    main()
import os

print("\nFiles in SVG folder:")
print("-" * 40)

for file in os.listdir(SVG_DIR):
    print(file)
print("\nACTUAL SVG DIRECTORY:")
print(SVG_DIR.resolve())

print("\nDoes folder exist?")
print(SVG_DIR.exists())

print("\nNumber of files inside:")
print(len(list(SVG_DIR.glob("*.svg"))))

print("\nOpening folder path:")
print(str(SVG_DIR.resolve()))
