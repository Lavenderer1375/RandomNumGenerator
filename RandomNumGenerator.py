import random

userInput = ""
while userInput != "done":
    sides = int(input("how many sides does the dice have?\n"))
    randomNum = random.randint(0, sides)
    print(randomNum)
