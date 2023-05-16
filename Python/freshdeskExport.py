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
  report_id_value = response.json()
  time.sleep(60)
  
  #Get report download links
  try:
    report_id = report_id_value['id']
    report_url = 'URL' # Add report ID
    report_payload = '# {Id: '+str(report_id)+', link:{rel: extracts, Href: /reports/raw/'+str(report_id)+'}'
    report_response = requests.request("GET", report_url, headers = headers, data = report_payload)
    raw_link = report_response.json()
    report_link =  raw_link['links']
    time.sleep(60)
    
    try:
      df = pd.DataFrame()
      
      for link in report_link:
        
        if link['status'] == 'COMPLETED':
          href = link['link']['href']
          resp = urllib2.urlopen(href).read()
          file = ZipFile(BytesIO(resp))
          file_name = list(file.NameToInfo)[0]
          
          try:
            df_metric = pd.read_csv(file.open(file_name))
            df = pd.concat([df, df_metric])
            print('DataFrame contains data!')
          except pd.errors.EmptyDataError:
            print('DataFrame is empty. Warning: Oops! ', sys.exc_info[0],' occured.')
        
        else:
          print('1. Export failed for report!')
        # Inner loop ends!
      
      #Save the downloaded data into csv. Add code accordingly
    except:
      print('2. Export failed for report!')
      pass
  except:
    print('3. Export failed for report!')
    pass
  
  return
#End of Code for CSAT Score

#get CS data from Freshdesk
def get_Tickets_CSdata(**kwargs):
  df = pd.DataFrame()
  #Pagination
  pg_number = 1
  print('Get Tickets:')
  #Check status
  url = 'URL'
  ticket_status = requests.get(url, auth = (API_key, API_password))
  
  if ticket_status.status_code == 200:
    while (pg_number != 0 and pg_number < 250): 
      url_tickets = 'URL' # Add time and page number
      tickets = requests.get(url_tickets, auth = (API_key, API_password))
      insights = json.loads(ticket.content)
      header = tickets.headers
      df = df.append(insights, ignore_index = True)
      
      #Next page if link is found:
      try:
        pg_number+=1
      except Exception:
        pg_number = 0
        print('Last page loaded')
      
      pg_diff = pg_number - 1
      if (pg_diff%40 == 0):
        time.sleep(60)
    # Add code below to clean the data
  
  else:
    response = json.loads(tickets_status.content)
    print(f'Failed to read tickets. Error: {response['errors']}.\n X-request-id:{response.headers['x-request-id']} \n Status Code: {str(response.status_code)}')
      
  return
            
          
        
        
      
  























