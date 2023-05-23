#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:


import pandas as pd 
from datetime import datetime, date, timedelta
from itertools import combinations


# In[6]:


DATE_FORMAT = "%Y-%m-%d"
TODAY_DT = date.today() #.strftime(DATE_FORMAT)


# # 1. Loading the csv of dates

# In[7]:


events_df = pd.read_csv("events.csv")
events_df.head()


# In[8]:


# adding a column dt with format datetime.date()

events_df['dt'] = events_df['date'].apply(lambda x: datetime.strptime(x, DATE_FORMAT).date())
events_df.head()


# In[9]:


events = events_df.set_index('event').transpose().to_dict()
events


# # 2. Functions

# ## 2.1. Secondary functions

# In[10]:


def stod(dt_str):
    """Converts string variable `dt_str` to date.
    
    Args:
        dt_str (str): The string date in `DATE_FORMAT` format.
        
    Returns:
        Date
    """
    return datetime.strptime(dt_str, DATE_FORMAT).date()


# In[11]:


def days_between(dt1, dt2):
    """Calculates difference between `dt1` and `dt2`.
    
    Args:
        dt1 (date): The first date.
        dt2 (date): The second date.
        
    Returns:
        Boolean
    """
    try:
        return abs((dt2 - dt1).days)
    except:
        return None


# In[12]:


# iterator by date
# input and output format: date(YYYY, MM, DD) 

def daterange(start_dt, end_dt):
    """Generates a range of dates from `start_dt` to `end_dt` (including the ends).
    
    Args:
        start_dt (date): The start date.
        end_dt (date): The end date.
        
    Returns:
        Iterator of dates (date)
    """
    for n in range(int((end_dt - start_dt).days) + 1):
        yield start_dt + timedelta(n)


# In[13]:


# rules for detecting anniversaries
# input format: date(YYYY, MM, DD) 

def rule_multiple(dt1, dt2, n):
    """Identifies if difference between 2 dates `dt1` and `dt2` is multiple of `n`.
    
    Args:
        dt1 (date): 
        dt2 (date): 
        n (int): The number of multiplicity.
        
    Returns:
        bool
    """
    if days_between(dt1, dt2) % n == 0:
        return True
    else:
        return False

def rule_anniversary(dt1, dt2):
    """Identifies if `dt1` is an anniversary of `dt2` or vice versa.
    
    Args:
        dt1 (date): 
        dt2 (date): 
        
    Returns:
        int or None
    """
    if dt1.month == dt2.month and dt1.day == dt2.day:
        return abs(dt1.year - dt2.year)
    else:
        return None


# In[16]:


def birth_dates():
    """Returns dictionary with dates of all births in events dictionary.
    
    Returns:
        Dict
    """
    birth_dict = {}
    for k, v in events.items():
        if v['category'] == 'birth':
            birth_dict[k] = v['dt']    
    return birth_dict


# ## 2.2. Functions for FastAPI

# In[99]:


def some_day_counter(dt_str=None):
    """Calculates amounts of days from each event in events dictionary to `dt_str`.
    
    Args:
        dt_str (str, optional): The string date in `DATE_FORMAT` format. Default value is None and uses for today's date.
        
    Returns:
        DataFrame
    """
    birth_dict = birth_dates()
    output_dict = {}
    
    try:
        if dt_str is None:
            dt = TODAY_DT
        else:
            dt = stod(dt_str)
            
        for event in events.keys():
            output_dict["Since {0}".format(event)] = days_between(dt, events[event]['dt'])
    
        for k in birth_dict.keys():
            output_dict["Age: {0}".format(k)] = days_between(dt, birth_dict[k])

        if len(birth_dict.keys()) > 1:
            output_dict["Age: total"] = sum([days_between(dt, birth_dict[k]) for k in birth_dict.keys()])

    except:
        print("Something wrong happened...")

    if len(output_dict):
        return pd.DataFrame.from_dict(output_dict, orient='index', columns=['days'])
    else:
        return "Sorry, there is no answer :("
    


# In[81]:


# def age_counter(dt_str=None):
#     """Returns dataframe with data about ages (in days) at `dt_str`.
    
#     Args:
#         dt_str (str, optional): The string date in `DATE_FORMAT` format. Default value is None and uses for today's date.
    
#     Returns:
#         DataFrame
#     """
#     birth_dict = birth_dates()
#     output_dict = {}
    
#     try:
#         if dt_str is None:
#             dt = TODAY_DT
#         else:
#             dt = stod(dt_str)
            
#         for k in birth_dict.keys():
#             output_dict["{0}'s age".format(k)] = days_between(dt, birth_dict[k])

#         if len(birth_dict.keys()) > 1:
#             output_dict["Total age"] = sum([days_between(dt, birth_dict[k]) for k in birth_dict.keys()])
#             for (k1, k2) in combinations(birth_dict.keys(), 2):
#                 output_dict["Age difference between {0} and {1}".format(k1, k2)] = days_between(birth_dict[k1], birth_dict[k2])
    
#     except:
#         print("Something wrong happened...")

#     if len(output_dict):
#         return pd.DataFrame.from_dict(output_dict, orient='index', columns=['days'])
#     else:
#         return "Sorry, there is no answer :("
    


# In[132]:


def range_calendar(start_dt_str, end_dt_str, n=1000):
    """Returns anniversaries from `start_dt_str` to `end_dt_str`.
    
    Args:
        start_dt_str (str): The string date in `DATE_FORMAT` format.
        end_dt_str (str): The string date in `DATE_FORMAT` format.
        n (int, optional): The number for checking multiplicity (more or equal 10). Default value is 1000.
    
    Returns:
        DataFrame
    """
    start_dt = stod(start_dt_str)
    end_dt = stod(end_dt_str)
    start_dt, end_dt = sorted([start_dt, end_dt])
    
    birth_dict = birth_dates()
    output_df_set = []
    
    try:
        for dt in daterange(start_dt, end_dt):
            for event in events.keys():
                event_dt = events[event]['dt']
                if (
                    (rule_multiple(dt, event_dt, 100) and events[event]['importance'] <= 2)
                    or
                    (rule_multiple(dt, event_dt, 1000) and events[event]['importance'] == 3)
                ):
                    temp_dict = {'date': dt.strftime('%Y-%m-%d'),
                                 'event': event, 
                                 'amount': days_between(dt, event_dt), 
                                 'unit': 'day'}
                    temp_df = pd.DataFrame.from_dict(temp_dict, orient='index').transpose()
                    output_df_set.append(temp_df)
                if rule_anniversary(dt, event_dt):
                    temp_dict = {'date': dt.strftime('%Y-%m-%d'),
                                 'event': event, 
                                 'amount': rule_anniversary(dt, event_dt), 
                                 'unit': 'year'}
                    temp_df = pd.DataFrame.from_dict(temp_dict, orient='index').transpose()
                    output_df_set.append(temp_df)
            total_age = sum([days_between(dt, birth_dict[k]) for k in birth_dict.keys()])
            if n >= 10 and total_age % n in range(len(birth_dict)):
                temp_dict = {'date': dt.strftime('%Y-%m-%d'),
                             'event': 'Total age ({})'.format(", ".join(birth_dict.keys())), 
                             'amount': total_age, 
                             'unit': 'day'}
                temp_df = pd.DataFrame.from_dict(temp_dict, orient='index').transpose()
                output_df_set.append(temp_df)
    
    except:
        print("Something wrong happened...")

    if len(output_df_set):
        return pd.concat(output_df_set).reset_index(drop=True)
    else:
        return "Sorry, there is no answer :("


# In[90]:


# def total_age_anniversaries(start_dt_str, end_dt_str, n=1000):
#     """Returns dates from `start_dt` to `end_dt` in which total age (in days) 
#     is close to be multiple of `n`.
    
#     Args:
#         start_dt_str (str): The string date in `DATE_FORMAT` format.
#         end_dt_str (str): The string date in `DATE_FORMAT` format.
#         n (int, optional): The number for checking multiplicity (more or equal 10). Default value is 1000.
    
#     Returns:
#         DataFrame
#     """
#     start_dt = stod(start_dt_str)
#     end_dt = stod(end_dt_str)
#     start_dt, end_dt = sorted([start_dt, end_dt])
    
#     birth_dict = birth_dates()
#     output_dict = {}
    
#     try:
#         for dt in daterange(start_dt, end_dt):
#             total_age = sum([days_between(dt, birth_dict[k]) for k in birth_dict.keys()])
#             if n >= 10 and total_age % n in range(len(birth_dict)):
#                 output_dict[dt.strftime('%Y-%m-%d')] = total_age
#     except:
#         print("Something wrong happened...")
    
#     if len(output_dict):
#         return pd.DataFrame.from_dict(output_dict, orient='index', columns=['days'])
#     else:
#         return "Sorry, there is no answer :("
    


# In[105]:


def differences_inside_set(n=100):
    """Returns DataFrame with round dates (in days) between events in events dictionary.
    
    Args:
        n (int, optional): The base of round dates. Default value is 100. 
        
    Returns:
        DataFrame
    """
    birth_dict = birth_dates()
    inside_dict = {}

    try:
        if len(events.keys()) > 1:
            for (event1, event2) in combinations(events.keys(), 2):
                if (
                    days_between(events[event1]['dt'], events[event2]['dt']) % n == 0 and 
                    event1 != event2 and 
                    events[event1]['dt'] < events[event2]['dt']
                ):
                    inside_dict["Between {} and {}".format(event1, event2)] = days_between(events[event1]['dt'], events[event2]['dt'])
        if len(birth_dict.keys()) > 1:
            for (k1, k2) in combinations(birth_dict.keys(), 2):
                inside_dict["Age: difference between {0} and {1}".format(k1, k2)] = days_between(birth_dict[k1], birth_dict[k2])

    except:
        print("Something wrong happened...")

    if len(inside_dict):
        return pd.DataFrame.from_dict(inside_dict, orient='index', columns=['days'])
    else:
        return "Sorry, there is no answer :("



# # 3. Performing

# In[63]:


today_dt_str = TODAY_DT.strftime(DATE_FORMAT)
today_dt_str


# In[100]:


some_day_counter() # ok
# some_day_counter('2023-05-22') # ok
# some_day_counter('kek') # ok

# ok


# In[114]:


# dt_str = events["Philip's death"]['date']

# age_counter()
# age_counter(dt_str)
# age_counter("")

# ok


# In[133]:


range_calendar('2021-01-01', '2021-03-01') 

# ok


# In[113]:


# start_dt = events['Engagement']['date']
# end_dt = events["Philip's death"]['date']

# total_age_anniversaries(start_dt, end_dt)
# total_age_anniversaries(start_dt, "")

# ok


# In[106]:


# differences_inside_set()

# ok


# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:


# str -> date: datetime.strptime(dt, "%Y-%m-%d").date()
# date -> str: dt.strftime('%Y-%m-%d')

#  in 'YYYY-MM-DD' format


# In[ ]:





# In[29]:


if __name__=="__main__":
    print(age_counter('2021-04-09'))


# In[ ]:




