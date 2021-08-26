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


#@app.route('/contactpage', methods=["GET", "POST"])
#def get_contact():
#    form=ContactForm
#    if request.method == "POST":
#        name = request.form["name"]
#        email = request.form["email"]
#        message = request.form["message"]
#        res = pd.DataFrame({'name': name, 'email': email, 'message':message}, index=[0])
#        res.to_csv('./contactmemessage.csv')
#        return render_template('templates\contactpage.html', form=form)
#    else:
#        render_template('templates\contactpage.html', form=form)



if __name__=='__main__':
    app.run(debug=True)