import os.path
from email.message import EmailMessage
#creating an empty email message
message = EmailMessage()

#creating sender and recipient
sender = "me@example.com"
recipient = "you@example.com"

#creating attachment
attachment_path = r"C:\Users\Email\example.png"
attachment_filename = os.path.basename(attachment_path)

#In order for the recipient of your message to understand what to do with an attachment, you  need to label the attachment with a MIME type and subtype to tell them what sort of file you’re sending.
#Using mimetypes module to detect the type and subtype of the attachment files

import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
#print(mime_type)

#The EmailMessage type needs a MIME type and subtypes as separate strings, so let's split this up 
mime_type, mime_subtype = mime_type.split('/', 1)
#print(mime_type)
#print(mime_subtype)

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
body = """Hey there! I'm learning to send emails unsing Python"""
message.set_content(body)

#Adding attachment to the message
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=os.path.basename(attachment_path))

#Use smtplib module to send the message ans set up mail server
import smtplib

mail_server = smtplib.SMTP_SSL('smtp.example.com', 485)

#Authenticate to the SMTP server
import getpass
mail_pass = getpass.getpass('Password? ')
mail_server.login(sender, mail_pass)

mail_server.send_message(message)
mail_server.quit()
#print(message)