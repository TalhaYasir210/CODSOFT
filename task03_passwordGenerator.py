import random
import string

print("Welcome to the Random Password Generator")

def main():
    length = int(input("Enter the length of the password you want to generate: "))
    complexity = input("Enter complexity (low, medium, high): ").lower()

    lowerA = string.ascii_lowercase
    upperA = string.ascii_uppercase
    digitsA = string.digits
    symbolsA = string.punctuation

    if complexity == "low":
        combine = string.ascii_lowercase + string.ascii_uppercase
    elif complexity == "medium":
        combine = string.ascii_lowercase + string.ascii_uppercase + string.digits
    elif complexity == "high":
        combine = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    else:
        print("Invalid complexity level")
        return

    A = random.sample(combine, length)
    password = "".join(A)
    print(password)
    main()

main()
