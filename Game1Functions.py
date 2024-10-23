
def validate():
    moves=["Rock","Paper","Scissors"]
    move=input("Choose Rock, Paper or Scissor!\n")
    if move in moves:
        print("Valid choice")
    else:
        print("Invalid choice. Please try again")
        validate()