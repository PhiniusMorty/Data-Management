import loggin
import boto3
import s3fs

#S3_secret = ''
#S3_Key = ''

def _uploadToS3 (index = False, header = True, **kwargs):
  s3 = s3fs.S3FileSystem(key = S3_Key, secret = S3_secret)
  with s3.open(f"s3://{kwargs['bucket']}/{kwargs['csv_name']}", 'w') as f:
    kwargs['file'].to_csv(f, index = index, header = header)
    
def single_api_toS3(**kwargs):
  #Upload the file
  s3_client = boto3.client('s3')
  
  try:
    response = s3_client.upload_file(
      kwargs['file_name'],
      kwargs['bucket'],
      kwargs['object_name'],
      ExtraArgs = {'ACL': f'{kwargs["permissions"]}'})
    print('File Uploaded!')
  except ClientError as e:
    print(logging.error(e))
    
def multiple_to_s3(**kwargs):
  #Upload the file
  s3_client = boto3.client('s3')
  
  for file in kwargs['file_name']:
    object_name = file.split('/')[-1]
    print(object_name)
    
    try:
      response = s3_client.upload_file(file, kwargs['bucket'], object_name)
      print('File uploaded!')      
    except ClientError as e:
      print(logging.error(e))
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
