import tkinter as tk

# Main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.attributes("-fullscreen", True)  # Fullscreen for mobile feel
root.configure(bg="#121212")  # Dark mobile-friendly background

current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Colors
x_color = "#FF3B30"       # Red for X
o_color = "#007AFF"       # Blue for O
highlight_color = "#FFD700"  # Gold for winning line
button_bg = "#1E1E1E"        # Button background

# Check winner function
def check_winner():
    # Rows
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != "":
            return board[r][0], [(r, 0), (r, 1), (r, 2)]
    # Columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != "":
            return board[0][c], [(0, c), (1, c), (2, c)]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0], [(0, 0), (1, 1), (2, 2)]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2], [(0, 2), (1, 1), (2, 0)]
    # Tie
    if all(board[r][c] != "" for r in range(3) for c in range(3)):
        return "Tie", []
    return None, []

# Button click function
def click(r, c):
    global current_player
    if board[r][c] == "":
        board[r][c] = current_player
        color = x_color if current_player == "X" else o_color
        buttons[r][c].config(text=current_player, fg=color, font=("Arial Rounded MT Bold", 100, "bold"))
        winner, positions = check_winner()
        if winner:
            show_winner(winner, positions)
        else:
            current_player = "O" if current_player == "X" else "X"

# Show winner function
def show_winner(winner, positions):
    if winner == "Tie":
        message = "🤝 It's a Tie! 🤝"
    else:
        message = f"🎉 Congratulations Player {winner}! 🎉"
        # Highlight winning line
        for r, c in positions:
            buttons[r][c].config(bg=highlight_color)

    # Display message in center
    congrats_label = tk.Label(root, text=message, font=("Arial Rounded MT Bold", 40, "bold"),
                              fg="#00FF00", bg="#121212")
    congrats_label.place(relx=0.5, rely=0.5, anchor="center")

    # Disable all buttons
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(state="disabled")

# Exit button
exit_btn = tk.Button(root, text="EXIT", command=root.destroy,
                     font=("Arial Rounded MT Bold", 20), bg="#FF3B30", fg="white")
exit_btn.place(relx=0.95, rely=0.95, anchor="se")

# Create buttons grid
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(root, text="", font=("Arial Rounded MT Bold", 100, "bold"),
                                  width=5, height=2, bg=button_bg, fg="white",
                                  command=lambda r=r, c=c: click(r, c))
        buttons[r][c].grid(row=r, column=c, padx=20, pady=20)

# Make grid expand like mobile screen
for i in range(3):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
