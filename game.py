import grid
import sys
import os
import time

def clear():
       os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print('''
    ---------------------
    |    Brain Buster   |
    --------------------- \n''')
    #grid.Board.displayBoard(board)
    grid.Board.displayHiddenBoard(board)
    print("\nGuess counter: ", numOfGuesses)
    print('''
1. Let me select two elements
2. Uncover one element for me
3. I give up - reveal the grid
4. New game
5. Exit
''')

def selectElements(board):
    grid.Board.displayHiddenBoard(board)
    global numOfGuesses
    cell1, cell2 = grid.Board.selectTwoElements(board)
    grid.Board.updateHiddenBoard(board, cell1, cell2)

    numOfGuesses += 1

    if (grid.Board.compareBoards(board)):
        score = ((grid.Board.board.gridSize / 2) / numOfGuesses) * 100

def uncoverOne(board):
    global numOfGuesses
    cell1 = grid.Board.selectOneElement(board)
    grid.Board.updateHiddenBoardOneInput(board, cell1)
    numOfGuesses += 2

def reveal(board):
    return grid.Board.revealBoard(board)

def newGame():
    print("Starting a new game!")
    return grid.Board()

def exit():
    print("Thank you for playing!")
    sys.exit()

choice  = -1
numOfGuesses = 0
board = grid.Board()
clear()

menu()

while (0 < choice < 6):
    choice = int(input("Select: "))

while (choice != 5):
    clear()
    match choice:
        case 1:
            selectElements(board)
        case 2:
            uncoverOne(board)
        case 3:
            reveal(board)
        case 4:
            board = newGame()
            #score = 0

    clear()
    #if grid.Board.compareBoards(board):
        #print("Congratulations, you won! \nYou scored: ", score, "\nIf you would like to play again, chooce option 4.")

    menu()

    choice = int(input("Select: "))


exit()
