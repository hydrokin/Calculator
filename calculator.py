def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

def calculator():
    print("Welcome to the Calculator App!")

    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Thank you for using the Calculator App. Goodbye!")
            break

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == "4":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please try again.")

calculator()
