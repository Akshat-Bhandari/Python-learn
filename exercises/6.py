t=()
brothers=('Ankit','Shyam')
sisters=('Akansha','Ankita')
siblings=brothers+sisters
print(len(siblings))
family_members=siblings+('Ram','Shruti')
list(family_members)
siblings=tuple(family_members[:4])
parents=tuple(family_members[-2:])
print(siblings)
print(parents)
print('\n')
fruits=('apple','banana','orange','watermelon')
vegetables=('spinach','capsicum','pumpkin','eggplant')
animal_products=('milk','chicken','pork','prawns')
food_stuff_tp=fruits+vegetables+animal_products

food_stuff_lt=list(food_stuff_tp)
if len(food_stuff_lt)%2==0:
    mid=len(food_stuff_lt)//2
    print(food_stuff_lt[mid-1:mid+1])
else:
    mid=len(food_stuff_lt)//2
    print(food_stuff_lt[mid])
    
print('\n')
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('\n')
print('Estonia' in nordic_countries)
print('Iceland'in nordic_countries)


