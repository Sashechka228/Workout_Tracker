import requests, os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

def get_workout_input():
    return {
        "exercise": input("Exercise: ").strip(),
        "sets": int(input("Sets (default 3): ") or 3),
        "reps": int(input("Reps (default 10): ") or 10),
        "weight": int(input("Weight (default 0): ") or 0),
        "notes": input("Notes: ").strip() or "-"
    }

def send_to_sheet(workout):
    data = {
        "log": {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            **workout
        }
    }

    return requests.post(SHEETY_ENDPOINT, json=data, headers=headers)

workout = get_workout_input()
response = send_to_sheet(workout)

print(response.json())

if response.status_code in (200, 201):
    print("Successfully added!")
else:
    print("Error:", response.text)

