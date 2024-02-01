# print("hello,i am shivam ")
# print("my age is",11 + 4 + 3 )
# vegitables="patato,tomato,onion,cally flower "
# print(len(vegitables))
# # print(vegitables[-1:-17])
# # print(vegitables[-1:0])
# # print(vegitables[:-12])
# # print(vegitables[-7:32])
# # nm="harry"
# # print(nm[-4:-2])
# a= "!!shivam@@@!%$
# !!"
# # print(a.upper())
# # print(a.lower())
# print(a.lower)
# print(a.upper)
# print(a.rstrip("@$#!"))
# print(a.rstrip("@"))

# date = 14
# while(date<=2):
#   print(date)
#   date=date-1

# print("its over now")

# a=4
# b=6
# print(a&b)
# print(a|b)
# print(a^be
# print(a<<b)
# print(a>>b)

#calculating the value of the sphare
'''r= float(input("enter the redius of the sphare is :"))
volume=(4/3)(3.148)(r**3)
print(" the valume of the sphare is:", volume)'''
#typ_casting
'''a= "1"
b= "2"
print(int(a)+int(b))'''
# a=input("enter your name:")
# print("my name is ",a)
# x=input("enter the first number:")
# y=input("enter the second number:")
# print(int(x)+int(y))
# print(int(x)-int(y))
# print(int(x)*int(y))
# print(int(x)/int(y))
# print(int(x)//int(y))
# print(int(x)**int(y))
# print(int(x)%int(y))

#change the  degree celceius into  the ferenight 
# temp_cel=float(input("enetr the tempraure in celis:"))
# fere=(temp_cel*1.8)+32
# print("thr trmp in fere is :", fere)

# a = int(input("enetr the num1 is :"))
# b = int(input("enetr the nym2 is :"))
# print("the value of: ", a+b )
# print("the value of: ",  a-b)
# print("the value of ", a*b)

#condition (if - else )

# problem1

# a=int(input("enter the number:"))
# if(a%2==0):
#   print("the num is even")
# else:
#   print("the num is odd")

# problem2

# c_p=int(input("enter the cost price:"))
# s_p=int(input("enetr the selleing price:"))
# if(c_p>s_p):
#   print("the loss is:", c_p-s_p)
# elif(c_p==s_p):
#  print("no profit no loss")
# else:
#   print("the profite is:",s_p-c_p)

#problem3
per=int(input("enter the percentage:"))
if per in range(81,100+1):  # or either write 101 as final range
  print("very good ")
elif per in  range(61,80+1): # or either write 81 as final range 
  print("good")
elif per in range(41,60+1): # or either write 61 as final range
  print("average")
else:
  print("fail")