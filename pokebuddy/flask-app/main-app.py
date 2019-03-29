from flask import Flask, request, render_template, url_for
import os
import Utils.classify

# To run this, type in terminal: `export FLASK_APP=main-app.py` (or whatever name of file is)
# Then type flask run
# Additional options: Use `flask run --host=0.0.0.0` or any other host you want to specify.
# additionally you can add `--port=4000` after the previous command to run on port 4000
app = Flask(__name__)

# What to do when user goes to default route
@app.route('/')
def show_page(): # The function name can be anything

    # You can just return default text 
    # return "Hello. Welcome to default page"

    # You'd rather return a rendered html file
    return render_template("index.html") 

# Just another route - this will be 0.0.0.0:4000/other
@app.route('/classify', methods=['POST'])
def show_another():
    doc = request.form['inputText']
    # number = str(Utils.classify.classify(doc))
    # number = number.zfill(4) + ".png"
    # return render_template("video.html", number=number)
    numbers = [str(num[0]).zfill(4)+".png" for num in Utils.classify.classify(doc)]
    return render_template("video.html", n1=numbers[0], n2=numbers[1], n3=numbers[2])