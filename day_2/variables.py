#2. Day 2: 30 Days of python programming
# Exercises: Level 1
#3. Declare a first name variable and assign a value to it
import math

first_name="Bushra"
#4. Declare a last name variable and assign a value to it
last_name="Hossain"
full_name=first_name+" "+last_name
#print(full_name)
country="Bangladesh"
city="Dhaka"
age=25
year=2025
is_married=False
is_true=True
is_light=False
a,b,c=10,3.256,"Onika"

# Exercises: Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(a))
print(type(b))
print(type(c))

print(len(first_name),len(last_name))

#Compare the length of your first name and your last name
max(len(first_name),len(last_name))
print("first_name length is longer") if len(first_name)>len(last_name) else "last_name length is longer"

num_one=5
num_two=4
total=sum([num_one,num_two])
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_one%num_two
exp=pow(num_one,num_two)
floor_division=math.floor(num_one/num_two) # num_ome // num_two

radius=30
area_of_circle=math.pi*radius**2
circum_of_circle = 2 * math.pi * radius
radius=int (input("Enter Radius"))
area=math.pi*radius**2

irst_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

help('keywords')