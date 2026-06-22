from pathlib import Path

# ============================================================
# LITTLE MONK POSTER FACTORY - CONFIGURATION FILE
# ============================================================

PROJECT_NAME = "Little Monk Poster Factory"

# Main output location on your desktop
OUTPUT_ROOT = Path("output")

# Output folders
SVG_DIR = OUTPUT_ROOT / "svg"
PDF_DIR = OUTPUT_ROOT / "pdf"
PNG_DIR = OUTPUT_ROOT / "png"
PREVIEW_DIR = OUTPUT_ROOT / "preview"
DOCS_DIR = OUTPUT_ROOT / "docs"
LOGS_DIR = OUTPUT_ROOT / "logs"

# Data folders inside repository
DATA_DIR = Path("data")
POSTER_CATALOG_FILE = DATA_DIR / "poster_list.csv"

# Brand colors
BRAND_COLORS = {
    "primary_blue": "#1E88E5",
    "gold": "#F9A825",
    "calm_background": "#F5F7FA",
    "dark_text": "#263238",
    "soft_grey": "#ECEFF1",
    "success_green": "#43A047",
    "warning_orange": "#FB8C00",
}

# Poster sizes in millimeters
POSTER_SIZES = {
    "A3": {
        "width_mm": 297,
        "height_mm": 420,
    },
    "A2": {
        "width_mm": 420,
        "height_mm": 594,
    },
}

# Font system
FONTS = {
    "heading": "Poppins",
    "body": "Inter",
    "quote": "Merriweather",
    "fallback": "Arial",
}


def create_output_folders():
    """
    Creates all required output folders automatically.
    """
    folders = [
        OUTPUT_ROOT,
        SVG_DIR,
        PDF_DIR,
        PNG_DIR,
        PREVIEW_DIR,
        DOCS_DIR,
        LOGS_DIR,
    ]

    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)

    print("Output folders created successfully.")
    print(f"Output Root: {OUTPUT_ROOT}")
def verify_paths():
    print("\nConfiguration Verification")
    print("-" * 40)

    print(f"Project : {PROJECT_NAME}")
    print(f"Catalog : {POSTER_CATALOG_FILE}")
    print(f"Output  : {OUTPUT_ROOT}")

    if POSTER_CATALOG_FILE.exists():
        print("Poster catalog found")
    else:
        print("Poster catalog NOT found")

if __name__ == "__main__":
    create_output_folders()
    verify_paths()
