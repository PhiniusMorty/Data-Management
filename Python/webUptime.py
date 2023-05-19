#import libraries
import requests
import smtplib
import time

# Add Website URL to monitor
url = 'https://www.example.com/'

#Email settings
SMTP_server = 'smtp.mailExample.com'
SMTP_port = 587
email_user = 'email@example.com'
email_password = 'PASSWORD'
to_email = 'recipient@example.com'
subject = 'Website Down - Name'
message = f'{url} appears to be down. '

def send_email():
  with smtplib.SMTP(SMTP_server, SMTP_port) as server:
    server.starttls()
    server.login(email_user, email_password)
    message = f'Subject: {subject}\n {message}'
  
  return

def check_website():
  try:
    response = requests.get(url)
    if response.status_code != 200:
      send_email()  
  except requests.exceptions.RequestException:
    send_email()
  return

while True:
  check_website()
  time.sleep(60) #Check in every minute
    
      
