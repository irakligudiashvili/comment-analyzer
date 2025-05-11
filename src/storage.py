import json
import os

DATA_FILE = "menu_data.json"

def load_menu():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return None

def save_menu(menu):
    with open(DATA_FILE, "w") as f:
        json.dump(menu, f, indent=2)