import smtplib


def success():
    gmail_user = ''
    gmail_password = ''

    FROM = ''
    to = ''
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
    gmail_user = ''
    gmail_password = ''

    FROM = ''
    to = ''
    subject = 'Script has failed'
    text = 'Your classes have not been selected, please re-run the script with new CRN numbers'

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
