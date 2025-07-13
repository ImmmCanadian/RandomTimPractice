import random

def rps(userChoice,computerChoice):
    if userChoice == "rock" and computerChoice == "scissors":
        print("You won this round!")
        return 1
    elif userChoice == "rock" and computerChoice == "rock":
        print("You tied this round!")
        return 0
    elif userChoice == "rock" and computerChoice == "paper":
        print("You lost this round!")
        return -1
    
    if userChoice == "paper" and computerChoice == "rock":
        print("You won this round!")
        return 1
    elif userChoice == "paper" and computerChoice == "paper":
        print("You tied this round!")
        return 0
    elif userChoice == "paper" and computerChoice == "scissors":
        print("You lost this round!")
        return -1
    
    if userChoice == "scissors" and computerChoice == "paper":
        print("You won this round!")
        return 1
    elif userChoice == "scissors" and computerChoice == "scissors":
        print("You tied this round!")
        return 0
    elif userChoice == "scissors" and computerChoice == "rock":
        print("You lost this round!")
        return -1

choices= ["rock","paper","scissors"]

print("Hi Welcome to Rock Paper Scissors!")

roundsFlag= False
round=0
humanWins = 0
computerWins=0

while roundsFlag == False:
    rounds=input("Please input how many rounds you want it to be best out of: ")
    if (int(rounds)%2 == 0):
        print("Please enter a odd amount of rounds!")
    else:
        round=rounds
        roundsFlag=True

print("This match will be a best of "+str(round)+"!")

i = 0

while i < int(round):
    userChoice = input("Choose rock paper or scissors! ")
    userChoice.strip().lower()

    if userChoice not in choices:
        continue
    
    computerChoice = choices[random.randint(0,2)]

    result = rps(userChoice,computerChoice)

    if result == 1:
        humanWins += 1
    elif result == -1:
        computerWins += 1
    else:
        i -= 1
    i += 1

if humanWins > computerWins: print("You won!")
else: print("You lost!")

    





