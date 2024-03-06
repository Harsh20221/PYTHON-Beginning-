i=int(input("Enter the number to find the factorial: "))
if i==0:
    print("The factorial of 0 is 1")
elif (i==1):
    print("The factorial of 1 is 1")
else:
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print("The factorial of ",i," is ",fact)
    
    

    