import random

computer_wins=0
user_wins=0

options=['rock','paper','scissors']

while True:
    user_input=input("type rock/paper/scissors or q to quit:").lower()
    if user_input =='q':
        break

    if user_input  not in options:
        continue

    random_number=random.randint(0,2)

    computer_pick=options[random_number]
    print('computer_picked',computer_pick+'.')

    if user_input=='rock' and computer_pick=='scissors':
        print("You Won!")
        user_wins+=1
        continue
    elif user_input=='scissors' and computer_pick=='paper':
        print("You won!")
        user_wins+=1
        continue
    elif user_input=='paper' and computer_pick=='rock':
        print("You won!")
        user_wins+=1
        continue
    else:
        print("You lost!")
        computer_wins+=1 
        
print("you won",user_wins,"times.")
print("computer won",computer_wins,"times.")
print("Good Bye") 
