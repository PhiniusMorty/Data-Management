#Import liberaries
import requests
import zipfile, json
from io import BytesIO
import s3fs, boto3
from datetime import datetime, date, timedelta
import pytz
import pandas as pd
import urllib.request
from pandas.io.json import json_normalize
from boto3 import client
from boto3.session import session

#Variables
s3_keys = ''
s3_secret = ''
header = {
  'accept': 'application/json',
  'X-Accellion-Version': '25',
  "Authorization': access_token
}

def download_url(url, save_path, chunk_size = 128):
  s3 = s3fs.S3FileSystem(key = S3_key, secret = s3_secret)  
  r = requests.request("GET", url, headers = header)
  with s3.open(save_path, 'wb') as f:
    for chunk in r.iter_content(chunk_size = chunk_size):
      f.write(chunk)
  return

def download(file_name):
  url_file_id = 'https://securesharek.target.com/rest/.......' #Get file ID link from documentation
  response = requests.get(url_file_id, headers = header)
  a = response.json()
  for i in range(len(a['data'])):
    url_download_file = 'https://securesharek.target.com/rest/files/{}/content'.format(a['data'][i]['id'])
    save_path = ''
    download_url(url_download_file, save_path)
    #Converting into csv format
    s3_resource = boto3.resource('s3', 
                                 aws_access_key_id = s3_keys, 
                                 aws_secret_access_key = s3_secret
                                )
    zip_obj = s3_resource.Object(bucket_name = '', 
                                 key = ''
                                )
    buffer = BytesIO(zip_obj.get()["Body"].read())
    zip_extract = zipfile.ZipFile(buffer)
    for filename in zip_extract.namelist():
      fileInfo = zip_extract.getinfo(filename)
      read_file = pd.read_csv(zip_extract.open(filename), sep = "\t")
      s3 = s3fs.S3FileSystem(key = s3_keys, secret = s3_secret)
      filename = filename.split('.txt')[0] # Add format of file. As an example I have added .txt
      # Add logic specific to file and format
      
      # Save the final file to S3
      with s3.open(f"", 'w', newline = "") as f:
        read_file.to_csv(f, index = False)
    return
        
def get_targetAPI(**kwargs):
  access_token = kwargs["access_token"]
  start_time = kwargs["start_time"]
  if str(kwargs['filename']) == '': #Add file name
    download(str(kwargs['filename']))
  else:
    continue
  
  return
