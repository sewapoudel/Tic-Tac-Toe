import tkinter as tk
from tkinter import messagebox

def winners():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="pink")
            buttons[combo[1]].config(bg="pink")
            buttons[combo[2]].config(bg="pink")
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()

def click(index):
    global game_over
    if buttons[index]["text"] == "" and not game_over:
        buttons[index]["text"] = current_player
        if check_winner():
            game_over = True
        else:
            player()

def player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

def check_winner():
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="pink")
            buttons[combo[1]].config(bg="pink")
            buttons[combo[2]].config(bg="pink")
            messagebox.showinfo("Tic Tac Toe", f"Player {buttons[combo[0]]['text']} wins!")
            return True
    return False

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i // 3, column=i % 3)

current_player = "X"
game_over = False

label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
