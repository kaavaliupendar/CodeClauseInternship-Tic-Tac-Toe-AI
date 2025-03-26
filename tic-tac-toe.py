import tkinter as tk
import tkinter.messagebox
board = [' ' for x in range(10)]

def reset():
    global board, b, states, player, stop_game
    board = [' ' for x in range(10)]

    states = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            b[i][j]["text"] = ' '
            b[i][j]["bg"] = "powder blue"
    player = "X"
    stop_game = False


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def computerPlay(r, c, comp_pos):
    global player



    if player == 'O' and states[r][c] == 0 and stop_game == False:
        board[comp_pos] = 'O'
        b[r][c]["text"] = "O"
        states[r][c] = 'O'
        player = 'X'
        check_play = check_for_winner()
        if check_play == 'X':
            tkinter.messagebox.showinfo("Result", "Congratulation, you won!")
            return
        elif check_play == 'O':
            tkinter.messagebox.showinfo("Result", "Opps, the computer won!")
            return


def callback(r, c):
    global player
    pos = int()

    if player == 'X' and states[r][c] == 0 and stop_game == False:
        if r == 0:
            pos = c + 1
        elif r == 1:
            pos = c + 4
        elif r == 2:
            pos = c + 7
        b[r][c]["text"] = "X"
        board[pos] = 'X'
        states[r][c] = 'X'
        player = 'O'
        check_play = check_for_winner()

        if check_play == 'X':
            tkinter.messagebox.showinfo("Result", "Congratulation, you won!")
            return
        elif check_play == 'O':
            tkinter.messagebox.showinfo("Result", "Opps, the computer won!")
            return


        if isBoardFull(board) == False:
            comp_pos = computerMove()
            if 1 <= comp_pos <= 3:
                r = 0
                c = comp_pos -1
            elif 4 <= comp_pos <= 6:
                r = 1
                c = comp_pos - 4
            elif 7 <= comp_pos <= 9:
                r = 2
                c = comp_pos - 7
            computerPlay(r, c, comp_pos)


        else:
                tkinter.messagebox.showinfo("Result", "Phew, it is a tie game!")






def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            check_play = states[i][0]
            b[i][0].configure(bg="grey")
            b[i][1].configure(bg="grey")
            b[i][2].configure(bg="grey")
            stop_game = True
            return check_play



    for i in range(3):
        if states[0][i] == states[1][i] == states[2][i] != 0:
            check_play = states[0][i]
            b[0][i].configure(bg="grey")
            b[1][i].configure(bg="grey")
            b[2][i].configure(bg="grey")
            stop_game = True
            return check_play


    for i in range(3):
        if states[0][0] == states[1][1] == states[2][2] != 0:
            check_play = states[0][0]
            b[0][0].configure(bg="grey")
            b[1][1].configure(bg="grey")
            b[2][2].configure(bg="grey")
            stop_game = True
            return check_play


    for i in range(3):
        if states[2][0] == states[1][1] == states[0][2] != 0:
            check_play = states[2][0]
            b[2][0].configure(bg="grey")
            b[1][1].configure(bg="grey")
            b[0][2].configure(bg="grey")
            stop_game = True
            return check_play




root = tk.Tk()
root.title("Tic-Tac-Toe with AI")

b = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

states = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]




for i in range(3):
    for j in range(3):
        b[i][j] = tk.Button(font=("Arial", 60), width=4, bg="powder blue", command=lambda r=i, c=j: callback(r,c))
        b[i][j].grid(row=i, column=j)

new_game = tk.Button(text="New Game", font=("Arial", 15), bg="grey", command=reset)
new_game.grid(row=3, column=1)

player = 'X'
stop_game = False

tk.mainloop()