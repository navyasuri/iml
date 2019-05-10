from flask import Flask, request, render_template, url_for, redirect
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
current_round = 0
player1_score = 0
player2_score = 0

current_player = player1
turns = ['desc', 'guess']
turn = 0

# What to do when user goes to default route
@app.route('/')
def show_page(): # The function name can be anything

    # You can just return default text 
    # return "Hello. Welcome to default page"

    # You'd rather return a rendered html file
    return render_template("landing.html") 

@app.route('/gamesetup')
def game_setup():
    # If GET method, return the page
    # If POST method, return the game route with player 1 loaded
    # In POST also set global variables from request form
    # return redirect(url_for('game'))
    return render_template('gameops.html')

@app.route('/game',  methods=['POST'])
def eval_and_display():
    # If we come from GameOps, set our parameters accordingly
    from_gameops, from_desc = False
    try:
        ops = request.form['fromops']
        from_gameops = True
    except:
        pass
    
    if from_gameops:
        player1 = request.form['p1name']
        player2 = request.form['p2name']
        current_player = player1

        # Display the player1 caption page
        return_page = "desc.html"
        return render_template(return_page, player=current_player)

    # If we come from desc, then we should generate image
    try:
        desc = request.form['fromdesc']
        from_desc = True
    except:
        pass
    
    if from_desc:
        caption = request.form['caption']
        # caption player is the one who provided caption to generate image
        caption_player = request.form['d_player']
        next_player = player1 if caption_player==player2 else player2
        # Generate image and copy to static folder

    # Read form and decide parameters, path and image



    

@app.route('/result')
def result_and_next():

    return render_template(next_page, next_player)

@app.route('/score')
def scoring():

    return render_template("scoring.html", player1score=player2_score, player2_score=player2_score)