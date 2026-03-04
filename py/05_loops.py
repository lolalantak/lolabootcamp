## Day 2 - Loops

## Exercises 1 - Create a multiplication table generator.

sifirberapa = True

while sifirberapa:
    sifir = int(input("Please Input The Number:"))

    if sifir==0:
        print("All Answer will be 0")
    
    else:
        for i in range (13):
            print(f"{i} x {sifir} = ({i*sifir})")










