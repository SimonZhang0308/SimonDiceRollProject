
import random

totalrolls = 0
totalsum = 0
rolls = []

print("""1. Roll Dice Once
2. Roll Dice 5 Times
3. Roll Dice 'n' Times
4. Roll Dice until Snake Eyes
5. Exit
""")

choice = input("Select an option (1-5): ")
choice = int(choice)

def gambling(n):
    for i in range(n):
        rolls.append(random.randint(1,6))

if choice == 1:
    gambling(2)
    roll1 = rolls[len(rolls)-1]
    roll2 = rolls[len(rolls)-2]
    print(roll1,",",roll2,"(sum:",roll1 + roll2,")")
    print(roll1, "is the number on the first die")
    print(roll2, "is the number on the second die")
    print("The sum is the result of adding the nubmers on both dice.")

if choice == 2:
    gambling(5)
    for i in rolls:
        totalsum += i
    print(totalsum)

if choice == 3:
    totalsum = 0
    n = int(input("How many rolls would you like? "))
    gambling(n)
    for i in rolls:
        totalsum += i
    print(totalsum)



if choice == 4:
    while True:
        roll1 = (random.randint(1, 6))
        if roll1 == 1:
            roll2 = (random.randint(1, 6))
            if roll2 == 1:
                totalrolls += 1
                print("SNAKE EYES! It took only",totalrolls,"rolls to get snake eyes!")
                break
        else:
            totalrolls += 1

if choice == 5:
    ("where is the thirst for gambling?")
    quit()

