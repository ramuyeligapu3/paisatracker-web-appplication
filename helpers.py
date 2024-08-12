import smtplib
import random
import string
from email.mime.text import MIMEText
from flask import Flask, flash, render_template, redirect, request, session
from flask_session import Session
from functools import wraps

app=Flask(__name__)

app.secret_key='admz lxwo nsox dwqb'




# Function to generate a random OTP
def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

# Function to send an email with the OTP
def send_otp(email, otp):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "ramuyeligapu6@gmail.com"
    sender_password = "admz lxwo nsox dwqb"

    subject = "PaisaTracker OTP verification"
    body = "Your OTP code is "+otp

    message=MIMEText(body)

    message['Subject']=subject
    message['From']=sender_email
    message['To']=email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message.as_string())
        server.quit()
        print("OTP email sent successfully")
    except Exception as e:
        print(f"Failed to send OTP email: {e}")


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
