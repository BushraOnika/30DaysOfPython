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

