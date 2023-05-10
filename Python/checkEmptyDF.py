import sys, s3fs
import pandas as pd


def _checkEmptyDF(**kwargs):
  #Connect to S3 file system
  s3 = s3fs.S3FileSystem(key = kwargs["S3_key"], secret = kwargs["s3_secret"])
  names_list = filenames(kwargs["filename"], kwargs["access_token"], kwargs["start_time"])
  try:
    for file_name in names_list:
      #print(file_name, type(file_name))
      df = pd.read_csv(s3.open(f"d3://{kwargs["bucket"]}/{kwargs["folder"]}/{file_name}.csv", mode = 'rb'))
      #print(df, type(df))
      print('Dataframe is Not empty, queing all the tasks!')
      return 
    
    if not names_list: 
      print(f'File - {kwargs["filename"]} is not available in s3')
      return
    
  except pd.errors.EmptyDataError as e:
    print("Warning: Oops! ", e, " occurred.")
    print('Dataframe is empty, skipping downstream processes!')
    return
  
