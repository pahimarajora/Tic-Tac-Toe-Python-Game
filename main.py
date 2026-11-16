import tkinter as tk
from tkinter import messagebox
from game_logic import TicTacToe

# Create game object
game = TicTacToe()

# Create main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("450x650")
root.configure(bg="#1E293B")
root.resizable(False, False)

# Colors
BG_COLOR = "#1E293B"
BOX_COLOR = "#334155"
X_COLOR = "#38BDF8"
O_COLOR = "#F472B6"
TEXT_COLOR = "#FFFFFF"

# Score variables
x_score = 0
o_score = 0





# Heading
title_label = tk.Label(
    root,
    text="TIC TAC TOE",
    font=("Arial", 25, "bold"),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
title_label.pack(pady=20)

# Turn indicator
turn_label = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 16, "bold"),
    bg=BG_COLOR,
    fg=X_COLOR
)
turn_label.pack(pady=10)

# Scoreboard
score_label = tk.Label(
    root,
    text="Player X: 0       Player O: 0",
    font=("Arial", 13),
    bg=BG_COLOR,
    fg=TEXT_COLOR
)
score_label.pack(pady=15)






# Frame for game board
board_frame = tk.Frame(root, bg=BG_COLOR)
board_frame.pack(pady=5)

buttons = []

for i in range(9):

    button = tk.Button(
        board_frame,
        text="",
        font=("Arial", 28, "bold"),
        width=5,
        height=2,
        bg=BOX_COLOR,
        fg=TEXT_COLOR,
        activebackground="#475569",
        relief="flat",
        cursor="hand2"
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )

    buttons.append(button)






def update_score():
    score_label.config(
        text=f"Player X: {x_score}       Player O: {o_score}"
    )


def button_click(position):
    global x_score, o_score

    player = game.current_player

    if not game.make_move(position):
        return

    buttons[position].config(
        text=player,
        fg=X_COLOR if player == "X" else O_COLOR,
        state="disabled"
    )

    winner = game.check_winner()

    if winner:
        if winner == "X":
            x_score += 1
        else:
            o_score += 1

        update_score()

        turn_label.config(text=f"Player {winner} Wins!")

        messagebox.showinfo(
            "Game Over",
            f"Congratulations! Player {winner} wins!"
        )

        disable_board()
        return

    if game.check_draw():
       turn_label.config(text="It's a Draw!")

       disable_board()

       messagebox.showinfo(
        "Game Over",
        "The match is a draw!"
       )
       
       return

    game.switch_player()

    turn_label.config(
        text=f"Player {game.current_player}'s Turn",
        fg=X_COLOR if game.current_player == "X" else O_COLOR
    )


def disable_board():
    for button in buttons:
        button.config(state="disabled")





def restart_game():

    game.reset_game()

    for button in buttons:
        button.config(
            text="",
            state="normal",
            fg=TEXT_COLOR
        )

    turn_label.config(
        text="Player X's Turn",
        fg=X_COLOR
    )


restart_button = tk.Button(
    root,
    text="RESTART GAME",
    font=("Arial", 13, "bold"),
    bg="#0EA5E9",
    fg="white",
    activebackground="#0284C7",
    relief="flat",
    cursor="hand2",
    command=restart_game
)

restart_button.pack(pady=5)





# Connect each button to its click function
for i in range(9):
    buttons[i].config(
        command=lambda position=i: button_click(position)
    )

# Run application
root.mainloop()
