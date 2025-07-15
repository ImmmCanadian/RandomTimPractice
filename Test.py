import random

ROWS=3
COLUMNS=3

SYMBOLS={
    "A":4,
    "B":8,
    "C":12,
    "D":16
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

print(get_Slot_Machine_Spin(ROWS,COLUMNS,SYMBOLS))

