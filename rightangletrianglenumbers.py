def print_number_triangle(rows):
    num = 1
    for i in range(1, rows + 1):  #? This will run for one time in the first iteration, f
        for j in range(1, i + 1): #? for i=1 the numbers will be 1, for i=2 the numbers will be 2,3, for i=3 the numbers will be 4,5,6, for i=4 the numbers will be 7,8,9,10, for i=5 the numbers will be 11,12,13,14,15
            print(num, end=" ")
            num += 1
        print()

# Get the number of rows for the triangle
rows = int(input("Enter the number of rows for the triangle: "))

# Call the function to print the number triangle
print_number_triangle(rows)
