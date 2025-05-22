empty_list=list()
list_more_itmes=["Bush","Bushra","Onika","Ash","Ashraful","Bushraful"]
print(len(list_more_itmes))

#4. Get the first item, the middle item and the last item of the list
first_item=list_more_itmes[0]
last_item=list_more_itmes[-1]
middle_item=list_more_itmes[int(len(list_more_itmes)/2)]
print(first_item,middle_item,last_item)

mixed_data_types=["Bushra Hossain",25,5.4,'single','Adabor, Mohammadpur']
#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

#Print the list using print()

#Print the number of companies in the list

#Print the first, middle and last company

it_companies=[ 'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
print(it_companies)

print(len(it_companies))
print(it_companies[0],it_companies[int(len(it_companies)/2)],it_companies[-1])

#Print the list after modifying one of the companies
it_companies[4]="NASA"
print(it_companies)

#Add an IT company to it_companies
it_companies.append("Tesla")
print(it_companies)

#Insert an IT company in the middle of the companies list

middle_index=int(len(it_companies)/2)
it_companies.insert(middle_index,"Oreo")

#Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[0].upper())
#Join the it_companies with a string '#;  '
join_string='#;'.join(it_companies)
print(join_string)

#Check if a certain company exists in the it_companies list.
is_company_exist="Apple" in it_companies
print(is_company_exist)

#Sort the list using sort() method
sorted_it_companies= it_companies.sort()
print(sorted_it_companies)

#Reverse the list in descending order using reverse() method
it_companies_reverse=it_companies.reverse()
print(it_companies_reverse)

#Slice out the first 3 companies from the list
print(it_companies[0:3])

#Slice out the last 3 companies from the list
print(it_companies[-3:])

#lice out the middle IT company or companies from the list
print(it_companies[middle_index])

#Remove the first IT company from the list
it_companies.remove(it_companies[0])
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies.remove(it_companies[middle_index])
print(it_companies)

#Remove the last IT company from the list
it_companies.remove(it_companies[-1])
print(it_companies)


#Remove all IT companies from the list
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
del it_companies

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join_list=front_end+back_end
print(join_list)

#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack=join_list.copy()
redux_index=full_stack.index("Redux")
full_stack.insert(redux_index + 1,"Python")
full_stack.insert(redux_index + 2,"SQL")
print(full_stack)