import pyperclip
import os

FILE_NAME = "passwords.txt"
def save_password(website, username, password):
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    with open(FILE_NAME, 'a') as file:
        file.write(f"{website}:{password}\n")

def get_password(website):
    website = input("Enter the website: ")
    if not os.path.exists(FILE_NAME):
        print("No passwords saved yet.")
        return

    with open(FILE_NAME, 'r') as file:
        for line in file:
            saved_website, saved_password = line.strip().split(':')
            if saved_website == website:
                pyperclip.copy(saved_password)
                print(f"Password for {website} copied to clipboard!")
                return
    print("Website not found.")

def main():
    while True:
        print("Password Manager")
        print("1. Save a password")
        print("2. Get a password")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            save_password(website, username, password)
            print("Password saved successfully!")
        elif choice == '2':
            website = input("Enter the website: ")
            get_password(website)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()