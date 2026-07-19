age=int(input("Enter your age: "))
if age>=18:
    print("You are old enough to learn to drive")
elif age>=0:
    N=18-age
    print("You need {} more years to learn to drive.".format(N))
print("\n")
my_age=18
your_age=int(input("Enter your age: "))
if your_age>my_age:
    if your_age-my_age==1:
        print("You are a year older than me.")
    if your_age-my_age>1:
        print("You are {} years older than me.".format(your_age-my_age))
elif your_age<my_age:
    if my_age-your_age==1:
        print("You are a year younger than me.")
    if my_age-your_age>1:
        print("You are {} years younger than me.".format(my_age-your_age))
elif your_age==my_age:
    print("You are the same age as me.")
print("\n")
a=int(input("Enter number one: "))
b=int(input("Enter number two: "))
if a>b:
    print("{0} is greater than {1}".format(a,b))
elif a<b:
    print("{0} is smaller than {1}".format(a,b))
elif a==b:
    print("a is equal to b")
print('\n')
M=float(input("Enter your marks: "))
if 90<=M<=100:
    print("Grade: A")
elif 80<=M<=89:
    print("Grade: B")
elif 70<=M<=79:
    print("Grade: C")
elif 60<=M<=69:
    print("Grade: D")
elif 0<=M<=59:
    print("Grade: F")
print("\n")
month=str(input("Enter the current month name: "))
if month=='September'or month=='October'or month=='November':
    print("The season is Autumn.")
elif month=='December'or month=='January'or month=='February':
    print("The season is Winter.")
elif month=='March'or month=='April'or month=='May':
    print("The season is Spring.")
elif month=='June'or month=='July'or month=='August':
    print("The season is Summer.")
print("\n")
fruits = ['banana', 'orange', 'mango', 'lemon']
f=str(input("Enter a fruit: "))
if f in fruits:
    print("Fruit exists in the list")
elif f not in fruits:
    fruits.append(f)
    print(fruits)
print("\n")
person={'first_name': 'Asabeneh','last_name': 'Yetayeh','age': 25,'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Space street','zipcode': '02210'}
    }
if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])
    if 'Python' in person['skills']:
        print("Person is skilled in Python:"),print('Python' in person['skills'])
    if 'Javascript' and 'React'in person['skills']:
        print("He is a front end developer.")
    if 'Node' and 'Python' and 'MongoDB' in person['skills']:
        print("He is a backend developer.")
    if 'Node'and 'React' and 'MongoDB' in person['skills']:
        print("He is a full stack developer.")
    else:
        print("unknown title")
if person['is_married'] == True and person['country']=='Finland':
    print("{0} {1} lives in {2}.He is married.".format(person['first_name'],person['last_name'],person['country']))
