import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True

# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input 
def playerInput(board):
    global currentPlayer
    while True:
        try:
            inp = int(input("Select a spot 1-9: "))

            if inp < 1 or inp > 9:
                print("Please pick a number from 1 to 9.")
                continue

            if board[inp - 1] != "-":
                print("That spot is already taken. Try again.")
                continue

            board[inp - 1] = currentPlayer
            break  

        except ValueError:
            print("Please enter a valid number (1-9).")


# check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True
    return False


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board) or checkRow(board) or checkDiag(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False


# switch player
def switchPlayer():
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"


def computer(board):
    if currentPlayer == "O":
        while True:
            position = random.randint(0, 8)
            if board[position] == "-":
                board[position] = "O"
                break
        switchPlayer()


while gameRunning:
    printBoard(board)
    playerInput(board)

    checkIfWin(board)
    if not gameRunning:
        break

    checkIfTie(board)
    if not gameRunning:
        break

    switchPlayer()
    computer(board)

    checkIfWin(board)
    if not gameRunning:
        break

    checkIfTie(board)
