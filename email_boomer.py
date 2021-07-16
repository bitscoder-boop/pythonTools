import pandas as pd
import smtplib

file = input("Excel file path: ")
emailFile = pd.read_excel(file)
emails = emailFile['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
userEmail = input("Enter ur email: ")
userPass = input("Enter ur password: ")
server.login(userEmail, userPass)
msg = input("Enter ur mesages: ") 
subject = input("Enter ur subject: ")
body = f'{subject}, {msg}'
for email in emails:
    server.sendmail(userEmail, email, body)
print("Succesfullt send")
server.quit()
