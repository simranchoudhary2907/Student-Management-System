from database import load_users, save_users
from utils import hash_password

def register():
    print("\n===== Register =====")

    username = input("Enter Username: ")
    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")

    if password != confirm_password:
        print("\n❌ Passwords do not match.")
        return
    
    users = load_users()

    for user in users:
        if user["username"] == username:
            print("\n❌ Username already exists.")
            return

    hashed_password = hash_password(password)

    new_user = {
        "username": username,
        "password": hashed_password,
        "role": "student"
    }

    users.append(new_user)
    save_users(users)

    print("\n✅ Registration Successful!")
    print("---------------------------")
    # print("Username:", username)
    print(f"Welcome, {username}!")
    # print("Hashed Password:", hashed_password)
    

def login():
    print("\n===== Login =====")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    users = load_users()
    hashed_password = hash_password(password)

    found = False

    for user in users:
        if user["username"] == username:

            found = True

            if user["password"] == hashed_password:
                print("\n✅ Login Successful!")
            else:
                print("\n❌ Incorrect Password.")
    if not found:
        print("\n Oops! User not found")

            


def logout():
    print("\nLogged out successfully.")