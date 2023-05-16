#import libraries
import sys, time, requests, math, s3fs
from datetime import datetime, date, timedelta, timezone
from io import StringIO
import pandas as pd
from dateutil import tz

#get marketing data from Klaviyo
def klaviyoExport(**kwargs):
  metric_id = kwargs['metric']
  start_time = kwargs['start_time']
  
  
