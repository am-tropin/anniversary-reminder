#!/usr/bin/env python
# coding: utf-8

# In[1]:


from functions.functions_store import announcement_upcoming_month


# In[2]:


announcement_upcoming_month()


# In[ ]:





# In[ ]:





# In[30]:


# announcement for an upcoming week
# to launch on Sundays

# df = range_calendar((TODAY_DT + timedelta(1)).strftime(DATE_FORMAT), (TODAY_DT + timedelta(7+1)).strftime(DATE_FORMAT))
# df

# with open('announcement_weekly.txt', 'w') as f:
#     for index, row in df.iterrows():
#         f.write("{0} -- {1} {2}s since {3}".format(row['date'], row['amount'], row['unit'], row['event']))
#         f.write('\n')

