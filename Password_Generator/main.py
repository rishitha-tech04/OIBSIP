import random
import string

print("===== Password Generator =====")

try:
    length = int(input("Enter the password length: "))

    if length <= 0:
        print("Password length must be greater than zero.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

except ValueError:
    print("Invalid input! Please enter a valid number.")