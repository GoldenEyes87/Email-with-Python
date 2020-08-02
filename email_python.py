import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template
html = Template(Path("1.html").read_text())
# we have imported a class therefore initializing an object
email = EmailMessage()
email['from'] = "Your name"
# content of the email can be anything text pic etc.
email['to'] = 'Email address of the person you want to send it to'
email['subject'] = 'Subject of the email'
email.set_content(html.substitute(name="content"), 'html')
# helps you to connect with gmail server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # same as saying hello to another person
    smtp.starttls()
    # print(smtp.local_hostname)
    # logs into your account
    smtp.login("your email address", 'your accounts password')
    smtp.send_message(email)
print('email is sent')
