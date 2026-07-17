dog={}
dog={'Name':'Oscar','Breed':'Pomeranian','Age':6}
student={'first_name':'Akshat','last_name':'Bhandari','gender':'Male','age':18,
         'marital_status':'Unmarried','skills':'Python coding','country':'India','city':'Dehradun',
         'address':'Post Office Road, Clement Town'}
print(len(student))
print(student['skills'],type(student['skills']))
student['skills']='Public speaking'
print(student.keys())
print(student.values())
print(dog.items())
student.clear()
del dog