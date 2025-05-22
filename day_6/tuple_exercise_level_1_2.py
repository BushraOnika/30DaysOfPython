#Create an empty tuple
empty_tuple=tuple()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters=("Onika","Alia","Era")
brothers=("Apurbo","Riyasat")

#Join brothers and sisters tuples and assign it to siblings
siblings=sisters+brothers

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members_list=list(siblings)
family_members_list.extend(["Anwar","Farhana"])
family_members = tuple(family_members_list)
print(family_members)
#Exercises: Level 2
#Unpack siblings and parents from family_members
siblings=family_members[0:-2]
parents=family_members[-2:]
print(siblings)
print(parents)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print( 'Iceland' in nordic_countries)