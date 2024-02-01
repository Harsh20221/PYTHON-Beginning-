def multiplication_table(number):
    for i in range(1, 11):
        result = number * i
        print(number, "x", i, "=", result)

num = int(input("Enter the number for the multiplication table: "))
multiplication_table(num)
