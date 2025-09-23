

print("Welcome to the game of Danger!!!")
playing = input("Wanna start playing? ")
if playing.lower == "no":
    quit()
answer = input("You got a dirt road, where have a river with full of alligator. You have two option to choose going either left or right? ").lower()

if answer == "left":
    answer = input("This is the starting point of river? What would you like to either swim or walk across it?(swim/walk): ").lower()
    if answer == "swim":
        print("You tried to swam across and eaten by an alligator so the game is over")
    if answer == 'walk':
        print("You walk a lot but ran out of energy to walk more so you lost the game")
    else:
        print("Not a valid option, you lost")

elif answer == "right":
    answer = input("You got a bridge, would like cross it by walk? or by bike?").lower()
    if answer == "bike":
        print("your bike ran out of fuel so you lost")
    if answer == "walk":
        answer = input("You met with a stranger, would you like to talk with him? ").lower()
        if answer == "yes":
            print("You won, bkz the stranger gave you the winning gold")
        else:
            print("you missed talking with the stranger, who had your gold to win")
    else:
        pass




