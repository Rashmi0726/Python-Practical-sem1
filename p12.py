'''WAP to accept a name from a user.
Raise and handle appropriate exception(s) if 
the text entered by the user contains digits and/or special characters'''


def validate_name(name):
    for char in name:
        if not char.isalpha() and char != ' ':
            raise ValueError("Invalid character in the name. Please enter only alphabetic characters and spaces.")

try:
    user_name = input("Enter your name: ")
    validate_name(user_name)
    print(f"Hello, {user_name}!")
except ValueError as ve:
    print(f"Error: {ve}")
