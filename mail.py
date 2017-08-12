#!/usr/bin/env python
import argparse
import getpass
import smtplib

USER = 'hotyrobot@gmail.com'
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--user", default=USER)
parser.add_argument("-t", "--tos", default="eugene.kondrashev@gmail.com")

parser.add_argument("-m", "--message", default='Test message')

parser.add_argument("-s", "--subject", default='Test subject')


def get_password(key, user):
    import keyring
    try:
        password = keyring.get_password('aci_mail_bot', user)
    except:
        password = getpass.getpass('Password:')
        keyring.set_password(key, user, password)
    return password


def send(tousr, subj, body, username=USER, password=None):
    if not password:
        password = get_password(username)
    headers = "\r\n".join(["from: " + username,
                       "subject: " + subj,
                       "to: " + tousr,
                       "mime-version: 1.0",
                       "content-type: text/html"])
    # body_of_email can be plaintext or html!
    content = headers + "\r\n\r\n" + body

    # The below code never changes, though obviously those variables need values.
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(username, password)
    session.sendmail(username, tousr, content)


def sendmsg(tos, msg, username=USER, password=PASSWORD):
    if not password:
        password = get_password(username)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(username, password)
    session.sendmail(username, tos, msg.as_string())


if __name__=="__main__":
    args = parser.parse_args()
    send(args.tos, args.subject, args.message)
