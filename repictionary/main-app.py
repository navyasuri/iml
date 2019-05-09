from flask import Flask, request, render_template, url_for
import os, subprocess
# import utils.(filename)

# To run this, type in terminal: `export FLASK_APP=main.py` (or whatever name of file is)
# Then type flask run
# Additional options: Use `flask run --host=0.0.0.0` or any other host you want to specify.
# additionally you can add `--port=4000` after the previous command to run on port 4000
app = Flask(__name__)

player1 = "Player 1"
player2 = "Player 2"
rounds = 0
player1_score = 0
player2_score = 0

current_player = player1

# What to do when user goes to default route
@app.route('/')
def show_page(): # The function name can be anything

    # You can just return default text 
    # return "Hello. Welcome to default page"

    # You'd rather return a rendered html file
    return render_template("index.html") 

# Just another route - this will be 0.0.0.0:4000/other
@app.route('/game')
def show_another():

    if current_player==player1:
        return render_template("game.html", player1=player1, player2=player2)
    elif current_player==player2:
        return render_template("game.html", player1=player1, player2=player2)