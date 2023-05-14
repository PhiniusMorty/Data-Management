#import libraries
import sys, json, sys, requests, time
import boto3
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta

#API access credentials
API_key = 'API_KEY'
API_password = 'API_PASSWORD'

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


