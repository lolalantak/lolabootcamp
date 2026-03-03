## Day 2 - IO Validation

#Insert Validation

name = input("Enter Your Name:")
height=float(input("Enter You Height:"))

while True:
    try:
        age = int(input("Enter Your Age:"))
        if age > 0 and age < 150:
            break
        else:
            print("Age must be positive !!!")
    except ValueError:
        print("Invalid Input!!!")


#Output Validation

print(f"Hello,{name}")
print(f"You are {age} years old and {height} feet tall")


