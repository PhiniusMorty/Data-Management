import sys
from datetime import datetime, timedelta
import pandas as pd
import requests
import json
import numpy as np
import psycopg2
import s3fs
import pytz
import mysql.connector
from mysql.connector import Error, FeildType

def redshiftConnect():
  
  conn = psycopg2.connect(
    host = 'placeholder',
    database = 'placeholder',
    port = 'placeholder',
    user = 'placeholder',
    password = 'placeholder'
  )
  cursor = conn.cursor()
  cursor.execute("Select * from Table")
  df = pd.DataFrame(cursor.fetchall())
  conn.commit()
  conn.close()
  return df

def mysqlConnect():
  conn = mysql.connector.connect(
    host = 'placeholder',
    database = 'placeholder',
    user = 'placeholde',
    password = 'placeholde'
  )
  cursor = conn.cursor()
  cursor.execute(query)
  results = cursor.fetchall()
  df_export = pd.DataFrame(results, dtype = object)
  _uploadToS3(bucket = kwargs['bucket'], csv_name = kwargs['csv_name'], file = df_export)
  
 
    
    
