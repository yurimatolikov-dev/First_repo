import json
import os

FILE_PATH = 'data.json'

def load_data():
    if not os.path.exists(FILE_PATH):
        return {}

    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_data(data):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)