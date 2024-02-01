a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operator = input("Enter the operator: ")

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case _:
        print("Invalid operator. Please enter '+' or '-'.")
