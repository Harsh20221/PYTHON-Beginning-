def print_number_pyramid(rows):
    num = 1
    for i in range(1, rows + 1):
        # Print leading spaces
        print(" " * (rows - i), end="") #? for i=1 the spaces will be 4, for i=2 the spaces will be 3, for i=3 the spaces will be 2, for i=4 the spaces will be 1, for i=5 the spaces will be 0
        
        # Print numbers
        for j in range(i):  #? for i=1 the numbers will be 1, for i=2 the numbers will be 2,3, for i=3 the numbers will be 4,5,6, for i=4 the numbers will be 7,8,9,10, for i=5 the numbers will be 11,12,13,14,15
            print(num, end=" ")
            num += 1  #? 0 will not print as num is 1 initially and it will be incremented by 1 after printing each number

        # Move to the next line after completing a row
        print()

# Get the number of rows for the pyramid
rows = int(input("Enter the number of rows for the pyramid: "))

# Call the function to print the pyramid with numbers
print_number_pyramid(rows)
