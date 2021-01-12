import itertools

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

higher = []
lower = []
draw = []
suit = []
vals = list(range(2,14))
suits = ['S', 'C', 'H', 'D']

deck = list(itertools.product(vals, suits))

ans = 'Y'
skip = 'Y'

print('Please input in this format - i.e. For 7 of Spades type 7s and King of Hearts type kh')

x = input('What is the face up card? ').upper()

while ans == 'Y':

    if skip == 'N':
        x = input('What is the face up card? ').upper()
    else:
        pass

    y = [x[0], x[1]]
    if x[0] + x[1] == '10':
        y[0] = 10
    elif y[0] == 'J':
        y[0] = 11
    elif y[0] == 'Q':
        y[0] = 12
    elif y[0] == 'K':
        y[0] = 13
    elif y[0] == 'A':
        y[0] = 14
    else:
        y[0] = int(y[0])

    if x[1] == '0':
        a = (y[0],x[2])
    else:
        a = (y[0],y[1])

    
    if a[1] == 'S':
        suit.append('♠')
    elif a[1] == 'C':
        suit.append('♣')
    elif a[1] == 'H':
        suit.append('♥')
    elif a[1] == 'D':
        suit.append('♦')
    
    if x[1] == '0':
        print(f'Face up card is {y[0]} {suit[0]} ')
    else:
        print(f'Face up card is {x[0]} {suit[0]} ')
    
    if a not in deck:
        x = input('This card has been used. Please enter a new card! ').upper()
        y = [x[0], x[1]]
        if x[0] + x[1] == '10':
            y[0] = 10
        elif y[0] == 'J':
            y[0] = 11
        elif y[0] == 'Q':
            y[0] = 12
        elif y[0] == 'K':
            y[0] = 13
        elif y[0] == 'A':
            y[0] = 14
        else:
            y[0] = int(y[0])

        if x[1] == '0':
            a = (y[0],x[2])
        else:
            a = (y[0],y[1])
        
        
        if a[1] == 'S':
            suit.append('♠')
        elif a[1] == 'C':
            suit.append('♣')
        elif a[1] == 'H':
            suit.append('♥')
        elif a[1] == 'D':
            suit.append('♦')

        if x[1] == '0':
            print(f'Face up card is {y[0]} {suit[0]} ')
        else:
            print(f'Face up card is {x[0]} {suit[0]} ')
    else:
        pass
    
    deck.remove(a)
    for index in deck:
        if index[0] == a[0]:
            draw.append(index[0])
    for index in deck:
        if index[0] > a[0]:
            higher.append(index[0])
    for index in deck:
        if index[0] < a[0]:
            lower.append(index[0])

    high_problty = len(higher) / len(deck) * 100
    low_problty = len(lower) / len(deck) * 100
    draw_problty = len(draw) / len(deck) * 100

    print(f'\nChance to be Higher: {high_problty:.2f}' + ' %')
    print(f'Chance to be Lower: {low_problty:.2f}' + ' %')
    print(f'Chance to be a Draw: {draw_problty:.2f}' + ' %')
    
    if high_problty > low_problty:
        print('Choose Higher!')
    elif low_problty > high_problty:
        print('Choose Lower!')

    x = input('\nDid you Win, Draw or Lose? (Enter next card if Win/Draw and N for Lose) ').upper()
    
    if x != 'N':
        ans = 'Y'
        skip = 'Y'
        higher.clear()
        lower.clear()
        draw.clear()
        suit.clear()
        y.clear()
    elif x == 'N':
        deck.clear()
        higher.clear()
        lower.clear()
        draw.clear()
        suit.clear()
        y.clear()
        vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        suits = ['S', 'C', 'H', 'D']
        deck = list(itertools.product(vals, suits))

        ans = input('\nYou Lost! Noob! Play again? (Y to play again and N to quit) ').upper()
        while ans != 'Y' or ans != 'N':
            x = input('You made a Typo! Please re-enter card. ').upper()
        else:
            pass
        skip = 'N'
    else:
        break
