import os

LINE = "A refrigerator door that refuses to unlock the snack drawer until you tell it a fresh, verified piece of gossip about someone in your neighborhood."

def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
