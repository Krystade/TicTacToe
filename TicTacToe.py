def add_x(location):
    board[location] = "X"

def add_o(location):
    board[location] = "O"

def did_win(mark):
    for i in range(3):
        if board[3*i] == mark and board[i*3 + 1] == mark and board[i*3 + 2] == mark:
            return True
    for i in range(3):
        if board[i+0] == mark and board[i+3] == mark and board[i+6] == mark:
            return True
        
    if board[0] == mark and board[4] == mark and board[8] == mark:
        return True
    if board[2] == mark and board[4] == mark and board[6] == mark:
        return True
    return False

def print_board():
    print("_________________________________________________")
    print()
    print("|\t" + board[0] + "\t|\t" + board[1] + "\t|\t" + board[2] + "\t|")
    print()
    print("_________________________________________________")
    print()
    print("|\t" + board[3] + "\t|\t" + board[4] + "\t|\t" + board[5] + "\t|")
    print()
    print("_________________________________________________")
    print()
    print("|\t" + board[6] + "\t|\t" + board[7] + "\t|\t" + board[8] + "\t|")
    print()
    print("_________________________________________________")
    print()

board = ["", "", "", "", "", "", "", "", ""]
print_board()
done = False

while not done:
    add_x(int(input("Where would you like to place the X? ")))
    print_board()
    if did_win("X"):
        print("X wins!")
        print(board)
        break
    add_o(int(input("Where would you like to place the O? ")))
    print_board()
    if did_win("O"):
        print("O wins!")
        print(board)
        break
