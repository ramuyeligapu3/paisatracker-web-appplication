import smtplib
from email.mime.text import MIMEText
import random

def send_email(subject, body, to_email):
    from_email = "ramuyeligapu6@gmail.com"
    app_password = "admz lxwo nsox dwqb"
    otp=random.randint(000,999)

    msg = MIMEText(otp)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, app_password)
        server.sendmail(from_email, to_email, msg.as_string())

# Example usage
send_email("Test Subject", "Test Body", "ramuyeligapu9@gmail.com")

