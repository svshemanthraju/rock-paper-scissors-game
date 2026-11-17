# Rock Paper Scissors Game in Python
import random

print("The computer is going to play Rock Paper Scissors. Try to beat it!")

options = ("rock", "paper", "scissors")
option = random.choice(options)

user = input("Enter your choice: ").lower().strip()

if option == user:
    print("It's a draw!")
elif (
    (user == "rock" and option == "paper")
    or (option == "rock" and user == "scissors")
    or (option == "scissors" and user == "paper")
):
    print("You have lost the game!")
elif (
    (option == "rock" and user == "paper")
    or (option == "scissors" and user == "rock")
    or (user == "scissors" and option == "paper")
):
    print("You have won the game!")
else:
    print("Invalid input")

print("---------------------------------------")
print(f"The computer has chosen {option}")
print(f"You have chosen {user}")
