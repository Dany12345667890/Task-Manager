import json
import os

FILENAME = "tasks.json"


def save_data(tasks):
    """Save the list of tasks to a JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved successfully!")


def load_data():
    """Load tasks from the JSON file. Returns an empty list if it does not exist."""
    if not os.path.exists(FILENAME):
        return []

    try:
        with open(FILENAME, "r") as file:
            tasks = json.load(file)
        return tasks if isinstance(tasks, list) else []
    except (json.JSONDecodeError, IOError):
        print("Warning: Could not load tasks.json. Starting with an empty list.")
        return []
