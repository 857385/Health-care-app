import smtplib
from email.mime.text import MIMEText

def send_email_notification(to_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'youremail@example.com'
    msg['To'] = to_email

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('youremail@example.com', 'password')
        server.sendmail('youremail@example.com', to_email, msg.as_string())
