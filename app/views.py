from app import app
from flask import render_template

@app.route("/")
def index():
    user = {"name": "acezio", "nickname": "whatever"}
    color_of_fruit = [
        {"name": "apple", "color": "red"},
        {"name": "banana", "color": "yellow"},
        {"name": "watermelon", "color": "green"},
    ]
    return render_template("index.html",
                           user=user,
                           fruitlist=color_of_fruit)