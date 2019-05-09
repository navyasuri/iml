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
turns = ['guess', 'desc']
turn = 0

# What to do when user goes to default route
@app.route('/')
def show_page(): # The function name can be anything

    # You can just return default text 
    # return "Hello. Welcome to default page"

    # You'd rather return a rendered html file
    return render_template("index.html") 

@app.route('/game-setup', methods=['GET', 'POST'])
def game_setup():
    # If GET method, return the page
    # If POST method, return the game route with player 1 loaded
    # In POST also set global variables from request form
    return redirect(url_for('game'))

@app.route('/game')
def eval_and_display():
    # Submit with parameters in the request form

    # Read form and decide parameters, path and image



    return_page = turns[turn]+".html"
    return render_template(render_page, player=current_player, next_turn=turns[turn-1])

@app.route('result')
def result_and_next():

    return render_template(next_page, next_player)

@app.route('/score')
def scoring():

    return render_template("scoring.html", player1score=player2_score, player2_score=player2_score)