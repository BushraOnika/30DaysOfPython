import math

age=25
height=5.11
complex_num=5+4j
#rite a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base=int(input("Enter base: "))
height=int(input("Enter heigth: "))
print("The area of the triangle is ",0.5*base*height)

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a=int(input("Enter side a: "))
side_b=int(input("Enter side b: "))
side_c=int(input("Enter side c: "))
print("The perimeter of the triangle is ", side_a+side_b+side_c)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length= int(input("Enter length: "))
width= int(input("Enter width: "))
print("Area:" ,length*width)
print("perimeter: ", 2*(width+length))

#
radius=int (input("Enter Radius"))
circum_of_circle = 2 * math.pi * radius
area=math.pi*radius**2

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

## Find the length of 'python' and 'dragon' and make a falsy comparison statement
print(len('python'))
print(len('dragon'))
print("python"=="dragon")

