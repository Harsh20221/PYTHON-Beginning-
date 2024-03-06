num=int(input("Please Enter the Number whose Harmonic series you want"))
sum=1
for i in range(1,num+1):
    print(f"1/{i}",end=" ")
    sum+=(1/i)
print()
print("The Sum of series is ",sum)