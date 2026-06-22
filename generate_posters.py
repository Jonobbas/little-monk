import csv
from config import POSTER_CATALOG_FILE


def load_posters():
    posters = []

    with open(POSTER_CATALOG_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            posters.append(row)

    return posters


def main():
    posters = load_posters()

    print("\nLittle Monk Poster Factory")
    print("-" * 40)

    print(f"Total Posters Found : {len(posters)}")
    print()

    for poster in posters:
        print(
            f"{poster['poster_id']} | "
            f"{poster['title']} | "
            f"{poster['size']}"
        )


if __name__ == "__main__":
    main()
