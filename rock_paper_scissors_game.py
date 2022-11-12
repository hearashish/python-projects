import random
user_won = computre_won = 0
options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Enter Rock/Paper/Scissors or Q to quit: ").lower()
    if user_pick == "q":
        break
    if user_pick not in options:
        continue

    # 0 = Rock, 1 = Paper, 2 = Scissors
    computre_pick = options[random.randint(0,2)]

    if user_pick == "rock" and computre_pick == "scissors":
        print("You Won!")
        user_won += 1
    elif user_pick == "paper" and computre_pick == "rock":
        print("You Won!")
        user_won += 1
    elif user_pick == "scissors" and computre_pick == "paper":
        print("You Won!")
        user_won += 1
    else:
        print("You Lost!")
        computre_won += 1

print("You won\t",user_won, "times.\nComputer won\t",computre_won, "times.\nGood Bye!!")