import random
import time
import sys

class Board:
    def __init__(self):
        self.keys = []
        self.values = []
        self.hiddenValues = []
        self.board = {}
        self.hiddenBoard = {}
        self.gridSize = int(sys.argv[1])
        self.numOfPairs = (self.gridSize * self.gridSize) // 2
        self.letters = ''.join(chr(97 + i) for i in range(self.gridSize))
        self.initializeBoard()

    def initializeBoard(self):
        for i in range(0, self.gridSize):
            for char in self.letters:
                self.keys.append((char, i))

        if self.gridSize not in [2, 4, 6]:
            print("Invalid grid size.")
            sys.exit()

        while len(self.values) < len(self.keys):
            x = random.randint(0, self.numOfPairs - 1)
            if self.values.count(x) < 2:
                self.values.append(x)
            self.hiddenValues.append('x')


        self.board = dict(zip(self.keys, self.values))
        self.hiddenBoard = dict(zip(self.keys, self.hiddenValues))
        self.score = 0

    def displayBoard(self):
        header = "      " + " ".join(f"[ {char.upper()} ]" for char in self.letters)
        print(header)
        for i in range(self.gridSize):
            row = f"[ {i} ] " + "   ".join(f"{self.board.get((char, i), ' '):>3}" for char in self.letters)
            print(row)

    def displayHiddenBoard(self):
        header = "      " + " ".join(f"[ {char.upper()} ]" for char in self.letters)
        print(header)
        for i in range(self.gridSize):
            row = f"[ {i} ] " + "   ".join(f"{self.hiddenBoard.get((char, i), ' '):>3}" for char in self.letters)
            print(row)

    def displayHybrid(self, cell1, cell2):
        header = "      " + " ".join(f"[ {char.upper()} ]" for char in self.letters)
        print(header)
        for i in range(self.gridSize):
            row = f"[ {i} ] "
            for char in self.letters:
                if (char, i) == cell1 or (char, i) == cell2:
                    row += f"{self.board.get((char, i)):>3}   "
                else:
                    row += f"{self.hiddenBoard.get((char, i)):>3}   "
            print(row)



    def selectOneElement(self):
        while True:
            cell = input(f"Enter cell coordinates (ie. a0): ").lower()
            if len(cell) == 2 and cell[0] in self.letters and cell[1].isdigit() and -1 < int(cell[1]) < self.gridSize :
                cell = (cell[0], int(cell[1]))
                return cell
            print("Invalid input, please enter a valid cell coordinate: ")


    def selectTwoElements(self):
        cell1 = self.selectOneElement()
        cell2 = self.selectOneElement()
        return cell1, cell2

    def updateHiddenBoard(self, cell1, cell2):
            self.displayHybrid(cell1, cell2)
            time.sleep(2)
            if self.board[cell1] == self.board[cell2]:
                self.hiddenBoard[cell1] = self.board[cell1]
                self.hiddenBoard[cell2] = self.board[cell2]
            else:
                if self.hiddenBoard[cell1] is 'x':
                    self.hiddenBoard[cell1] = 'x'
                if self.hiddenBoard[cell2] is 'x':
                    self.hiddenBoard[cell2] = 'x'
            self.displayHiddenBoard()

    def updateHiddenBoardOneInput(self, cell1):
            self.hiddenBoard[cell1] = self.board[cell1]
            self.displayHiddenBoard



    def revealBoard(self):
        for i in range(self.gridSize):
            for char in self.letters:
                cell = (char, i)
                self.hiddenBoard[cell] = self.board[cell]

    def compareBoards(self):
        for i in range(0, self.gridSize):
            for char in self.letters:
                if (self.hiddenBoard.get((char, i)) != self.board.get((char, i))):
                    return False

        return True




