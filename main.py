import random, time, copy
from termcolor import cprint


#Introduction
print()
cprint('=============================', 'red')
cprint('Welcome to MineSweeper v.3.0!', 'cyan')
cprint('=============================', 'red')
print()
print('Excited to declare version 3.0 of MineSweeper as almost fully functional!')


#Reset game
def reset():
    print('''
MAIN MENU
=========

-> For instructions on how to play, type 'I'
-> To play immediately, type 'P'
''')

    choice = input("Type here: ").upper()

    if choice == "I":
        print(open("Instructions.txt", "r").read())

        input("Press [enter] when ready to play. ")

    elif choice != "P":
        reset()





#The solution grid.
    b = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]



    for n in range (0, 10):
        placeBomb(b)

    
    for r in range(0, 9):
        for c in range(0, 9):
            value = l(r, c, b)
            if value == "*":
                updateValues(r, c, b)

#Sets the variable k to a grid of blank spaces, because nothing is yet known about the grid.
    k = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    printBoard(k)
    #Start timer
    startTime = time.time()
    #The game begins!
    play(b, k, startTime)




#Places a marker in the given location.
def marker(r, c, k):
    k[r][c] = '⚐'
    printBoard(k)


def choose(b, k, startTime):
    #Variables
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ,'i']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    #Loop in case of invalid entry
    while True:
        chosen = input('Choose a square (eg. E4) or place a marker (eg. mE4): ').lower()

    #Checks for valid square.
        if len(chosen) == 3 and chosen[0] == 'm' and chosen[1] in letters and chosen[2] in numbers:
            c, r = (ord(chosen[1]))-97, int(chosen[2])
            marker(r, c, k)
            play(b, k, startTime)
            break
        elif len(chosen) == 2 and chosen[0] in letters and chosen[1] in numbers:
            return (ord(chosen[0]))-97, int(chosen[1])
        else:
            choose(b, k, startTime)



#Checks known grid for 0s.
def checkZeros(k, b, r, c):
    oldGrid = copy.deepcopy(k)
    zeroProcedure(r, c, k, b)
    if oldGrid == k:
        return
    while True:
        oldGrid = copy.deepcopy(k)
        for x in range (9):
            for y in range (9):
                if l(x, y, k) == 0:
                    zeroProcedure(x, y, k, b)
        if oldGrid == k:
            return


#When a zero is found, all the squares around it are opened.
def zeroProcedure(r, c, k, b):

    #Row above
    if r-1 > -1:
        row = k[r-1]
        if c-1 > -1: row[c-1] = l(r-1, c-1, b)
        row[c] = l(r-1, c, b)
        if 9 > c+1: row[c+1] = l(r-1, c+1, b)

    #Same row
    row = k[r]
    if c-1 > -1: row[c-1] = l(r, c-1, b)
    if 9 > c+1: row[c+1] = l(r, c+1, b)

    #Row below
    if 9 > r+1:
        row = k[r+1]
        if c-1 > -1: row[c-1] = l(r+1, c-1, b)
        row[c] = l(r+1, c, b)
        if 9 > c+1: row[c+1] = l(r+1, c+1, b)






def play(b, k, startTime):
    #player chooses square
    c, r = choose(b, k, startTime)

    #Gets the value at that location
    v = l(r, c, b)

    #If you hit a bomb, it ends the game.
    if v == '*':
        printBoard(b)
        print('You Lose!')
        #Print timer result.
        print('Time: ' + str(round(time.time() - startTime)) + 's')
        #Offer to play again.
        playAgain = input('Play again? (Y/N): ').lower()
        if playAgain == 'y':
            reset()
        else:
            quit()

    #Puts that value into the known grid (k).
    k[r][c] = v

    #Runs checkZeros() if that value is a 0.
    if v == 0:
        checkZeros(k, b, r, c)
    printBoard(k)

    #Checks to see if you have won.
    squaresLeft = 0
    for x in range (0, 9):
        row = k[x]
        squaresLeft += row.count(' ')
        squaresLeft += row.count('⚐')


    if squaresLeft == 10:
        printBoard(b)
        print('You win!')
        #Print timer result.
        print('Time: ' + str(round(time.time() - startTime)) + 's')
        #Offer to play again.
        playAgain = input('Play again? (Y/N): ')
        playAgain = playAgain.lower()
        if playAgain == 'y':
            reset()
        else:
                quit()

    play(b, k, startTime)






#Places the bomb in a random location
def placeBomb(b):
    r = random.randint(0, 8)
    c = random.randint(0, 8)
    #Checks if there is bomb in that location. If not it puts it there.
    currentRow = b[r]
    if not currentRow[c] == "*":
        currentRow[c] = "*"
    else:
        placeBomb(b)


#Adds 1 to all of the squares around a bomb.
def updateValues(rn, c, b):

    #Row above.
    if rn-1 > -1:
        r = b[rn-1]
        
        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1

    #Same row.    
    r = b[rn]

    if c-1 > -1:
        if not r[c-1] == '*':
            r[c-1] += 1

    if 9 > c+1:
        if not r[c+1] == '*':
            r[c+1] += 1

    #Row below.
    if 9 > rn+1:
        r = b[rn+1]

        if c-1 > -1:
            if not r[c-1] == '*':
                r[c-1] += 1

        if not r[c] == '*':
            r[c] += 1

        if 9 > c+1:
            if not r[c+1] == '*':
                r[c+1] += 1



#Gets the value of a coordinate on the grid.
def l(r, c, b):
    return b[r][c]


def printBoard(b):
    print('    A   B   C   D   E   F   G   H   I')
    print('  ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗')
    for r in range (0, 9):
        print(r,'║',l(r,0,b),'║',l(r,1,b),'║',l(r,2,b),'║',l(r,3,b),'║',l(r,4,b),'║',l(r,5,b),'║',l(r,6,b),'║',l(r,7,b),'║',l(r,8,b),'║')
        if not r == 8:
            print('  ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣')

    print('  ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝')





reset()