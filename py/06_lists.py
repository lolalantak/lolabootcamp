## Day 3 - Lists

fruits = ["apple","banana",'orange']
numbers = [1,2,3,4,5]
mixed = ["hello",42,3.14,True]
empty_list = []

# Accessing Element

#print(fruits[0])   
#print(fruits[-1])
#print(numbers[1:4]) #akan berhenti sblm index 4
#print(numbers[:3]) #akan berhenti sblm index 3
#print(numbers[2:]) #akan bermula selepas index 2

# lists Operation: CRUD a list

fruits.append ("grape")    # Add to end fruits list
fruits.insert (1,"kiwi")
fruits.remove ("banana")
popped = fruits.pop ()
fruits.sort ()
fruits.reverse ()


print (fruits)  

## Exercises
## 2.Write a program that finds the largest and smallest number in list.

listofnumbers = [1,23,2.47,4545,34,678]

largestnumber = max (listofnumbers)
smallestnumber = min (listofnumbers)

print (f"The largest Numbers is : {largestnumber}")
print (f"The smallest Number is: {smallestnumber}")