"""
tiktaktoe.py: druhý projekt do Engeto Online Python Akademie
author: David Sláma
email: cimka1@seznam.cz
discord: cimka1#2497
"""

print("Welcome to Tic Tac Toe\n============================================\nGAME RULES:\nEach player can place one mark (or stone)\nper turn on the 3x3 grid. The WINNER is\nwho succeeds in placing three of their\nmarks in a:\n\t* horizontal,\n\t* vertical or\n\t* diagonal row\n============================================\nLet's start the game")

#vykresluje hrací plochu se stavem hry

def hraci_pole(board):
    print("+---+---+---+")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n+---+---+---+")

# vyzve hráče k zadání svého tahu

def input_hrace(player):
    print("Player", player,"| Please enter your move number", end=" ")
    move = input()
    return move

# umisťuje značku (O nebo X) na hrací na zvolenou pozici 

def place_marker(board, marker, position):
    row, col = (position - 1) // 3, (position -1) % 3
    if board[row][col] == " ":
     board[row][col] = marker
     return True
    else:
        print("This position is already occupied.")
        return False
    
def check_vyhry(board, marker):
    # Kontrola, zda některý hrář vyhrál
    for i in range(3):
        if board[i] == [marker, marker, marker]:
            return True
        if [board[j][i] for j in range(3)] == [marker, marker, marker]:
            return True
        if [board[i][i] for i in range(3)] == [marker, marker, marker]:
            return True
        if [board[i][2 - i] for i in range(3)] == [marker, marker, marker]:
            return True
        return False
    
board = [[" " for _ in range(3)] for _ in range(3)]
player = "O"

while True:
    hraci_pole(board)
    move = input_hrace(player)
    try:
        move = int(move)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if move < 1 or move > 9:
        print("Invalid move. Please choose a number between 1 and 9.")
        continue
    if not place_marker(board, player, move):
        continue
    if check_vyhry(board, player):
        hraci_pole(board)
        print("Congratulations, the player", player, "WON!")
        break
    if all(cell != " " for row in board for cell in row):
        hraci_pole(board)
        print("It's a DRAW.")
        break
    player = "X" if player == "O" else "O"