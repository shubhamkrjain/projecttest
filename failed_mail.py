import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("jainalokkumar5@gmail.com", "Passwrd@123") 
# message to be sent 
message = "Hey Developer, you need to check your code once. Might be this have some error. "
# sending the mail 
s.sendmail("jainalokkumar5@gmail.com", "jainalokkumar5@gmail.com", message) 
# terminating the session 
s.quit()
