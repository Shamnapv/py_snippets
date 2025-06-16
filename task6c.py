student={"name":"shamna","roll_no":63,"department":"it","marks":88}
print("original dictionary:",student)
print("Name :",student["name"])
print("roll_no using get():",student.get("roll_no"))
student["college"]="Gec palakkad"
print("after adding college",student)
student["marks"]=90
print("After update mark",student)
student.pop("roll_no")
print("After pop(roll_no)",student)
student.update({"email":"shamna@gmail.com","phone_no":"9078563412"})
print("After adding email and phone_no using update",student)
print("keys:",student.keys())
print("values:",student.values())
print("items:",student.items())
student.setdefault("gender","Female")
print("After setdefault",student)
student2=student.copy()
print("copy of student:",student2)
print("removed item using popitem()",student.popitem())
keys=['fruits','vegetable']
dictionary=dict.fromkeys(keys,'not provided')
print(dictionary)
print("After clear():",student.clear())

"""output: (base) PS C:\Users\shaim\Desktop\pythonlab> python task6c.py
original dictionary: {'name': 'shamna', 'roll_no': 63, 'department': 'it', 'marks': 88}
Name : shamna
roll_no using get(): 63
after adding college {'name': 'shamna', 'roll_no': 63, 'department': 'it', 'marks': 88, 'college': 'Gec palakkad'}
After update mark {'name': 'shamna', 'roll_no': 63, 'department': 'it', 'marks': 90, 'college': 'Gec palakkad'}
After pop(roll_no) {'name': 'shamna', 'department': 'it', 'marks': 90, 'college': 'Gec palakkad'}
After adding email and phone_no using update {'name': 'shamna', 'department': 'it', 'marks': 90, 'college': 'Gec palakkad', 'email': 'shamna@gmail.com', 'phone_no': '9078563412'}
keys: dict_keys(['name', 'department', 'marks', 'college', 'email', 'phone_no'])
values: dict_values(['shamna', 'it', 90, 'Gec palakkad', 'shamna@gmail.com', '9078563412'])
items: dict_items([('name', 'shamna'), ('department', 'it'), ('marks', 90), ('college', 'Gec palakkad'), ('email', 'shamna@gmail.com'), ('phone_no', '9078563412')])  
After setdefault {'name': 'shamna', 'department': 'it', 'marks': 90, 'college': 'Gec palakkad', 'email': 'shamna@gmail.com', 'phone_no': '9078563412', 'gender': 'Female'}
copy of student: {'name': 'shamna', 'department': 'it', 'marks': 90, 'college': 'Gec palakkad', 'email': 'shamna@gmail.com', 'phone_no': '9078563412', 'gender': 'Female'}
removed item using popitem() ('gender', 'Female')
{'fruits': 'not provided', 'vegetable': 'not provided'}
After clear(): None"""
