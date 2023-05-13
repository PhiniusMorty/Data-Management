#import liberaries
import paramiko, psycopg2
import pandas as pd
import boto3, s3fs
import datetime from datetime, date, timedelta

#Global variables
access_key = ''
access_secret = ''
region = ''

def sftpExtract(**kwargs):
  max_file_date = '' # Add a logic to get date from database or system
  file_type = kwargs['file_type']
  s3_conn = boto3.client('s3', 
                         aws_access_key_id = access_key,
                         aws_secret_access_key = access_secret
                        )
  host = 'sftp.attentivemobile.com'
  port = 22
  password = kwargs['password']
  username = kwargs['username']
  
  client = paramiko.SSHClient()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  client.connnect(hostname = host, port = post, username = username, password = password)
  sftp = client.open_sftp()
  sftp.chdir('/downloads')
  remote_files = sftp.listdir()
  remote_path = f'/downloads/'
  file_list = [] 
  #Add logic below to get the file list as required
  
  # Add the files to S3 bucket
  for i in file_list:
    with sftp.open(remote_path +i, "r") as f:
      f.prefetch()
      s3_conn.put_object(Body = f, 
                         bucket = kwargs['bucket'],
                         keys = kwargs['key_bucket']
                        )
  sftp.close()
  client.close()
  return
                         

  
  
  
