A=['Thirty', 'Days', 'Of', 'Python']
print(' '.join(A))
print("\n")

space = " "
B="Coding" + space + "For" + space + "All"
print(B)
print("\n")

company='Coding For All' 
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print("\n")

print(company.find('Coding'))
print(company.index('Coding'))
print(company.replace('Coding', 'Python'))
print("\n")

print("Python for Everyone".replace("Everyone", "All"))
print("\n")

print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))
print("\n")

print(company[0])
print(company[-1:])
print(company[10])
print("\n")

print(''.join(i[0] for i in "Python for Everyone".split()))
print(''.join(i[0] for i in company.split()))
print("\n")

print(company.index('C'))
print(company.index('F'))
print((company + "People").rindex('l'))
print("\n")

print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))
print('You cannot end a sentence with because because because is a conjunction'[31:54])
print("\n")

print(company.startswith('Coding'))
print(company.endswith('Coding'))
print('   Coding For All      '.strip())
print("\n")

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
print("\n")

C=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(C))
print("\n")
print("I am enjoying this challenge.\nI just wonder what is next.")
print("\n")
print("Name\t\tAge\tCountry\tCity\n")
print("Asabeneh\t250\tFinland\tHelsinki")
print("\n")

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {0} is {1} meters square.".format(radius, area))
print("\n")

a=8 
b=6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")