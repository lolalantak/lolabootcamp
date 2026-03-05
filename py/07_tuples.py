## Day 3 - Tuples

coordinates = (10,20)
person = ("Abu",25,"Engineer",23)
single_item = (42,)

# Tuple operation

print (coordinates [0])
print (len(person))

# Exercises - Create a system that stores student grades as tuples (name, subject, grade)
# and uses sets to find unique subjects and students.

grades = [
    ("Alice","Math",85),
    ("Bob","Science",92),
    ("Alice","Science",78),
    ("charlie","Math",90),
    ("Bob","Math",88),
    ("Alice","English",95)
]

listofname = set (gred [0] for gred in grades)
listofsubject = set (gred [1] for gred in grades)
listofgrade = set (gred [2] for gred in grades)

print (f"Bil Pelajar adalah : {len (listofname)} & Senarai Pelajar ialah : {listofname}")
print (f"Senarai Subject : {listofsubject}")

for name, subject, grede in grades:
    print (f"Name:{name} | Subject : {subject [listofsubject]} | Gred : {grede}")



