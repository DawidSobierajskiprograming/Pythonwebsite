from os import remove
import re
from flask import Flask, render_template, url_for, redirect, request
from flask.wrappers import Request
from forms import ContactForm
import pandas as pd


app = Flask(__name__)
app.secret_key = "somethingorother"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/notready")
def notready():
    return render_template("sorrynotready.html")

@app.route("/contact")
def contact():
    return render_template("contactpage.html")

if __name__=='__main__':
    app.run(debug=True)