#import libraries
import sys, time, json, pytz
from datetime import date, datetime, timedelta
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adsinsights import AdsInsights
from facebook_business.adobjects.adreportrun import AdReportRun

#Add variables for Facebook API and initialize connection to API

FacebookAdsApi.init(access_token = KEYS['ACCESS_TOKEN'], api_version = 'v15.0')

#Get ad insights
def getAdInsight(**kwargs):
  print(str(kwargs['task_id']))
  #Add counter to track API calls
  counter = 0
  #Initialize data frame
  df = pd.DataFrame()
  #loop through account ids if multiple
  for account in kwargs['Account_id']:
    ads = AdAccount(account).get_insights(
      params = {
        "date_preset": "today"
        "action_attribution_window":["1d_click"],
        "level": "ad",
        "limit": "1000",
        "status": ["ACTIVE"]},
      fields = ad_fields,
      is_syn = True)
    ads.api_get()
    #Add while loop to verifuy that asyn is working
    while ads[AdsReportRun.Field.asyn_status]! = 'Job Completed' or ads[AdReportRun.Field.async_percentage_compeletion] <100:
      print(ads.api_get())
      time.sleep(1)
      ads.api_get()      
      if ads[AdReportRun.Field.async_status] == 'Job Failed':
        break
      else: 
        continue
    
    counter+=1    
    insights = str(ads.get_result(
      params = {"limit": 1000},
      fields = ad_fields
        )
      )
    #Replace string and convert to json
    df_normalized = json.laods(insights.replace('<AdsInsights>', ''))
    #append response to data frame
    df = df.append(df_normalized, ignore_index = True)
    time.sleep(1)
    return
