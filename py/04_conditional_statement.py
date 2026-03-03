## Day 2 - Conditional Statement

##Write a program that categorizes BMI (Body Mass Index) into
##underweight(<18.5), normal weight(<24.9), overweight(<29.9), and
##obesity(<30.0). (formula = kg/m^2)

while True:
    print("=== BMI (Body Mass Index ===)")

    weight=float(input("Please Input Your Weight:"))
    height=float(input("Please Input Your Height:"))
    bmi=(weight/(height**2))

    if bmi <18.5:
        print("Underweight")
    
    elif bmi <24.9:
        print("Normal Weight")

    elif bmi <29.9:
        print("Overweight")

    elif bmi <30.0:
        print("Obersity")

    else:
        print("Terlebih berat Mu Niiii")
    



