def print_triangle(rows):
    for i in range(1, rows + 1):
        # Use a loop to print the repeated number in each row
        for j in range(1, i + 1):
            print(i, end="")
        print()


rows = int(input("Enter the number of rows for the triangle: "))


print_triangle(rows)
