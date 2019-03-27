import smtplib #import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#settings for gmail
host="smtp.gmail.com"
port=587
username="user@gmail.com"
password="password"
to_list=["email_odbiorcy@gmail.com"]

#MESSAGE
the_msg=MIMEMultipart("alternative")
the_msg['Subject']="Hello there!"
the_msg["From"]=username
#the_msg["To"]=[to_list]

plain_txt="Testing the message"
html_txt="""\
<html>
	<head></head>
	<body>
		<p>Hey!</p>
		Testing this email <b>message</b>. Made by Konrad Szwed aka Kowareta.
		</p>
	</body>
</html>
"""

part_1=MIMEText(plain_txt,'plain')
part_2=MIMEText(html_txt,"html")

the_msg.attach(part_1)
the_msg.attach(part_2)
#print(the_msg.as_string())

email_connection = smtplib.SMTP(host, port)
email_connection.ehlo()
email_connection.starttls()
try:
	email_connection.login(username,password)
	email_connection.sendmail(username, to_list, the_msg.as_string())
except:
	print("Wrong username or password or another problem")

email_connection.quit()


