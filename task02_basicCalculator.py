print("~~~~ Mini Calculator ~~~~")
num1 = float(input("Enter the first number of your choice: "))
num2 = float(input("Enter the second number of your choice: "))
while True:
    choice = int(input("Press 1 for addition\nPress 2 for subtraction\nPress 3 for multiplication\nPress 4 for division \npress 0 to Quit \nPick any 0 ~ 4: "))
    if choice == 1:
        print(num1 + num2)
    elif choice == 2:
        print(num1 - num2)
    elif choice == 3:
        print(num1 * num2)
    elif choice == 4:
        if num2 == 0:
            print("Division by zero is not allowed.")
        else:
            print(num1 / num2)
    elif choice == 0:
        quit()
    else:
        print("INVALID")

