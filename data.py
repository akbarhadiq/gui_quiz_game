import requests
import html

QUESTION_AMOUNT = 10
QUESTION_TYPE = "boolean"

API_params = {
    "amount": QUESTION_AMOUNT,
    "type": QUESTION_TYPE
}


def get_question():
    response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean", params=API_params)
    response.raise_for_status()  # -->if something happened to api getter
    data = response.json()["results"]
    question_data = data
    return question_data



