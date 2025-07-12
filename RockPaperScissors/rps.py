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