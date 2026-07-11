a=[]
b=[1,2,3,4,5]
print(len(b))
print(b[0],b[len(b)//2],b[-1])
mixed_data_types = ['Akshat', 18,5.10,'Unmarried','Clement Town']
print("\n")

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print("\n")

print(it_companies[0],it_companies[len(it_companies)//2],it_companies[-1])
it_companies[0]='Meta'
print(it_companies)
print("\n")

it_companies.append('X')
print(it_companies)
print("\n")

it_companies.insert(len(it_companies)//2,'Tesla')
print(it_companies)
print("\n")

it_companies[1] = it_companies[1].upper()
print(it_companies)
print('#;'.join(it_companies))
print('Facebook' in it_companies)
print("\n")

it_companies.sort()
print(it_companies)
print("\n")

it_companies.reverse()
print(it_companies)
print("\n")

print(it_companies[:3])
print(it_companies[-3:])
print(it_companies[4:5])
print("\n")

it_companies.pop(0)
print(it_companies)
it_companies.pop(len(it_companies)//2)
print(it_companies)
it_companies.pop(-1)
print(it_companies)
print("\n")

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
developement=front_end+back_end
print(developement)
front_end.extend(back_end)
print(front_end)
print("\n")

full_stack=front_end.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

