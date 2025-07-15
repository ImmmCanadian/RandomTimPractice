import random


MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

ROWS=3
COLUMNS=3

SYMBOLS={
    "A":4,
    "B":8,
    "C":12,
    "D":16
}

SYMBOLS_VALUE={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def get_Slot_Machine_Spin(rows,columns,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        temp = [symbol]*symbol_count
        all_symbols = all_symbols + temp
    
    column = []
    temp=[]

    for i in range(columns*rows):
        value = random.choice(all_symbols)
        temp.append(value)
        if (i+1) % 3 == 0:
            column.append(temp)
            temp=[]
    
    return column

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

def check_Winnings(columns,lines,bet,values):
    winnings=0
    winning_Lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_Lines.append(line+1)

    return winnings,winning_Lines

def deposit():
    while True:
        money = input("How much would you like to deposit? ")
        if money.isdigit() and int(money) > 0:
            amount = int(money)
            break
        else:
            print("Please enter a valid number.")
    return amount

def get_Number_Of_Lines():
    while True:
        lines = input(f"Enter how many lines you would like to bet on (1-{MAX_LINES}): ")
        if lines.isdigit() and 1<= int(lines)<= MAX_LINES:
            lines = int(lines)
            break
        else:
            print("Please enter a valid number of lines.")
    return lines

def get_Bet():
    while True:
        bet = input(f"How much would you like to bet on each line (${MIN_BET}-${MAX_BET})?: ")
        if bet.isdigit() and MIN_BET<= int(bet)<= MAX_BET:
            bet = int(bet)
            break
        else:
            print("Please enter a valid bet amount.")
    return bet

def spin(balance):

    lines=get_Number_Of_Lines()
    while True:
        bet = get_Bet()
        if (lines*bet)>balance:
            print(f"You do not have enough to bet this amount. Your current balance is {balance}")
            check = input("Would you like to redeposit (Y/N)? ")
            if check.lower().strip() == "y":
                balance += deposit()
        else:
            break
    print(f"You are betting ${bet} on {lines} lines, for a total bet of {bet*lines}")
    balance -= bet*lines
    slot_Machine = get_Slot_Machine_Spin(ROWS,COLUMNS,SYMBOLS)
    print_slot_machine(slot_Machine)
    winnings,winning_lines = check_Winnings(slot_Machine,lines,bet,SYMBOLS_VALUE)
    balance += winnings
    if winnings > 0:
        print(f"You won ${winnings} on lines", *winning_lines)
    else:
        print(f"You lost! Better luck next spin")

    return balance



def main():
    print("Welcome to Noah's Slot Machine!")
    user_Balance = deposit()

    while True:
        user_Balance = spin(user_Balance)
        respin_Check = input("Please enter y if you would like to spin again or q if you would like to quit. ")
        if respin_Check.lower().strip() == "q":
            break
 
    print(f"You left with ${user_Balance}.")

main()