import random
print("Welcome to number guessing game!")

upper_bound = input("Enter a upper bound for the number: ")
if upper_bound.isdigit():
    ub = int(upper_bound)
    if ub <=0:
        print("Number must be greater than 0")
        quit()
else:
    print("It must be a number")
    quit()

number_of_guess = 0 
random_number = random.randint(0,ub)
while True:
    number_of_guess+=1
    guessed_num = input("Guess a number: ")
    if guessed_num.isdigit():
        guessed_num =  int(guessed_num)
    else:
        print("Guess a number atleast")
        continue
    if guessed_num == random_number:
        print("You got it")
        break
    elif guessed_num > random_number:
        print("You were above it")
    else:
        print("You were below it")
    

print("You guessed it in ", number_of_guess, "guesses")