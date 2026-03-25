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

# AI move (random)
def ai_move():
    empty_spots = [i for i, spot in enumerate(board) if spot == " "]
    if empty_spots:
        move = random.choice(empty_spots)
        board[move] = "O"
        buttons[move]["text"] = "O"
        if check_win("O"):
            tk.messagebox.showinfo("Game Over", "You lose!")
            root.quit()
        elif check_tie():
            tk.messagebox.showinfo("Game Over", "It's a tie!")
            root.quit()

# handle player click
def on_click(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i]["text"] = "X"
        if check_win("X"):
            tk.messagebox.showinfo("Game Over", "You win!")
            root.quit()
        elif check_tie():
            tk.messagebox.showinfo("Game Over", "It's a tie!")
            root.quit()
        else:
            ai_move()

# create buttons
for i in range(9):
    btn = tk.Button(root, text=" ", font=("Times New Roman", 40), width=5, height=2, command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)
    
root.mainloop()