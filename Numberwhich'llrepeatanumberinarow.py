def print_number_triangle(rows):
    for i in range(1, rows + 1):  #? this loop will run for 1 time in the first iteration 
        # Print numbers in each row
        for j in range(1, i + 1): #? for i=1 the numbers will be 1, 
            print(j, end=" ")   #? since j always starts from 1 and ends at i+1, so for i=1, j will be 1, for i=2, j will be 1,2, for i=3, j will be 1,2,3, for i=4, j will be 1,2,3,4, for i=5, j will be 1,2,3,4,5
        # Move to the next line after each row
        print()

# Get the number of rows for the triangle
rows = int(input("Enter the number of rows for the triangle: "))

# Call the function to print the number triangle
print_number_triangle(rows)
