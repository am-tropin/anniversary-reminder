#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[123]:


import pandas as pd 
from datetime import datetime, date, timedelta
from itertools import combinations


# In[7]:


TODAY_DT = date.today().strftime("%Y-%m-%d")


# # 1. Loading the csv of dates

# In[150]:


events_df = pd.read_csv("events.csv")
events_df.head()


# In[151]:


events = events_df.set_index('event').transpose().to_dict()
events


# # 2. Functions

# In[166]:


def days_between(d1, d2):
    return abs((datetime.strptime(d2, "%Y-%m-%d") - datetime.strptime(d1, "%Y-%m-%d")).days)

def rule_multiple(dt1, dt2, n):
    if days_between(dt1.strftime('%Y-%m-%d'), dt2) % n == 0:
        return True
    else:
        return False

def anniversary(check_date, event_date):
    if check_date.month == event_date.month and check_date.day == event_date.day:
        return check_date.year - event_date.year
    else:
        return None


# In[44]:


# iterator by date
# date format of input args: date(YYYY, MM, DD)
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


# In[133]:


def today_counter(events):
    print("Today is...")
    for event in events.keys():
        print("{} days since {}".format(days_between(TODAY_DT, events[event]['date']), event))

def range_calendar(dt_start, dt_end):
    for dt in daterange(dt_start, dt_end):
        for event in events.keys():
            if (
                (rule_multiple(dt, events[event]['date'], 100) and events[event]['importance'] <= 2)
                or
                (rule_multiple(dt, events[event]['date'], 1000) and events[event]['importance'] == 3)
            ):
                print("{} -- {} days since {}".format(dt, days_between(dt.strftime('%Y-%m-%d'), events[event]['date']), event))
            if anniversary(dt, datetime.strptime(events[event]['date'], "%Y-%m-%d")):
                print("{} -- {} years since {}".format(dt, anniversary(dt, datetime.strptime(events[event]['date'], "%Y-%m-%d")), event))
            


# In[131]:


def age_counter(birthday_dt_1, birthday_dt_2, given_dt):
    print("Age difference: {} days".format(days_between(birthday_dt_1, birthday_dt_2)))
    print("Elizabeth II age: {} days".format(days_between(given_dt, birthday_dt_1)))
    print("Prince Philip age: {} days".format(days_between(given_dt, birthday_dt_2)))
    print("Total age: {} days".format(days_between(given_dt, birthday_dt_2) + days_between(given_dt, birthday_dt_1)))

def total_age_anniversaries(birthday_dt_1, birthday_dt_2, start_dt, end_dt):
    for dt in daterange(datetime.strptime(start_dt, "%Y-%m-%d"), datetime.strptime(end_dt, "%Y-%m-%d")):
        if (
            (days_between(dt.strftime('%Y-%m-%d'), birthday_dt_1) + days_between(dt.strftime('%Y-%m-%d'), birthday_dt_2)) % 1000 == 0
            or 
            (days_between(dt.strftime('%Y-%m-%d'), birthday_dt_1) + days_between(dt.strftime('%Y-%m-%d'), birthday_dt_2)) % 1000 == 1
        ):
            print("{} -- {} days of their combined age".format(dt.strftime('%Y-%m-%d'), 
                                                               days_between(dt.strftime('%Y-%m-%d'), birthday_dt_1) + days_between(dt.strftime('%Y-%m-%d'), birthday_dt_2)
                                                              ))

def differences_inside_set(events):
    for event1 in events.keys():
        for event2 in events.keys():
            if days_between(events[event1]['date'], events[event2]['date']) % 100 == 0 and event1 != event2 and events[event1]['date'] < events[event2]['date']:
                print("{} days between {} and {}".format(days_between(events[event1]['date'], events[event2]['date']), event1, event2))


# In[172]:


def age_counter_2(given_dt):
    birth_dict = {}
    for k, v in events.items():
        if v['category'] == 'birth':
            birth_dict[k] = v['date']

    try:
        for k in birth_dict.keys():
            print("{0}'s age: {1} days".format(k, days_between(given_dt, birth_dict[k])))

        if len(birth_dict.keys()) > 1:
            for (k1, k2) in combinations(birth_dict.keys(), 2):
                print("Age difference between {0} and {1}: {2} days".format(k1, k2, days_between(birth_dict[k1], birth_dict[k2])))
            print("Total age: {} days".format(sum([days_between(given_dt, birth_dict[k]) for k in birth_dict.keys()])))

    except:
        print("Something happens...")


# # 3. Performing

# In[175]:


# age_counter_2(given_dt)
# age_counter_2("")


# In[ ]:





# In[161]:


# today_counter(events)


# In[160]:


# range_calendar(date.today(), date(2023, 12, 31))


# In[129]:


# birthday_dt_1 = events["Elizabeth"]['date']
# birthday_dt_2 = events["Philip"]['date']
# given_dt = events["Philip's death"]['date']


# In[159]:


# age_counter(birthday_dt_1, birthday_dt_2, given_dt)


# In[157]:


# total_age_anniversaries(birthday_dt_1, birthday_dt_2, events['Engagement']['date'], events["Philip's death"]['date'])


# In[156]:


# differences_inside_set(events)


# In[ ]:





# In[ ]:





# In[155]:


if __name__=="__main__":
    print(age_counter_2('2021-04-09'))


# In[ ]:




