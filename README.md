Sending Emails With Python

# SendeMailPython

#### Getting Started
```
Python comes with the built-in smtplib module for sending emails using the Simple Mail Transfer Protocol (SMTP). smtplib uses the RFC 821 protocol for SMTP. The examples in this project will use the Gmail SMTP server to send emails, but the same principles apply to other email services.
```

#### Note : Setting up a Gmail Account for Development
```
If you decide to use a Gmail account to send your emails, I highly recommend setting up a throwaway account for the development of your code. This is because you’ll have to adjust your Gmail account’s security settings to allow access from your Python code, and because there’s a chance you might accidentally expose your login details.
```
To set up a Gmail address for testing your code, do the following:

* Turn Allow less secure apps to ON :  Be aware that this makes it easier for others to gain access to your account.

If you don’t want to lower the security settings of your Gmail account, check out Google’s documentation on how to gain access credentials for your Python script, using the OAuth2 authorization framework.


## Download and install 

```
$ git clone https://github.com/Taysssir/SendeMailPython.git
$ cd SendeMailPython
$ python sendmail.py
```
Output Console : You will find something similar to this:
```
Type your Email Sender and press enter: 
Type your Password and press enter: 
Type Recipient Email and press enter: 
Type Subject Email and press enter: 
Type your mail text and press enter: 
```