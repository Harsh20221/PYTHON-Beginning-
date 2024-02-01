rang=int(input("Please enter The Range of numbers in which you want prime no"))
for num in range(1,rang):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
         
        else:
            print(num)