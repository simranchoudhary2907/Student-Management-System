import json
import os

USERS_FILE = "data/users.json"


def load_users():
    """Load all users from users.json"""

    if not os.path.exists(USERS_FILE):
        return []

    with open(USERS_FILE, "r") as file:
        users = json.load(file)

    return users



def save_users(users):
    """Save all users to users.json"""

    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)