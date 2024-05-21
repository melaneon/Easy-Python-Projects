name = input("What is your name? ")
print("Welcome " + name + "to this adventure!")

answer = input(
    "You are on the road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, and you can walk around it or swim across? Type 'walk' to walk around ot 'swim' to swim: ").lower()
    if answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
        print("You lose.")
    elif answer == "swim":
        print("You swam across and were eaten by alligator.")
        print("You lose.")
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or head back? (cross/back): ").lower()
    if answer == "back":
        answer = input(
            "You go back to a main road. Now you can decide to drive in the mountains or go left (drive/left): ").lower()
        if answer == "drive":
            print("You drove for hours and hours and ran out of gas.")
            print("You lose.")
        if answer == "left":
            answer = input(
                "You come to a river, and you can walk around it or swim across? "
                "Type 'walk' to walk around ot 'swim' to swim: ").lower()
            if answer == "walk":
                print("You walked for many miles, ran out of water and you lost the game.")
                print("You lose.")
            elif answer == "swim":
                print("You swam across and were eaten by alligator.")
                print("You lose.")
            else:
                print("Not a valid option. You lose.")
        else:
            print("Not a valid option. You lose.")
    elif answer == "cross":
        answer = input("You cross a bridge and meet a stranger. Do you talk to them?(yes/no): ").lower()
        if answer == "yes":
            # WIN option!
            print("You talked to the stranger and they gave you gold.")
            print("You WIN!")
        elif answer == "no":
            print("You are rude. They kill you.")
            print("You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print(f"Thank you for playing, {name}. Let's play again soon!")

