import math

print(3+4)
print(3-4)
print(3*4)
print(4%3)
print(4/3)
print(3**4)
print(4//3)
#Write strings on the python interactive shell. The strings are the following:
print("Bushra Hossain")
print("Hossain")
print("Bangladesh")
print("I am enjoying 30 days of python")
#Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Bushra"))
print(type("Hossain"))
print(type("Bangladesh"))

# Exercise: LEVEL 3
#Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
integer_num=2
float_num=1.3
complex_num=1+8j
string_example="Onika"
boolean_example=True
list_example=['Onika','Bush']
tuple_example=("Bush",25) #can't be added or removed
set_example={"Bush",3} #can be add added and removed and no duplicate values
dictionary_example={"name": "Bush","age":25,"city":"Dhaka"}

#Find an Euclidian distance between (2, 3) and (10, 8)
euclidian_distance = math.sqrt(pow(10-2,2)+pow(3-8,2))
print(euclidian_distance)

