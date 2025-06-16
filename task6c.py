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