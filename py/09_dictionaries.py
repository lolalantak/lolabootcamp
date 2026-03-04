## Day 3 - Dictionaries

## 1 - Create Dictionary

student_records = {
    "student_001": {
        "name" : "John",
        "age" : 19,
        "major" : "Computer Science",
        "grades" : [85,92,78]
    },
    "student_002": {
        "name" : "Sarah",
        "age" : 20,
        "major" : "Biology",
        "grades" : [90,88,95]
    },
}
 
 # 2 - Add New Student

student_records ["student_003"] = {
    "name" : "Mike",
        "age" : 18,
        "major" : "Math",
        "grades" : [82,79,91]
}

# 3 Update John age=20

student_records ["student_001"]["age"] = 20

# loop & print

keys = student_records.keys ()
values = student_records.values ()
items = student_records.items ()

for student_id, student_info in student_records.items ():
    print (f"Student ID : {student_id} | Name : {student_info ["name"]} | Major : {student_info ["major"]}")