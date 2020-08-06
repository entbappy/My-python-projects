# Game development ,,, Game name Snake , Water , gun
import random

lst = ["s","w","g"]
chance = 10
no_chance = 0
human_points = 0
computer_points = 0

print("         Snake , Water , Gun ")
while no_chance<chance:
    print("s for Snake\nw for Water\ng for Gun\n")
    _input = input("Choose one...\n")
    l = _input.lower()

    _random = random.choice(lst)

    if l == _random:
        print(f"You chose {l} and Computer chose {_random}\n")
        print("Tie!!! Both were same")

    # If human choose "s"
    elif l == "s" and _random == "g":
        computer_points = computer_points+1
        print("Computer won with 1 point!!")
        print(f"You chose {l} and Computer chose {_random}\n")
        print(f"Your point is {human_points} and Computer point is {computer_points}\n")

    elif l == "s" and _random == "w":
        human_points = human_points+1
        print("Human won with 1 point!!")
        print(f"You chose {l} and Computer chose {_random}\n")
        print(f"Your point is {human_points} and Computer point is {computer_points}\n")

    # If human choose "w"
    elif l == "w" and _random == "s":
        computer_points = computer_points+1
        print("Computer won with 1 point!!")
        print(f"You chose {l} and Computer chose {_random}\n")
        print(f"Your point is {human_points} and Computer point is {computer_points}\n")

    elif l == "w" and _random == "g":
        human_points = human_points+1
        print("Human won with 1 point!!")
        print(f"You chose {l} and Computer chose {_random}\n")
        print(f"Your point is {human_points} and Computer point is {computer_points}\n")

    # If human choose "g"
    elif l == "g" and _random == "s":
        human_points = human_points+1
        print("Human won with 1 point!!")
        print(f"You chose {l} and Computer chose {_random}\n")
        print(f"Your point is {human_points} and Computer point is {computer_points}\n")

    elif l == "g" and _random == "w":
        computer_points = computer_points+1
        print("Computer won with 1 point!!")
        print(f"You chose {l} and Computer chose {_random}\n")
        print(f"Your point is {human_points} and Computer point is {computer_points}\n")

    else:
        print("You put wrong input!!!")

    no_chance = no_chance+1
    print(f"You have left {chance - no_chance} out of {chance}")
print("Game Over!")
if human_points == computer_points:
    print("Tie ")
elif human_points>computer_points:
    print(f"Human Won with {human_points} points ")
    print(f"Your points were {human_points}")
    print(f"Computer points were {computer_points}")
else:
    print(f"Computer won with {computer_points} points")
    print(f"Computer points were {computer_points}")
    print(f"Your points were {human_points}")