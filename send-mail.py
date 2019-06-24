#THIS FILE NEEDS TO *NOT* BE NAMED email.py
#email.py is reserved from smtplib

import smtplib

#test email - please be kind
sender_email_id = 'tmail4319@gmail.com'
sender_email_id_password = 'test~password'
receiver_email_id = 'tmail4319@gmail.com'

#Notifies user via email. Current method does NOT support attachments.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls() 
s.login(sender_email_id, sender_email_id_password)
message = "Warning! Motion Detected!"
s.sendmail(sender_email_id, receiver_email_id, message) 
s.quit()