# import random

# top_of_range = input("Type a number: ")

# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)
#     if top_of_range <= 0:
#         print("Please type a number larger than 0 next time.")
#         quit()
# else:
#     print("Please type a number next time.")
#     quit()


# random_number = random.randint(0, top_of_range)
# guesses = 0

# while True:
#     guesses += 1
#     user_guess = input("Make a guess: ")
#     if user_guess.isdigit():
#         user_guess = int(user_guess)
#     else:
#         print("Type a number")
#         continue

#     if user_guess == random_number:
#         print("You got it")
#         break
#     elif user_guess > random_number:
#         print("your guess is to high")
#     else:
#         print("Your guess is too low")

# print("You got it it ", guesses, "guesses")


import random 

upper_bound = input("Type a number: ")
if upper_bound.isdigit():
    upper_bound = int(upper_bound)
    if upper_bound <= 0:
        print("Please type number that higher than zero")
        quit()
else:
    print("Type a number next time")
    quit()
lower_bound = 10
random_number = random.randint(lower_bound, upper_bound)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("type a number")
        continue

    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess < random_number:
        print("too low")
    else:
        print("too high")
print("You got it in ", guesses, " guesses")