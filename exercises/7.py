# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
it_companies.update(['Meta','Nvidia'])
it_companies.remove("Oracle")

print(A|B) #or we can write print(A.union(B))
print(A&B) #or we can write print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.update(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B

print(len(age))
AGE=list(age)
print(len(AGE))

S="I am a teacher and I love to inspire and teach people"
W=S.split()
w=set(W)
print("The number of unique words in the sentence are {0}".format(len(w)))