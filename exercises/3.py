age=18
height=5.10
complex=1+6j

base=float(input("Enter the length of the base of a triangle: "))
height=float(input("Enter the height of the triangle: "))
area = 0.5*base*height
print("The area of the triangle is:", area)
print("\n")

a=int(input("Enter side a of a triangle: "))
b=int(input("Enter side b of a triangle: "))
c=int(input("Enter side c of a triangle: "))
Perimeter = a+b+c
print("The perimeter of the triangle is:", Perimeter)
print("\n")

length=float(input("Enter the length of a rectangle: "))
breadth=float(input("Enter the breadth of a rectangle: "))
area_of_rectangle=length*breadth
print("The area of the rectangle is:", area_of_rectangle)
perimeter_of_rectangle=2*(length+breadth)
print("The perimeter of the rectangle is:", perimeter_of_rectangle)
print("\n")

pi=3.14
radius = float(input("Enter the radius of the circle: "))
area_of_circle = pi*(radius**2)
print("The area of the circle is:", area_of_circle)
circum_of_circle = 2*pi*radius
print("The circumference of the circle is:", circum_of_circle)
print("\n")

x1,y1 = 2,2
x2,y2 = 6,10
distance =((x2-x1)**2 + (y2-y1)**2)**0.5
print("Euclidean distance between (2, 2) and (6, 10) is:",distance)
print("\n")

#Calculate the value of y (y = x^2 + 6x + 9).
# Try to use different x values and figure out at what x value y is going to be 0.
x=int(input("Enter the value of x: "))
y = x**2 + 6*x + 9
print("The value of y is:", y)
print("\n")

print({"The length of 'python' is":len("python")})
print({"The length of 'dragon' is":len("dragon")})
print(len("python")!=len("dragon"))
print("\n")

print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'python' and 'on' not in 'dragon')
print("\n")

q=len("python")
float(q)
print("In float",q)
str(q)
print("In string",q)
print("\n")

E=int(input("Enter a number: "))
if E%2==0:
    print("The number is even")
else:
    print("The number is odd")
print("\n")

integer_no=int(2.7)
r=7%3
print(r==integer_no)

print(type('10')==type(10))
c='9.8'
print(int(float(c)) == 10)
print("\n")

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours_per_day= float(input("Enter hours per day: "))
rate = float(input("Enter rate per hour: "))
earnings = hours_per_day * rate * 7
print("Your weekly earnings is:", earnings)
print("\n")

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for {0} seconds.".format(seconds))
print("\n")

i=1
while(i<=5):
    print(i,1,i**1,i**2,i**3,"\n")
    i+=1
    
