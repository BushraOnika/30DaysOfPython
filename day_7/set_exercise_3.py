#Exercises: Level 3
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#    Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set=set(age)
print("List size: ",len(age))
print("Set size: ",len(age_set))
if len(age)>len(age_set):
    print("List is bigger")
else:
    print("Set is bigger")

#    Explain the difference between the following data types: string, list, tuple and set

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
text="I am a teacher and I love to inspire and teach people"
words=text.split(" ")
print(words)
print(len(words))
unique_words=set(words)
print("Unique words count in the sentence : ",len(unique_words))