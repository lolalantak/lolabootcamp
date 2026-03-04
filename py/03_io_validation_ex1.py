## Exercises 1
## 1.Create a simple calculator that takes two number and an operation from user ##

number1=float(input("Insert Your 1st Number:"))
number2=float(input("Insert Your 2nd Number:"))
operation=input("Select Your Operation (+,-,*,/):")

if operation=="+":
    result = number1+number2

elif operation=="-":
    result = number1-number2

elif operation=="*":
    result = number1*number2

elif operation=="/":
    if number2 !=0:
       result = number1/number2
    else:
        result = "Error!. Mana Boleh"

else:
    result = "Invalide Operation"


#Output result

print(f"Your Answer:{result}")