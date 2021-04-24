import smtplib
from getpass import getpass

##INPUTS ARGS
sender      = input("Type your Email Sender and press enter: ")
password    = getpass("Type your Password and press enter: ") #We use getpass without echoing what we type to the console
recipient   = input("Type Recipient Email and press enter: ")
subject     = input("Type Subject Email and press enter: ")
text        = input("Type your mail text and press enter: ")

#CREATE A SECURE CONNECTION WITH GMAIL'S SMTP SERVER
##PORT SSL REQUIRED FOR GMAIL : 465
port        = 465
smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", port)

#AUTHENTICATE 
smtp_server.login(sender, password)
message     = "Subject: {}\n\n{}".format(subject, text)

#SEND MAIL
try:
    smtp_server.sendmail(sender, recipient, message)
except smtplib.SMTPException as e:
    print(e)
#QUIT SERVER
smtp_server.close()

