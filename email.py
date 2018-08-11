import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("", "")

#Send the mail
def message(msg):
    server.sendmail("", "", msg)
