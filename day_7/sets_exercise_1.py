it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#    Find the length of the set it_companies
print(len(it_companies))
#   Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#    Insert multiple IT companies at once to the set it_companies
it_companies.update(['NASA','Github'])
print(it_companies)
#    Remove one of the companies from the set it_companies
it_companies.remove('Apple') #it gives error when there is no element

#    What is the difference between remove and discard
it_companies.discard('Facebook') # it doesn't give error