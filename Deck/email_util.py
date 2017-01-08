import keyring
import smtplib

GMAIL = 'smtp.gmail.com:587'
SERVICE = "gmail"


def get_username():
    username = keyring.get_password(SERVICE, "username")
    email_addr = username+'@gmail.com'
    return username, email_addr


def get_password(username):
    return keyring.get_password(SERVICE, username)


def send_email(to_addr, message):
    server = smtplib.SMTP(GMAIL)
    server.ehlo()
    server.starttls()
    username, from_address = get_username()
    password = get_password(username)
    server.login(username, password)
    server.sendmail(from_address, to_addr, message)
    server.quit()
