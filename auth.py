def register():
    print("\n===== Register =====")

    username = input("Enter Username: ")
    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")

    if password != confirm_password:
        print("Passwords do not match.")
        return
    
    print("\nRegistration Details")
    print("----------------------")
    print("Username:", username)
    print("Password:", password)
    print("Confirm Password:", confirm_password)



def login():
    print("\n===== Login =====")


def logout():
    print("\nLogged out successfully.")