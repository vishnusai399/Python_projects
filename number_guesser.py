import random

top_of_range=input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("enter a number greater than 0 next time")
        quit()
else:
    print("Enter a number")
    quit()
random_number=random.randint(0,top_of_range)

guesses=0

while True:
    guesses+=1
    user_guess=input("Guess the number: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("enter a number")
        continue
    if user_guess==random_number:
        print("you got it!")
        break

    elif user_guess>random_number:
        print("You were above number")
        
    else:
        print("You were below the number!")
print("you guessed it in",guesses,"guesses")