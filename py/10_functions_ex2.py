## Day 4 - Functions

# Exercises 2
# 2.Build a temperature converter function. (Celsius to Fahrenheit)



# input Data

celcius = float (input ("Please input the temperatue in Celsius:"))
   
# Convert to Fahrenheit

def converter (celcius):
   fah = (celcius * 9/5) +32
   return fah

fahrenheit = converter (celcius)

# Print Result

print (f"Temperature in Fahrenheit:{fahrenheit}")