import smtplib
from util import environment

def sendEmail(to, msg, subject):
    email = environment.GMAIL_EMAIL
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, environment.GMAIL_PASSWORD)
    message = f'From: Sistema de alertas tempranas" <{to}>\nSubject: {subject}\n\n{msg}'
    server.sendmail(email, to, message)
    server.quit()
    print("Correo enviado")