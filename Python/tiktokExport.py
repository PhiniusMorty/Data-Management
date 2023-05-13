#import liberaries
import pandas as pd
import json, requests, sys
from pandas import json_normalize
from datetime import date, datetime, timedelta
from six import string_types
from six.moves.urllib.parse import urlencode, urlunparse

def getAds(**kwargs):
  header = {
    "Access_token": kwargs['Access_token']
  }
 
  list_tiktok = []
  # For disaster management
  start_time = f'{datetime.today() - timedelta(days = 3): %Y-%m-%d}'
  end_time = f'{datetime.today() - timedelta(days = 0): %Y-%m-%d}'
   url = '' #Add url with parameters
  for i in range(1,10):
    response = requests.get(url, headers = header
  
            
