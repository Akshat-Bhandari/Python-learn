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
print("\n")

#2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("The minimum age in the list is:",ages[0])
print("The maximum age in the list is:",ages[-1])

ages.append(ages[0])
ages.append(ages[-1])
print(ages)

if len(ages)%2==0:
    median=(ages[len(ages)//2]+ages[len(ages)//2+1])/2
else:
    median=ages[len(ages)//2]
print("The median age in the list is:",median)

for i in range(len(ages)):
    sum=0
    sum=sum+ages[i]
avg=sum/len(ages)
print("The average age in the list is:",avg)

print("The range of the ages in the list is:",ages[-1]-ages[0])
M=abs(ages[-1]-avg)
m=abs(ages[0]-avg)
print("The difference between the maximum and average is:",M)
print("The difference between the minimum and average is:",m)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

if len(countries)%2==0:
    middle_countries=countries[len(countries)//2-1:len(countries)//2+1]
else:
    middle_countries=countries[len(countries)//2]
print("The middle countries in the list are:",middle_countries)

if len(countries)%2==0:
    first_half=countries[:len(countries)//2]
    second_half=countries[len(countries)//2:]
else:
    first_half=countries[:len(countries)//2+1]
    second_half=countries[len(countries)//2+1:]
print("The first half of the countries list is:\n\n",first_half)
print("The second half of the countries list is:\n\n",second_half)
print("\n")
print(len(countries))
print(len(first_half))
print(len(second_half))
print("\n")

['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
a,b,c,*scandic=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(a)
print(b)
print(c)
print(scandic)
