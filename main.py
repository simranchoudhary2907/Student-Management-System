from auth import register, login, logout

print("=" * 40)
print(" Student Management System ")
print("=" * 40)

print("1. Register")
print("2. Login")
print("3. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    register()

elif choice == "2":
    login()

elif choice == "3":
    print("Thank you!")

else:
    print("Invalid Choice")