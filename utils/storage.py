import json
import os

FILE_PATH = "data/projects.json"

def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []