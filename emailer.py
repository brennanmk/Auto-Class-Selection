import smtplib


def success():
    gmail_user = 'brennanmk2200@gmail.com'
    gmail_password = 'Bpm02052'

    FROM = 'brennanmk2200@gmail.com'
    to = 'brennanmk2200@gmail.com'
    subject = 'Script has completed'
    text = 'Your classes have been selected'

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
       """ % (FROM, ", ".join(to), subject, text)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(FROM, to, message)
        server.close()
    except:
        print('Something went wrong...')


def failure():
    gmail_user = 'brennanmk2200@gmail.com'
    gmail_password = 'Bpm02052'

    FROM = 'brennanmk2200@gmail.com'
    to = 'brennanmk2200@gmail.com'
    subject = 'Script has failed'
    text = 'Your classes have no been selected'

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
           """ % (FROM, ", ".join(to), subject, text)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(FROM, to, message)
        server.close()
    except:
        print('Something went wrong...')
