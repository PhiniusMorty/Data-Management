#import Liberaries
import boto3
import json
impot datetime
import dateutills.z

#Create a timzone object for EST
est_tz = dateutill.tz.gettz('US/Eastern')

#get the current time in EST timezone
now = dateitme.datetime.now(tz = est_tz)

current_time = now.strftime("%H:%M")
print(current_time)

client = boto3.client('dms')
client_sns = boto3.client('sns')

def lambda_handler(event, context):
  #task ARN
  inc_taskARN = ''
  full_taskARN = ''
  
  responseInc = client.describe_replication_tasks(
    Filters = [
      {
        'Name' = "",
        "Values": []
      }
    ]
  )
  
  try: 
    #Add logic for trigger
    
    #Setup SNS notification
    notification = ''
    response = client_sns.publish(
      TargetARN = "",
      Messsage = json.dumps({'default': notification}),
      MessageStructure = 'json',
      Subject = ''
    )
  except Exception as e:
    #Add exception 
    
  return
