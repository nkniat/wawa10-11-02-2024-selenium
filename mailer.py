import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("natas.brd@gmail.com", "Fur112358rier")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("natas.brd@gmail.com", "natas.knt@gmail.com", message)
# terminating the session
s.quit()