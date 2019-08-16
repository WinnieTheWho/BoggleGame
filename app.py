from boggle import Boggle
from flask import Flask, render_template, session


app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"

boggle_game = Boggle()
board = boggle_game.make_board()


@app.route("/")
def display_board():
    """Display the game board on home page"""

    return render_template("home.html", board=board)


@app.route('/board-route')
def board_route():
    """Set board in session"""

    session["board"] = board 
    return session["board"]
