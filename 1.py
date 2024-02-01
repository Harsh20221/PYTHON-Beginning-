#num1=5
#print(num1 , "Is of Type ",type(num1) )
#num2=38
#print(num2 , "Is of Type ",type(num2))
#num3=3+4
#print(5,"is of type ", type(5))

#languages=["swift","Java", "Python"]
#print(languages[1])

#?set is an unordered collection of unique items , set is defined by values sep by commas inside braces 
 #python dictionary is an ordered collection of items , it stores elements in key value pairs 
 #keys are unique identifiers that are associated with each values 
#student_Id={100 , 200 ,300, 400, 500}  #?SET data type

#print (student_Id)
 
#capital_city={"Nepal", "Kathmandu", "India", "New Delhi", "China", "Beijing"} 
#print(capital_city)
#print(capital_city['Nepal'])
#print(capital_city['Kathmandu'])


 
#!python type conversion 

#num = 5  # ?this is implicit data type
##print(num)

#num = 5.5  # ? this is explicit data type
#print(float_num)
# Type conversion is the process of converting data of one type to anotner type  -- for ex converting int data type to str 
#integer_num = 123  #!This is an example of implicit data conversion
#float_num = 1.23
#new_num = integer_num + float_num
#print("Value",new_num)
#print("Data type of new_num", type(new_num),type)

num_string="10"
num_integer=15
print('Data Type ', type(num_string))
num_string=int(num_string)  #?explicit data type conversion
print('Data Type ', type(num_string))
num_sum=num_string+num_integer