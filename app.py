from flask import Flask
from flask import render_template
from flask import request, redirect
from model import gif_chooser
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/results", methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        sender_name = request.form["sender"]
        recipient_name = request.form["recipient"]
        message = request.form["message"]
        gif_type = request.form["gif_type"]       
        giphy_query = gif_chooser(gif_type)
    return render_template("results.html", sender=sender_name, recipient=recipient_name, message=message, query=giphy_query)

