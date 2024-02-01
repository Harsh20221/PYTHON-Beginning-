def print_triangle(rows):
    for i in range(1, rows + 1):
        # Print numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        
        # Move to the next line after each row
        print()

# Get the number of rows for the triangle
rows = int(input("Enter the number of rows for the triangle: "))

# Call the function to print the triangle
print_triangle(rows)
