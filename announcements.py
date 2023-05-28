#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd 
from datetime import datetime, date, timedelta
import calendar

from functions_store import range_calendar, stod


# In[2]:


DATE_FORMAT = "%Y-%m-%d"
TODAY_DT = date.today()


# In[3]:


events_df = pd.read_csv("events.csv")
events_df['dt'] = events_df['date'].apply(lambda x: datetime.strptime(x, DATE_FORMAT).date())
events = events_df.set_index('event').transpose().to_dict()


# In[30]:


# announcement for an upcoming week
# to launch on Sundays

# df = range_calendar((TODAY_DT + timedelta(1)).strftime(DATE_FORMAT), (TODAY_DT + timedelta(7+1)).strftime(DATE_FORMAT))
# df

# with open('announcement_weekly.txt', 'w') as f:
#     for index, row in df.iterrows():
#         f.write("{0} -- {1} {2}s since {3}".format(row['date'], row['amount'], row['unit'], row['event']))
#         f.write('\n')


# In[25]:


# announcement for an upcoming month
# to launch on 28th of previous month

days_month = lambda dt: calendar.monthrange(dt.year, dt.month)[1]

first_dt = TODAY_DT.replace(day=1) + timedelta(days_month(TODAY_DT))
last_dt = first_dt + timedelta(days_month(first_dt) - 1)

df = range_calendar(first_dt.strftime(DATE_FORMAT), last_dt.strftime(DATE_FORMAT))
df


# In[29]:


with open('announcement_monthly.txt', 'w') as f:
    f.write(first_dt.strftime("%B %Y"))
    f.write('\n\n')
    
    for index, row in df.iterrows():
#         f.write("{0} -- {1} {2}s since {3}".format(row['date'], row['amount'], row['unit'], row['event']))
        f.write("{0} -- {1} {2}s since {3}".format(stod(row['date']).strftime("%d"), row['amount'], row['unit'], row['event']))
        f.write('\n')


# In[ ]:




