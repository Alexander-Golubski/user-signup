from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

def is_empty():
    ### True if username, password, or verify password field is empty ###


def valid_pw():
    ### False if username password contains space, < 3 or > 20 char ###

def pw_match():
    ### True if passwords are the same ###

def valid_email():
    ### true if email has a single @, a single ., no spaces, and between 3 and 20 characters long ###
    

@app.route("/")
def index():
    return render_template('signup_form.html', title="Signup Form") #add more arguments here

@app.route("/welcome")
def welcome():
    return render_template('welcome.html', title="Welcome")

