from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# creating board
board = [" " for i in range(9)]

# checking for the winner (ONLY rows & columns)
def check_winner(player):
    winning_pos = [
        [0,1,2], [3,4,5], [6,7,8],   # rows
        [0,3,6], [1,4,7], [2,5,8]    # columns
    ]
    for positions in winning_pos:
        if board[positions[0]] == board[positions[1]] == board[positions[2]] == player:
            return True
    return False

# checking for draw
def check_draw():
    return " " not in board

curr_player = "X"

@app.route("/", methods=["GET", "POST"])
def index():
    global curr_player, board
    winner = None
    draw = False

    if request.method == "POST":
        if "reset" in request.form:
            board = [" " for i in range(9)]
            curr_player = "X"
            return redirect(url_for("index"))

        move = int(request.form["move"])

        if board[move] == " ":
            board[move] = curr_player

            if check_winner(curr_player):
                winner = curr_player
            elif check_draw():
                draw = True
            else:
                # switching the player (your logic)
                if curr_player == "X":
                    curr_player = "O"
                else:
                    curr_player = "X"

    return render_template("index.html",
                           board=board,
                           curr_player=curr_player,
                           winner=winner,
                           draw=draw)

if __name__ == "__main__":
    app.run(debug=True)
