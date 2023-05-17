#import libraries
import sys, time, requests, math, s3fs
from datetime import datetime, date, timedelta, timezone
from io import StringIO
import pandas as pd
from dateutil import tz

#get marketing data from Klaviyo
def klaviyoExport(**kwargs):
  metric_id = kwargs['metric']
  start_time = kwargs['start_time'] #Keep time in Epoch
  next_time = kwargs['end_time'] #Keep time in Epoch
  filename = kwargs['filename']
  df_final = pd.DataFrame()
  nextTime = '{}'.format(next_time)
  date = kwargs['date']
  headers = {'accept': 'application/json'}
  
  #Extract data for received email Type
  if metric_id = 'receivedMetrics':
    counter = 0
    count_var = 0
    name = '{}_{}.csv'.format(filename,date)
    while next_time > start_time:
      url = 'URL' # Add metric id, nextTime, and key for API
      response = requests.get(url, headers = headers)
      result = response.text
      df = pd.read_json(StrinIO(result))
      nextTime = df['next'].loc[1]
      next_list = nextTime,split('-')
      next_time = int(next_list[0])
      df2 = pd.json_normalize(df['data'])
      col_list = 'COLUMNS LIST' # Add columns to pull
      df_col = pd.DataFrame()
      
      #define columns in dataframe
      for i in col_list:
        df_col[i] = df2[i]
      df_final = pd.concat([df_final, df_col], ignore_index = True)
      counter+= 1
      
      #To optimize the data fetch. Generally received email type will have huge volume of data 
      if counter = 2000:
        # Save the df_final variable in a csv file and reinitialize
        # Add save logic by yourself according to need either in local or S3 buckets
        count_var+= 1
        counter = 0
    
    if c < 2000:
      # Save the df_final variable in a csv file and reinitialize
      # Add save logic by yourself according to need either in local or S3 buckets
  
  #Extract data for opened email Type
  elif metric_id = 'openedMetrics':
    counter = 0
    count_var = 0
    name = '{}_{}.csv'.format(filename,date)
    while next_time > start_time:
      url = 'URL' # Add metric id, nextTime, and key for API
      response = requests.get(url, headers = headers)
      result = response.text
      df = pd.read_json(StrinIO(result))
      nextTime = df['next'].loc[1]
      next_list = nextTime,split('-')
      next_time = int(next_list[0])
      df2 = pd.json_normalize(df['data'])
      col_list = 'COLUMNS LIST' # Add columns to pull
      df_col = pd.DataFrame()
      
      #define columns in dataframe
      for i in col_list:
        df_col[i] = df2[i]
      df_final = pd.concat([df_final, df_col], ignore_index = True)
      counter+= 1
      
      #To optimize the data fetch. Generally received email type will have huge volume of data 
      if counter = 2000:
        # Save the df_final variable in a csv file and reinitialize
        # Add save logic by yourself according to need either in local or S3 buckets
        count_var+= 1
        counter = 0
    
    if c < 2000:
      # Save the df_final variable in a csv file and reinitialize
      # Add save logic by yourself according to need either in local or S3 buckets
  
  #Extract data for Clicked email Type
  elif metric_id = 'clickedMetrics':
    counter = 0
    count_var = 0
    name = '{}_{}.csv'.format(filename,date)
    while next_time > start_time:
      url = 'URL' # Add metric id, nextTime, and key for API
      response = requests.get(url, headers = headers)
      result = response.text
      df = pd.read_json(StrinIO(result))
      nextTime = df['next'].loc[1]
      next_list = nextTime,split('-')
      next_time = int(next_list[0])
      df2 = pd.json_normalize(df['data'])
      col_list = 'COLUMNS LIST' # Add columns to pull
      df_col = pd.DataFrame()
      
      #define columns in dataframe
      for i in col_list:
        df_col[i] = df2[i]
      df_final = pd.concat([df_final, df_col], ignore_index = True)
      counter+= 1
      
      #To optimize the data fetch. Generally received email type will have huge volume of data 
      if counter = 2000:
        # Save the df_final variable in a csv file and reinitialize
        # Add save logic by yourself according to need either in local or S3 buckets
        count_var+= 1
        counter = 0
    
    if c < 2000:
      # Save the df_final variable in a csv file and reinitialize
      # Add save logic by yourself according to need either in local or S3 buckets
  
  ###############################################################################
  #Similarly Add for Bounced, Marked as spam, unsubscribed and other email types#
  ###############################################################################
  return


      
  
  
  
