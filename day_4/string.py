thirty="Thirty"
day="Days"
of="Of"
python = "Python"
single_string=thirty+" "+day+" "+of+" "+python+"."
print(single_string)

sentence="Coding"+" "+"For"+" "+"All."
#print(sentence)

company="Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize()) #only 1st word capital
print(company.title()) #all words 1st alphabet capital
#print(swapcase())
print(company[0:7])

substring="Coding"
if substring.lower() in company.lower():
    print("found")
print(company.replace("Coding","Python"))
print(company.split(" "))

split_comma="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
print(split_comma)

print(company[0]) #What is the character at index 0 in the string Coding For All.

print(len("Coding For All.")-1)#What is the last index of the string Coding For All.

print(company[10])

phrase = "Python For Everyone"
words = phrase.split()
acronym=''.join(word[0].upper() for word in words)
#print(acronym)

phase2="'Coding For All'"
words=phase2.split()
acronym2="".join(words[0].upper() for word in words)

text="Coding For All"
first_c=text.index("C")
print(first_c)

first_f=text.index('F')
print(first_f)

rfind_text="Coding For All People."
print(rfind_text.rfind("l"))

becuase_occurance_text = 'You cannot end a sentence with because because because is a conjunction'
first_occurance_because_index=(becuase_occurance_text.index('because'))

last_occurance_because_index=(becuase_occurance_text.rindex('because'))

phrase_becuase=becuase_occurance_text[first_occurance_because_index:last_occurance_because_index+len("because")]

print(phrase_becuase)

is_startwith_coding= text.startswith("Coding")
print(is_startwith_coding)
is_endwith_coding=text.endswith("coding")
print(is_endwith_coding)

remove_left_right_space='   Coding For All      ' .strip()
print(remove_left_right_space)

print ("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

python_libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
sentence="# ".join(python_libraries)

multiLine_space_seperate ="""I am enjoying this challenge.
I just wonder what is next.""".split("\n")
print(multiLine_space_seperate)

print("Name\tAge\tCountry\tCity\nAsabenah\t250\tFinland\tHelsinki")

multiline_print="""radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square."""
print(multiline_print)

radius = 10

area = 3.14 * radius ** 2
print(f"radius = {radius}")
print(f"area = 3.14 * radius ** 2")
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")

a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")