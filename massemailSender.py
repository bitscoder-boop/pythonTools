import pandas as pd
import smtplib
from email.mime.text import MIMEText


def getuserCredentials():
    # user id and password to send the email from
    userEmail = input("Enter ur email: ")
    userPass = input("Enter ur password: ")
    return userEmail, userPass


def getMessage(userEmail):
    #message body and structure to send are defined here
    message = MIMEText(input("Message: "))
    message['Subject'] = input("Subject: ")
    message['From'] = userEmail
    return message

if __name__ == '__main__':
    emailFile = pd.read_excel(input("Excel file path: "))
    emails = emailFile['Emails'].values
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    userEmail, userPass = getuserCredentials()
    server.login(userEmail, userPass)
    message = getMessage(userEmail)
    for email in emails:
        server.sendmail(userEmail, email, message.as_string())
    print("Succesfullt send")
    server.quit()

