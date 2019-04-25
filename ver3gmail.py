import smtplib
import pymysql as dbms

Hi msg 
Hello msg

c=db.cursor()
c.execute('select Mail,Name from employee')
email=list(c.fetchall())

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from email.utils import COMMASPACE, formatdate

connection=smtplib.SMTP('smtp.gmail.com',587)
connection.ehlo()
connection.starttls()
print("started")
print("success")
connection.quit()
