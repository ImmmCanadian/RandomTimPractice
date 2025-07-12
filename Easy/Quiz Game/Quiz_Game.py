playerScore=0

print("Welcome to the quiz!")

play = input("Would you like to play? Yes or No")

if play.strip().lower() == "no":
    quit()

questionOne = input("Ok! First question, what is Spains capital city?")
 
if questionOne.strip().lower() == "madrid":
    print("Correct")
    playerScore += 1
else:
    print("Incorrect!")

questionTwo = input("Next question, what does CPU stand for?")
 
if questionTwo.strip().lower() == "central processing unit":
    print("Correct")
    playerScore += 1
else:
    print("Incorrect!")

print("Your total final score is " + str(playerScore) + " out of 2")
print("Thanks for playing!")

