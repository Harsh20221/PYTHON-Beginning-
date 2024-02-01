# # # # print("hello,i am shivam ")
# # # # print("my age is",11 + 4 + 3 )
# # # # vegitables="patato,tomato,onion,cally flower "
# # # # print(len(vegitables))
# # # # # print(vegitables[-1:-17])
# # # # # print(vegitables[-1:0])
# # # # # print(vegitables[:-12])
# # # # # print(vegitables[-7:32])
# # # # # nm="harry"
# # # # # print(nm[-4:-2])
# # # # a= "!!shivam@@@!%$#!!"
# # # # # print(a.upper())
# # # # # print(a.lower())
# # # # print(a.lower)
# # # # print(a.upper)
# # # # print(a.rstrip("@$#!"))
# # # # print(a.rstrip("@"))

# # # # date = 14
# # # # while(date<=2):
# # # #   print(date)
# # # #   date=date-1

# # # # print("its over now")

# # # # a=4
# # # # b=6
# # # # print(a&b)
# # # # print(a|b)
# # # # print(a^be
# # # # print(a<<b)
# # # # print(a>>b)

# # # #calculating the value of the sphare
# # # '''r= float(input("enter the redius of the sphare is :"))
# # # volume=(4/3)(3.148)(r**3)
# # # print(" the valume of the sphare is:", volume)'''
# # # #typ_casting
# # # '''a= "1"
# # # b= "2"
# # # print(int(a)+int(b))'''
# # # # a=input("enter your name:")
# # # # print("my name is ",a)
# # # # x=input("enter the first number:")
# # # # y=input("enter the second number:")
# # # # print(int(x)+int(y))
# # # # print(int(x)-int(y))
# # # # print(int(x)*int(y))
# # # # print(int(x)/int(y))
# # # # print(int(x)//int(y))
# # # # print(int(x)**int(y))
# # # # print(int(x)%int(y))

# # # #change the  degree celceius into  the ferenight
# # # # temp_cel=float(input("enetr the tempraure in celis:"))
# # # # fere=(temp_cel*1.8)+32
# # # # print("thr trmp in fere is :", fere)

# # # # a = int(input("enetr the num1 is :"))
# # # # b = int(input("enetr the nym2 is :"))
# # # # print("the value of: ", a+b )
# # # # print("the value of: ",  a-b)
# # # # print("the value of ", a*b)

# # # #condition (if - else )

# # # # problem1

# # # # a=int(input("enter the number:"))
# # # # if(a%2==0):
# # # #   print("the num is even")
# # # # else:
# # # #   print("the num is odd")

# # # # problem2

# # # # c_p=int(input("enter the cost price:"))
# # # # s_p=int(input("enetr the selleing price:"))
# # # # if(c_p>s_p):
# # # #   print("the loss is:", c_p-s_p)
# # # # elif(c_p==s_p):
# # # #  print("no profit no loss")
# # # # else:
# # # #   print("the profite is:",s_p-c_p)

# # # #problem3
# # # per=int(input("enter the percentage:"))
# # # if per>80:
# # #   print("very good ")
# # # elif per>60:
# # #   print("good")
# # # elif per>40:
# # #   print("average")
# # # else:
# # #   print("fail")

# # # #problem4

# # math_markes=int(input("enter the math markes:"))
# # eng_markes=int(input("enetr the english markes:"))
# # if(math_markes>80 and eng_markes>80):
# #   print("grade A")
# # elif(math_markes>80 or eng_markes>80):
# #   print("grade B")
# # elif(math_markes <=60 and eng_markes==70):
# #   print("grade C")
# # else:
# #   print("grade D")
# num=int(input("enetr the number :"))
# if num>1000 and num<9999:
#   print("true")
# else:
#   print("false")

# a= int(input("enter the num1 is:"))
# b= int(input("enter the num2 is:"))
# c= int(input("enter the num3 is:"))
# if a>b and a>c:
#   print("a is greatest no. among them")
# elif b>a and b>c:
#     print("b is greatest no. among them")
# else:
#     print("c is greatest no. among them")
a=int(input("enter the num1 is:"))
b=int(input("enter the num2 is:"))
operator= (input(" enter oprator:"))
match operator:
 case "+":
   print(a + b) 
 case "-" :
  print(a - b)

    

# if a>b:
#   if a>c:
#     print("a is the big number among them")
#   else:
#     print("c is the big number among them")
# else:
#   if b>c:
#      print("b is the big number among them")
#   else:
#      print("c is the big number among them")