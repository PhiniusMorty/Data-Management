#import libraries
import sys, json, sys, requests, time, pytz
import urllib.request as urllib2
from io import BytesIO
from zipfile import ZipFile
import boto3
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta

#API access credentials
API_key = 'API_KEY'
API_password = 'API_PASSWORD'

#To get ratings and Ticket data export
def get_ratingTickets(**kwargs):
  #set up time parameter
  current_hour = datetime.now() - timedelta(hours = 72)
  current_time = current_hour.strftime(f'%Y-%m-%d')
  df = pd.DataFrame()
  #Pagination counter
  pg_number = 1
  
  if str(kwargs['category']) == 'ratings':
    #Get staisfaction ratings
    url = 'URL' #Add url
    rating_response = requests.get(url, auth = (API_key, API_password)) #Add time
    
    if rating_response.status_code == 200:
      print('Request successful')
      
      while pg_number!=0:
        response = requests.get(url, auth = (API_key, API_password)) #Add time and page number
        insights = json.loads(response.content)
        header = response.headers
        df = df.append(insights, ignore_index = True)
        
        #Next page if link is found:
        try:
          print(header['link'])
          pg_number+= 1
        except Exception:
          pg_number = 0
          print('Page not found')
        
        #Handling rate limits
        page_diff = pg_number - 1
        
        if (page_diff%40 == 0):
          time.sleep(60)
          
      print('End requests!')
      
    else:
      response = json.loads(rating_response.content)
      print(f'Unable to read tickets. \n X-request-id:{rating_response.headers['x-request-id']} \n Status Code: {str(rating_response.status_code)}')
  
  elif str(kwargs['category']) == 'tickets':
    #check for status code
    ticket_response = requests.get(url, auth = (API_key, API_password)) #Add time
    
    if ticket_response.status_code == 200:
      print('Request successful')
      
      while pg_number!=0:
        response = requests.get(url, auth = (API_key, API_password)) #Add time and page number
        insights = json.loads(response.content)
        header = response.headers
        df = df.append(insights, ignore_index = True)
        
        #Next page if link is found:
        try:
          print(header['link'])
          pg_number+= 1
        except Exception:
          pg_number = 0
          print('Page not found')
        
        #Handling rate limits
        page_diff = pg_number - 1 
        
        if (page_diff%40 == 0):
          time.sleep(60)
          
      print('End requests!')
    
    else:
      response = json.loads(ticket_response.content)
      print(f'Unable to read tickets. \n X-request-id:{ticket_response.headers['x-request-id']} \n Status Code: {str(ticket_response.status_code)}')
      
  else:
    print('No category defined')

  return
'''
#------------------------------Documentation------------
To get customer statisfaction score.

https://support.freshchat.com/en/support/solutions/articles/50000002990-extract-api

Report list
0. Conversation Created
1. Conversation Agent Assigned
2. Conversation Group Assigned
3. Message Sent
4. First Response Time
5. Response Time
6. Resolution Time
7. Conversation Resolution Label
8. Conversation Resolved
9. Agent Activity
10. Agent Intelliassign Activity
11. CSAT Score
#---------------------------------------------------------
'''
def get_CSATscore(**kwargs):
  report_name = kwargs['report_name']
  current_time = datetime.now() #Can change timezone by using pytz.timezone('Required timezone')
  start_time = current_time.date() - timedelta(days = 1)
  end_time = current_time.date()
  data_format = 'csv'
  
  url = 'URL' #Add required url
  # Add a payload
  payload = '{"start":\"' + str(start_time)+ '\", "end": \"'+ str(end_time)+ '\", "event": \"'+report_name+ '\", "format": "'+data_format+ '\"}'
  headers = {
    'accept':'application/json',
    'Content-Type': 'application/json',
    'Authorization': str((API_key, API_password))
  }
  response = requests.request("POST", url, headers = headers, data = payload)
  report_id = response.json()
  time.sleep(60)
  
  try:
    df = pd.DataFrame()
    for link in links:
      
  























