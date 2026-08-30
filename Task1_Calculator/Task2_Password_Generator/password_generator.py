import random
import string

print("================================")
print("       PASSWORD GENERATOR")
print("================================")

while True:

    try:
        length = int(input("\nEnter password length: "))

        if length <= 0:
            print("Please enter a positive number.")
            continue

        if length < 4:
            print("For a strong password, use at least 4 characters.")

        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        password = ''.join(
            random.choice(characters)
            for _ in range(length)
        )

        print("\nGenerated Password:")
        print(password)

        again = input("\nGenerate another password? (yes/no): ")

        if again.lower() != "yes":
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number!")
