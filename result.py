# Show Survey Results

import json

try:
    with open("survey_data.json", "r") as f:
        data = json.load(f)

    print("\n===== SURVEY RESULTS =====")
    for i, answer in enumerate(data, start=1):
        print(f"Q{i}: {answer}")

except FileNotFoundError:
    print("No survey data found.")