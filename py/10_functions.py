## Day 4 - Functions

# Exercises 1
# 1.Write a function that checks if a number is prime.

# Masukkan Number

def input_number (num):
    num = int (input("Please input the number:"))
    return num

# Check Prime Number

def prime_number (num):
    if num <= 1:
        return False
    
    for prime in range (2,num):
        if num % prime == 0:
            return False
    
    return True

number = input_number(int)

# Print result

if prime_number (number):
    print (f"{number} is Prime Number")

else:
    print (f"{number} Not a Prime Number")

