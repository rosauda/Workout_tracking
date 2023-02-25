import os
import requests

# ---------------------------- VARIABLES ------------------------------- #

GENDER = "male"
WEIGHT_KG = 88
HEIGHT_CM = 180
AGE = 32

# Environment variables
APP_ID = os.environ["api_id"]
API_KEY = os.environ["api_key"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# ---------------------------- GETTING EXERCISE DATA USING API ------------------------------- #

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
