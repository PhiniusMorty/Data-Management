#import Liberaries
import boto3
import json
import time

def lambda_handler(event, context):
  #Connect to DMS
  client = boto3.client('dms')
  #task ARN 
  taskArn = ['']  
  try: 
    for arn in taskArn:
      #modify the DMS task
      repsonse = client.modify_replication_task(
        ReplicationTaskArn = arn,
        ReplicationTaskSettings = '{"Logging": {"DeleteTaskLogs": true}}'
      )
      print('Modifying task with ARN as:', arn)
      time.sleep(5)
      return {
        'statusCode': 200,
        'body': json.dumps('Logs are deleted')
      }
    
  except Exception as error:
    raise error
