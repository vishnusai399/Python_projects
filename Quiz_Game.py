print("welcome to the quiz")
playing= input("do you want to play quiz? ")

if playing.lower()!="yes":
    quit()
print("okay! let's play the game :)")

score=0

answer =input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer =input("what does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
answer =input("what does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")
    
answer =input("what does PSU stands for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("you got " + str(score) + "questions correct")
print("you got" + str((score/4)*100) +" %")

