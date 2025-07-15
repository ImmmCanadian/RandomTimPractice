import random

def roll_Dice():
    rolled_Number = random.randint(1, 6)  
    return rolled_Number

def initialize_Game():
    while True:
        p_Count = input("Please select how many players you would like to play (2 to 4): ")
        if p_Count.isdigit():
            p_Count = int(p_Count)
            if 2 <= p_Count <= 4:
                break
            else:
                print("Please enter a valid amount of players (2-4)")
        else:
            print("Invalid, please enter a number")

    while True:
        max_Score = input("Please enter what you would like the max score to be: ")
        if max_Score.isdigit() and int(max_Score) > 0:
            break
        else:
            print("Invalid, please enter a number greater than 0")

    return int(p_Count), int(max_Score)

player_Count, max_Score = initialize_Game()
player_Scores = [0] * player_Count


while max(player_Scores) < max_Score:
    for player_Index in range(player_Count):  
        print(f"\nPlayer {player_Index + 1}'s turn!")
        print(f"Your total score is: {player_Scores[player_Index]}\n")
        current_Turn_Score = 0
        turn_Active = True
        
        while turn_Active:
            choice = input("Would you like to (r)oll or (h)old? ").lower()
            
            if choice == 'h':
                
                player_Scores[player_Index] += current_Turn_Score
                print(f"\nPlayer {player_Index + 1} holds. Total score: {player_Scores[player_Index]}")
                turn_Active = False
            elif choice == 'r':
                
                roll = roll_Dice()
                print(f"You rolled a {roll}!")
                
                if roll == 1:
                    print("Unlucky! You lose all points from this turn.")
                    current_Turn_Score = 0
                    turn_Active = False
                else:
                    current_Turn_Score += roll
                    print(f"Current turn score: {current_Turn_Score}")
                    
                    
                    if player_Scores[player_Index] + current_Turn_Score >= max_Score:
                        player_Scores[player_Index] += current_Turn_Score
                        break
            else:
                print("Invalid choice. Please enter 'r' to roll or 'h' to hold.")
        
        
        player_Scores[player_Index] += current_Turn_Score
        print(f"Player {player_Index + 1} total score: {player_Scores[player_Index]}")
        
        
        if player_Scores[player_Index] >= max_Score:
            break


winning_Score = max(player_Scores)
winning_Player = player_Scores.index(winning_Score) + 1
print(f"\nPlayer {winning_Player} wins with a score of {winning_Score}!")