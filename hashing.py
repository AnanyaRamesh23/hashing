import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    print("Original password:", password)
    print("Hashed password:", hashed)   

    users[username] = hashed

    print("User registered successfully!\n")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = hash_password(password)

    if username in users:
        if users[username] == hashed:
            print("Login successful!\n")
        else:
            print("Wrong password!\n")
    else:
        print("User not found!\n")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!\n")