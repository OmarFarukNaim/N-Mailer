
import smtplib
import time
import pyfiglet
f = pyfiglet.figlet_format("N-Mailer", font="slant")
print(f)
sender_email = input("Enter Sender Email>")
email_password = input("Enter EMail Password>")
receiver_email=input("Enter Receiver Email>")

subject = input("Enter Email Subject>")
message = input("Enter Your Message Here>")
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email,email_password)
i = int(input("How many email you want to send>"))
j = 0
while j < i:
    server.sendmail(sender_email, receiver_email, message)
    j = j+1
    print("EMail sent to" + " " + receiver_email + " " + "Count" + " " + str(j))
    time.sleep(2)
