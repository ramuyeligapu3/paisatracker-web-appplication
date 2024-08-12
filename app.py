import os
from cs50 import SQL
from flask import Flask, flash, render_template, redirect, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, send_otp, generate_otp

# Initialize the database
db = SQL("sqlite:///expenses.db")

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'admz lxwo nsox dwqb'

# Enable template auto-reload
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use the filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Global variables to store the user's email and OTP
otp_global = ""
user_email_global = ""

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/report")
def report():
    """Generate and display reports based on user-selected criteria"""
    report_type = request.args.get('type')

    # Query database for different report types
    if report_type == 'last_7_days':
        query = db.execute("SELECT * FROM expenses WHERE date >= date('now','-7 days') AND user_id=?", session["user_id"])
        income = db.execute("SELECT SUM(amount) FROM expenses WHERE date >= date('now','-7 days') AND category='income'AND user_id=?", session["user_id"])
        expense = db.execute("SELECT SUM(amount) FROM expenses WHERE date >= date('now','-7 days') AND category='expense'AND user_id=?", session["user_id"])
    elif report_type == 'this_month':
        query = db.execute("SELECT * FROM expenses WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now') AND user_id=?", session["user_id"])
        income = db.execute("SELECT SUM(amount) FROM expenses WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now') AND category='income' AND user_id=?", session["user_id"])
        expense = db.execute("SELECT SUM(amount) FROM expenses WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now') AND category='expense' AND user_id=?", session["user_id"])
    elif report_type == 'last_month':
        query = db.execute("SELECT * FROM expenses WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now', '-1 month') AND user_id=?", session["user_id"])
        income = db.execute("SELECT SUM(amount) FROM expenses WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now', '-1 month') AND category='income' AND user_id=?", session["user_id"])
        expense = db.execute("SELECT SUM(amount) FROM expenses WHERE strftime('%Y-%m', date) = strftime('%Y-%m', 'now', '-1 month') AND category='expense' AND user_id=?", session["user_id"])

    # Print income for debugging purposes
    inc = income[0]
    print(inc['SUM(amount)'])

    return render_template("report.html", data=query, income=income[0]['SUM(amount)'], expenses=expense[0]["SUM(amount)"])

@app.route("/expense")
def expense():
    """Display the latest expenses"""
    expenses_table = db.execute("SELECT * FROM expenses WHERE category=(?)  AND user_id=? ORDER BY expense_id DESC LIMIT 100", "expense", session["user_id"])
    return render_template("expense.html", expenses_table=expenses_table)

@app.route("/income")
def income():
    """Display the latest incomes"""
    expenses_table = db.execute("SELECT * FROM expenses WHERE category=(?)  AND user_id=? ORDER BY expense_id DESC LIMIT 100", "income", session["user_id"])
    return render_template("income.html", expenses_table=expenses_table)

@app.route("/home", methods=["GET", "POST"])
def home():
    """Handle new expense/income entry and display recent entries"""
    if request.method == "POST":
        print("success1")
        category = request.form.get("category")
        amount = request.form.get("amount")
        description = request.form.get("description")
        date = request.form.get("date")

        # Validate form data
        if not date or not amount or not category or not description:
            return render_template("home.html", user_name=session["user_name"])

        if session["user_id"] and amount and category and description and date:
            print("success4")
            db.execute("INSERT INTO expenses (user_id, amount, category, description, date) VALUES (?,?,?,?,?)", session["user_id"], amount, category, description, date)

    # Fetch the latest 5 expense entries
    expenses_table = db.execute("SELECT * FROM expenses WHERE user_id=? ORDER BY expense_id DESC LIMIT 5", session["user_id"])
    return render_template("home.html", user_name=session["user_name"], expenses_table=expenses_table)

@app.route("/")
def index():
    """Render the index page"""
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login"""
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # Ensure email and password were submitted
        if not request.form.get("email") or not request.form.get("password"):
            message = "Inputs should not be empty"
            return render_template("login.html", message=message)

        # Query database for email
        rows = db.execute("SELECT * FROM users WHERE email = ?", request.form.get("email"))

        # Ensure email exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            message = "Invalid credentials, please try again."
            return render_template('login.html', message=message)

        # Remember which user has logged in
        session["user_name"] = rows[0]["username"]
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/home")
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Handle user registration"""
    session.clear()

    if request.method == "POST":
        username = request.form.get("name")
        useremail = request.form.get("email")
        password = request.form.get("password")
        print(username)

        # Ensure all inputs are filled
        if password == "" or useremail == "" or username == "":
            message = "Fill all the inputs"
            return render_template("register.html", message=message)

        # Check if the user already exists
        rows = db.execute("SELECT * FROM users WHERE email = ?", useremail)
        if len(rows) == 1:
            message = "User already exists! Please kindly login."
            return render_template("register.html", message=message)
        else:
            print(username)
            hashcode = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            db.execute("INSERT INTO users (username, hash, email) VALUES (?, ?, ?)", str(username), hashcode, str(useremail))
            return render_template("login.html")
    else:
        return render_template("register.html")

@app.route("/mail_sent", methods=["GET", "POST"])
def mail_sent():
    """Handle OTP sending for password reset"""
    global otp_global, user_email_global

    if request.method == "POST":
        user_email = request.form.get("email")
        user_email_global = user_email  # Store user's email for later use

        # Check if the email exists in the database
        otp_sent = db.execute("SELECT email FROM users WHERE email=?", (user_email,))

        if otp_sent:
            otp = generate_otp()
            otp_global = otp  # Store OTP for verification
            send_otp(user_email, otp)
            return render_template("/forgot.html")
        else:
            flash("Email not found in company records. Please try again.", "error")

    return render_template("forgot_password.html")

@app.route("/forgot", methods=["GET", "POST"])
def forgot():
    """Handle password reset after OTP verification"""
    global otp_global, user_email_global

    if request.method == "POST":
        otp_received = request.form.get("otp")
        new_password = request.form.get("password")
        confirm_password = request.form.get("confirmpassword")

        # Verify OTP and update password
        if otp_received == otp_global:
            hash_code = generate_password_hash(confirm_password, method='pbkdf2:sha256', salt_length=8)
            db.execute("UPDATE users SET hash=? WHERE email=?", hash_code, str(user_email_global))
            message = "Password changed successfully!!"
            return render_template("login.html", message1=message)

    return render_template("forgot.html")

@app.route("/logout")
def logout():
    """Log out the current user"""
    session.clear()
    return redirect("/")

# Run the Flask app
if __name__ == "__main__":
    app.run()