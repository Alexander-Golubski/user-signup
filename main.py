from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

def is_empty(u_input):
    ### True if username, password, or verify password field is empty ###
    return u_input == ""

def valid_un_pw(u_input):
    ### False if username or password contains space, < 3 or > 20 char ###
    if len(u_input) > 20 or len(u_input) < 3:
        return False
    if " " in u_input:
        return False
    else:
        return True

def pw_match(pw, v_pw):
    ### True if passwords are the same ###
    return pw == v_pw

def valid_email(u_input):
    ### true if email has a single @, a single ., no spaces, and 
    # between 3 and 20 characters long ###
    if "@" not in u_input:
        return False
    if "." not in u_input:
        return False
    if " " in u_input:
        return False
    if 3 > len(u_input) > 20:
        return False
    else:
        return True

@app.route("/user-signup", methods=["POST"])
def index():

    username = request.form["username"]
    password = request.form["password"]
    verify_pw = request.form["verify_pw"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_pw_error = ""
    email_error = ""

    if is_empty(username):
        username_error = "Please enter a username."
    else:
        if not valid_un_pw(username):
            username_error = "Username must be between 3 and 20 characters and not contain spaces."

    if is_empty(password):
        password_error = "Please enter a password."
    else:
        if not valid_un_pw(password):
            password_error = "Password must be between 3 and 20 characters and not contain spaces."
            password = ""
            verify_pw = ""

    if is_empty(verify_pw):
        verify_pw_error = "Please verify password."
    else:
        if not pw_match(password, verify_pw):
            verify_pw_error = "Passwords do not match."
            password = ""
            verify_pw = ""

    if not is_empty(email):
        if not valid_email(email):
            email_error = "Email must be between 3 and 20 characters long and contain a single \"@\", a single \".\", and no spaces."

    if not username_error and not password_error and not verify_pw_error and not email_error:
        return render_template('welcome.html', title="Welcome", username=username)
    else:
        return render_template('index.html', title="Signup Form", username_error=username_error, password_error=password_error, verify_pw_error=verify_pw_error, email_error=email_error, username=username, password=password, verify_pw=verify_pw, email=email)

@app.route("/user-signup")
def display_user_signup():
    return render_template('index.html', title="Signup Form")

if __name__ == "__main__":
    app.run()