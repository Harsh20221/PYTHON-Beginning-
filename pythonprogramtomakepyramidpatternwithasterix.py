def print_pyramid(rows):
    for i in range(1, rows + 1):  #?for i=1 the spaces will be 4, for i=2 the spaces will be 3, for i=3 the spaces will be 2, for i=4 the spaces will be 1, for i=5 the spaces will be 0
        # ?Print leading spaces
        print(" "*  (rows - i), end="")   #?
        print("* " * i)


rows = int(input("Enter the number of rows for the pyramid: "))

print_pyramid(rows)
