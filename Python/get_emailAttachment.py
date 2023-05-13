#import liberaries
import pandas as pd
import numpy as np
import psycopg2
from datetime import datetime, timezone, date, timedelta
import time
import s3fs
import email
import imaplib
import sys

def extract_attachment(**kwargs):
  #Variables
  files = []
  count = 0
  now = datetime.now()
  dt = date.today() - timedelta(days = now.weekday() + 1) #Monday
  start_time = dt.strftime('%d-%b-%Y')
  gmail_password = kwargs['password']
  gmail_user = kwargs['user']
  subject = ''
  #assign connection
  mail = imaplib.IMAP4_SSL(host = "imap.gmail.com", port = IMAP4_PORT)
  mail.login(gmail_user, gmail_password)
  mail.select('Inbox')
  details = f'(FROM "emailID@gmail.com" SUBJECT "Subject1" SINCE {start_time})'
  #Fetch data
  result, data = mail.search(None, details)
  ids = data[0] # data is a list
  id_list = ids.split() #ids is a space seperated string
  
  for num in id_list:
    typ, data = mail.fetch(num, '(RFC822)')
    #convert bytes literal to string
    email_message = email.message_from_string(data[0][1].decode('utf-8'))
    #To get attachment from email
    for part in email_message.walk():
      if part.get_content_maintype() == 'multipart' or part.get('Content-Disposition') is None:
        continue
      fileName = part.get_filename()
      #print(fileName)
      file_part = fileName.split('.')[0]
      
      
        
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
