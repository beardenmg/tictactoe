import tkinter as tk
from tkinter import messagebox
import random

# initialize main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# game board state
board = [" " for _ in range(9)]
buttons = []

# check for win
def check_win(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# check for tie
def check_tie():
    return " " not in board

def reset_game():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn["text"] = " "

def game_over(message):
    # ask the player if they want to play again
    if messagebox.askyesno("Game Over", message + "\nPlay again?"):
        reset_game()
    else:
        root.destroy()

# AI move (random)
def ai_move():
    empty_spots = [i for i, spot in enumerate(board) if spot == " "]
    if empty_spots:
        move = random.choice(empty_spots)
        board[move] = "O"
        buttons[move]["text"] = "O"
        if check_win("O"):
            game_over("You lose!")
        elif check_tie():
            game_over("It's a tie!")

# handle player click
def on_click(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i]["text"] = "X"
        if check_win("X"):
            game_over("You win!")
        elif check_tie():
            game_over("It's a tie!")
        else:
            ai_move()

# create buttons
for i in range(9):
    btn = tk.Button(root, text=" ", font=("Arial", 40), width=5, height=2, command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()