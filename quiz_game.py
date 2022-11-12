print("Welcome to computer quiz game!")
playing = input("Do you want to play this game? ")

if playing.lower()!='yes':
    quit()

score =0
print("Let's start the game now!")
answer = input("What does cpu stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorret")

answer = input("What does gpu stand for? ").lower()
if answer == "graphical processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorret")

answer = input("What does ram stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorret")

answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorret")

print("You got "+str(score)+" correct answers.")
print("You got "+str(score/4*100)+"%.")