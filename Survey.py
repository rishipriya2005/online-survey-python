# Online Survey Application

import json

# Survey Questions
questions = [
    {
        "question": "1. Which programming language do you like most?",
        "options": ["Python", "Java", "C++", "JavaScript"]
    },
    {
        "question": "2. How did you learn programming?",
        "options": ["College", "YouTube", "Online Courses", "Self Practice"]
    },
    {
        "question": "3. What is your goal?",
        "options": ["Job", "Freelancing", "Startup", "Higher Studies"]
    }
]

responses = []

print("===== ONLINE SURVEY =====\n")

for q in questions:
    print(q["question"])
    
    for i, option in enumerate(q["options"], start=1):
        print(f"{i}. {option}")
    
    while True:
        try:
            choice = int(input("Enter option number: "))
            if 1 <= choice <= len(q["options"]):
                responses.append(q["options"][choice - 1])
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

    print()

# Save responses to file
with open("survey_data.json", "w") as f:
    json.dump(responses, f)

print("✅ Thank you for completing the survey!")