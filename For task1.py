number = int(input("Enter a number: "))      #Ask user to enter a number
number += 1

for x in range(number):                      #Set x to be user's number
    for y in range (1, 13):                  #Set y to have a range from 1 to 12
        total = (f"{x} * {y} = {x*y}")       #calculate 
        print(total)
    