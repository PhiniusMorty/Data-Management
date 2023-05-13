#import liberaries
import sys
import json
import boto3
import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta
from boto3.dynamodb.conditions import Key, Contains, Attr

def get_dynamoDB(**kwargs):
  #Variable defined
  region = ''
  Access_key = ''
  access_secret = ''
  #Connect to DynamoDB
  dynamodb_connect = boto3.resource('dynamodb', 
                                    region_name = region,
                                    aws_access_key_id = Access_key,
                                    aws_secret_access_key = access_secret)
  #Get data from Table 
  table = dynamodb.Table(kwargs['dynamodb_table'])  
  df = pd.DataFrame()
  response = table.scan(
    #FilterExpression = Attr('').contains()
  )
  items = response.get('Items')
  count = response["Count"]
  
  while 'LastEvaluateKey' in response:
    response = table.scan(
      #FilterExpression = Attr('').contains()
      ExclusiveStartKey = response['LastEvaluateKey']
    )
    count+= response["Count"]
    items.extend(response.get('Items'))
    
  print('Count for items in DynamoDB:', count)
  df = pd.DataFrame.from_dict(items)
  df_split = np.array_split(df, 30)
  # Add logic for formatting and cleaning!
  return
  
    
  
                 
      
    
  
