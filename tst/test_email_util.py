from email.mime.text import MIMEText
import Deck.email_util as email_util


def test_get_username():
    username, from_addr = email_util.get_username()
    print("Retrieved username %s for email %s" % (username, from_addr))