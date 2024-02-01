no=int(input("Enter the N no of terms upto which you want your sum :"))
terms=0
sum=0
print("The Numbers are ")
for i in range(1, no+1):
    if i%2!=0:
        print(i)

while True: 
    if terms%2!=0:
        sum=sum+terms
    terms=terms+1
    if terms>no:
        break
print("The sum of N terms is ",sum)
    
   