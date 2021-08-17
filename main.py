import requests
import datetime as dt
import os

NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID")
NUTRITIONIX_KEY = os.environ.get("NUTRITIONIX_KEY")
NUTRITIONIX_LINK = os.environ.get("NUTRITIONIX_LINK")
SPREADSHEET_LINK = os.environ.get("SPREADSHEET_LINK")
SPREADSHEET_ID = os.environ.get("SPREADSHEET_ID")
SPREADSHEET_KEY = os.environ.get("SPREADSHEET_KEY")
SPREADSHEET_HEADERS = (SPREADSHEET_ID, SPREADSHEET_KEY)
NUTRITIONIX_HEADERS = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY
}

GENDER = "male"
WEIGHT = 90
HEIGHT = 175
AGE = 18

get_data = input("Tell me what exercises you did: ")

EXERCISE_ENDPOINT = {
    "query": get_data,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_LINK, json=EXERCISE_ENDPOINT, headers=NUTRITIONIX_HEADERS)
gym_data = response.json()

for gym in gym_data["exercises"]:
    datetime = dt.datetime.now()
    date = datetime.strftime("%Y-%m-%d")
    time = datetime.strftime("%H:%M:%S")
    exercise = gym["user_input"]
    duration = gym["duration_min"]
    calories = gym["nf_calories"]

    SPREADSHEET_ENDPOINT = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories
        }
    }


    response = requests.post(url=SPREADSHEET_LINK, json=SPREADSHEET_ENDPOINT, auth=SPREADSHEET_HEADERS)
    print(response.text)



response = requests.get(url=SPREADSHEET_LINK, auth=SPREADSHEET_HEADERS)
data = response.json()
print(data)