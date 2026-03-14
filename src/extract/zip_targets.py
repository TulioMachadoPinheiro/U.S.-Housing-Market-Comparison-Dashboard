ZIP_TARGETS = {
    "Massachusetts": ["02481", "01701", "02148"],
    "Texas": ["77584", "75035", "77084"],
    "Florida": ["33157", "34711", "33012"],
    "California": ["90016", "94134", "94112"],
    "New York": ["10025", "11207", "11226"],
    "Colorado": ["80219", "80013"],
    "Illinois": ["60629", "60632"],
    "Georgia": ["30044", "30349"]
}

if __name__ == "__main__":
    total_zips = sum(len(zips) for zips in ZIP_TARGETS.values())

    print("States:", len(ZIP_TARGETS))
    print("Total ZIP codes:", total_zips)
    print(ZIP_TARGETS)