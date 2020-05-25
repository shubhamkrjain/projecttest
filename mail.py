import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("jainalokkumar5@gmail.com", "Passwrd@123") 
# message to be sent 
message = "Hey Developer,Your model train is ready and accuracy is above than 95%. "
# sending the mail 
s.sendmail("jainalokkumar5@gmail.com", "jainalokkumar5@gmail.com", message) 
# terminating the session 
s.quit()
