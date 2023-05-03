import sys
from datetime import datetime, timedelta
import pandas as pd
import requests
import time
import json
import numpy as np
import psycopg2
import s3fs
import pytz

#S3_secret = ''
#S3_Key = ''

def redshiftViewBackup(**kwargs):
  tz_NY = pytz.timezone('American/New_York')
  #Connect to Redshift
  conn = psycopg2.connect(
    host = 'placeholder',
    database = 'placeholder',
    port = 'placeholder',
    user = 'placeholder',
    password = 'placeholder'
  )
  cursor = conn.cursor()
  
  #get_schemalist function is defined to get the list of schemas containing views
  def get_schemalist():
    cursor.execute("SELECT Distinct schemaname from pg_views where schemaname not in ('pg_catalog', 'information_schema');")
    df = pd.DataFrame(cursor.fetchall())
    conn.commit()
    return df
  
  #get list of views from a given schema
  def get_viewlist(schema):
    query = "SELECT viewname from pg_views where schemaname = '{0}'".format(schema)
    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall())
    conn.commit()
    view_list = df[0].to_list()
    return df
  
  #get Create script for given view
  def get_createScript(view):
    query = "SELECT viewname, definition from pg_views where schemaname not in ('pg_catalog', 'information_schema') and viewname = '{0}'".format(view)
    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall()[0][1])
    conn.commit()
    view_list = df[0].to_list()
    return df
  
  data = get_schemalist()
  schema_list = data[0].to_list()
  counter = 0
  
    
  for schema_name in schema_list:    
    view_list = get_viewlist(schema_name)
    for view in view_list: 
      query = get_createScript(view)
      read_view_name = f'{schema_name}.{view}.sql'
      folder_name = f'{datetime.now(tz_NY):%Y%m%d}'
      #uploading all the files to s3 into given folder
      s3 = s3fs.S3FileSystem(key = S3_key, secret = S3_secret)
      with s3.open(f"s3://{kwargs['bucket']/scriptBackups/{folder_name}/{read_view_name}", 'w', encoding = 'utf-8') as f:
        f.write(query)
      prinit(f"{read_view_name} uploaded to s3")
      counter = counter + 1

  print(f"{counter} views uploaded")
  conn.close()
  return

      
