#import Liberaries
import sys, psycopg2
import pandas as pd
from googleapiclient.discovery import build
from google.oauth2 import service_account

#import google and DB parameters
Scopes = ['SCOPE'] # Add scope
id
#Authenticate Google
credentials = service_account.Credentials.from_service_account_file( , scopes = Scopes) # Add scope
sheet_service = build('sheets', 'v4', credentails = credentials)

#To call and read content of google sheet
def readSheets(**kwargs):
  get_range = f'{kwargs['sheet_name']}!{kwargs['cell_range']}'
  sheet_id = 
  result = sheet_service.spreedsheets().values().get(sheet_id = sheet_id, range = get_range).execute()
  rows = result.get('values',[])
  df = pd.DataFrame(rows, dtype = object)
  return

#To clear rows or entire sheets
def clearSheets(**kwargs):
  sheet_service.spreedsheets().values().clear(spreedsheet_id = kwargs['id'], range = kwargs['get_range']).execute()
  return

#To write on sheets
def writeSheets(**kwargs):
  #Get data into a datafrmae
  
  data = [{'range': kwargs['get_range'], 'values': values}]
  body = {
    'value_input_option': 'RAW',
    'data': data
  }
  
  sheet_service.spreedsheets().values().batchUpdate(spreadsheet_id = kwargs['id'], body = body).execute()
  return

  
  
                                                                    
