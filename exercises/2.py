#2

#Declaring Variables
first_name = "Akshat"
last_name = "Bhandari"
full_name ="Akshat Bhandari"
country = "India"
city ="Dehradun"
age = 18
year = 2026
lane,street,city,state= 22,"Turner Road","Dehradun","Uttarakhand"

#Checking the data types of the variables
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(lane))
print(type(street))
print(type(city))
print(type(state))

print("lengths of the first name and last name")
print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
print("The sum of the two numbers is:", total)
diff=num_one - num_two
print("The difference of the two numbers is:", diff)
product=num_one * num_two
print("The product of the two numbers is:", product)
division=num_one / num_two
print("The division of the two numbers is:", division)
remainder=num_one % num_two
print("The remainder of the two numbers is:", remainder)
exp =num_one ** num_two
print("The exponent of the two numbers is:", exp)
floor_division=num_one // num_two
print("The floor division of the two numbers is:", floor_division)

radius = float(input("Enter the radius of the circle: "))
area_of_circle = 3.14*(radius**2)
print("The area of the circle is:", area_of_circle)
circum_of_circle = 2*3.14*radius
print("The circumference of the circle is:", circum_of_circle)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))
print("{0}, {1}, {2}, {3}".format(first_name, last_name, country, age))