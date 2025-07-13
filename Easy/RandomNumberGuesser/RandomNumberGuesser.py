import random

numberGuessed = False

print("Welcome to the random number guesser game!")

play = input("Would you like to play? ")

if play.strip().lower() == "no":
    quit()

numRange = 10
randomNumber = random.randint(1,numRange)
guessCount=0

print("We have generated a random number from 1 to "+str(numRange)+", good luck!")

while numberGuessed == False:
    guess = input("Guess a number! ")
    if int(guess) == randomNumber:
        numberGuessed = True
        guessCount += 1
        print("You guessed the correct number which was "+str(guess)+"!")
        print("It took you "+str(guessCount)+" tries.")
    elif int(guess) < randomNumber:
        print("Your guess is too low!")
        guessCount += 1
    else:
        print("Your guess is too high!")
        guessCount += 1
    
    if guessCount > numRange:
        userQuit = input("Would you like to stop playing? ")
        if userQuit.strip().lower() == "yes":
            quit()

