import smtplib
fromaddr = 'supxbr@gmail.com'
toaddrs  = '9145391203@vtext.com'
msg = 'I just spent my day after work figuring out how to send email with Python'
username = 'supxbr'
password = 'Cheapgrapes1'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()