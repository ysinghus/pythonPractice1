import random
# number guessing game
userInput=input("Please guess a number between 5-10: ")
userInput=int(userInput)
print(userInput)
computerNumber=random.randint(5,10)
if(userInput==computerNumber):
    print("You guessed the correct number")
else:
    print(f"You guessed the incorrect number. The computer's number was: ",{computerNumber})
