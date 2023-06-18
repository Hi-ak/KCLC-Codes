from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "My first website"

@app.route("/<name>")
def welcome(name):
    name = name.capitalize()
    return "<h1>Welcome to kclc, " + name + "!</h1>"

if (__name__ == "__main__"):
    app.run()