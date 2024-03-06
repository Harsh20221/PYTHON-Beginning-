list=[]
while True:
    I=int(input("Please Enter the Data to be pushed inside the List: "))
    list.append(I)
    ch=input("entern to close ")
    if ch=="n":
        break
    
    
sum=0
for i in range(0,len(list)):
    sum=sum+list[i]  ###!!! It is important that in order to find the sum or multiplication of a list you must enter it as list(i) else it will not work 
print("The sum of all the numbers in the list is ",sum)