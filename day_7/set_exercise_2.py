# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 2

#    Join A and B
A.update(B)
print(A)
#    Find A intersection B
print(A.intersection(B))
#    Is A subset of B
print(A.issubset(B))
#    Are A and B disjoint sets
print(A.isdisjoint(B))
#    Join A with B and B with A
A_join_B=A.union(B)
B_join_A=B.union(A)
print(A_join_B)
print(B_join_A)
#    What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#    Delete the sets completely
del A,B

