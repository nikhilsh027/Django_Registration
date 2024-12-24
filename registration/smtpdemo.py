import smtplib

sender = 'djangotest027@gmail.com'
receivers = ['nss96687@gmail.com']

message = """hello snow 
"""

gmail_user = "djangotest027@gmail.com"
gmail_app_password = "ndvx oxnp kftb tslg"
sent_from = "djangotest027@gmail.com"
sent_to = "nss96687@gmail.com"
email_text = message

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server. login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()

    print("Email sent!")
except Exception as exception:
    print(str(exception))
