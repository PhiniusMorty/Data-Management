#import Liberaries
import sys
from datetime import datetime, date
import pandas as pd
import pytz, s3fs, psycopg2, boto3

def validateFile(**kwargs):
  #Get a list of keys in S3 bucket.
  s3_paginator = boto3.client('s3', 
                              aws_access_key_id = S3_key,
                              aws_secret_access_key = s3_secret, verify = True
                             )
  try:
    resp = s3_paginator.list_objects(bucket = kwargs['bucket'], Prefix = kwargs['bucket_key'])
    for obj in resp['Contents']:
      if obj['key'] == kwargs['bucket_key']:
        print('File upload successful. File: ', obj['key'])
        break
      else:
        print('No match')
        return False
  except Exception as error: 
    print(f'Failed to execute validation: {error}')
    return
  
