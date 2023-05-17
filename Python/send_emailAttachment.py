#import libraries
import sys, s3fs,os, smtplib, pytz, time
import pandas as pd
import numpy as np
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
from io import StringIO

def send_emailAttachment():
  #Add to, cc, recepient, subject line, data_msg, noData_msg, and other
  to = 'mail@gmail.com'
  cc = 'mailcc@gmail.com'
  recepient = cc.split(',') + [to]
  subject = "Subject"
  file_name = 'FILE NAME' # Add file name
  data_msg = 'message containing data'
  noData_msg = 'message containing no data'
  gmail_pass = 'PASSWORD'
  user = 'USER'
  host = 'smtp.gmail.com'
  port = 'PORT'
  # Create message object
  message = MIMEMultipart()
  # Add in header
  message['From'] = Header(user)
  message['To'] = Header(to)
  message['CC'] = cc
  message['Subject'] = Header(subject)
  textStream = StringIO()
  # Add your condition to extract data and put it in data (possibly DataFrame)
  
  if data.empty:
    # Add message body as MIMEText
    message.attach(MIMEText(noData_msg, 'plain', 'utf-8'))
  else:
    data.columns = []
    data.to_csv(textStream, index = False)
    #Add message body as MIMEText
    message.attach(MIMEText(body, 'plain', 'utf-8'))
    #Add attachments
    message.attach(MIMEApplication(textStream.getvalue(), Name = file_name))
    
  #Email Server
  server = smtplib.SMTP_SSL(host, port)
  server.login(user, gmail_pass)
  #Send mail and quit server
  server.sendmail(user, recepient, message.as_string())
  server.quit()
  return

                   
                   
  
  
  
