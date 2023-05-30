#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[18]:


import pandas as pd 
from datetime import datetime, date, timedelta
from itertools import combinations


# In[2]:


# DATE_FORMAT = "%Y-%m-%d"
# TODAY_DT = date.today() #.strftime(DATE_FORMAT)


# # 1. Functions

# ## 1.1. Loading the csv of dates

# In[12]:


def event_dict():
    events_df = pd.read_csv("../events.csv")
    DATE_FORMAT = "%Y-%m-%d"
    
    # adding a column dt with format datetime.date()
    events_df['dt'] = events_df['date'].apply(lambda x: datetime.strptime(x, DATE_FORMAT).date())
    events = events_df.set_index('event').transpose().to_dict()

    return events


# In[15]:


# events = event_dict()
# events


# ## 1.2. Secondary functions

# In[40]:


def stod(dt_str):
    """Converts string variable `dt_str` to datetime.date.
    
    Args:
        dt_str (str): The string date in `DATE_FORMAT` format.
        
    Returns:
        Date or ValueError
    """
    DATE_FORMAT = "%Y-%m-%d"
    try:
        return datetime.strptime(dt_str, DATE_FORMAT).date()
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


# In[47]:


# dt_str = ""
# dt_str = "kek"
# dt_str = "2023-05-30"
# print(stod(dt_str), type(stod(dt_str)))


# In[51]:


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


# In[48]:


def check_roundness(n, p, d):
    """Identifies if number `n` is round depending on parameters `p` and `d`.
    
    Args:
        n (int): The number.
        p (int): The number of importance.
        d (int): The number for degree of 10.
        
    Returns:
        bool
    """
    if p in [1, 2, 3]:
        if n >= (10**(d+1)):
            if n % (10**(d+1)) == 0:
                return True
            else: 
                return False
        else:
            if (n % (10**d) == 0 and p <= 2):
                return True
            else:
                return False
    else:
        raise ValueError("Incorrect data format of importance, should be in 1, 2 or 3.")
        
        
def check_same_digits(n):
    """Identifies if number `n` consists of the same digits.
    
    Args:
        n (int): The number.
        
    Returns:
        bool
        
    >>> check_same_digits(111)
    True
        
    >>> check_same_digits(11)
    False
        
    >>> check_same_digits(112)
    False
    """
    if len(set(list(str(n)))) == 1 and len(str(n)) >= 3:
        return True
    else:
        return False

def check_palindrome(n):
    """Identifies if number `n` is palindrome.
    
    Args:
        n (int): The number.
        
    Returns:
        bool
        
    >>> check_palindrome(1221)
    True
    
    >>> check_palindrome(121)
    False
    
    >>> check_palindrome(1231)
    False
    """
    if str(n) == str(n)[::-1] and len(str(n)) >= 4:
        return True
    else:
        return False
    
def check_monotonous(n):
    """Identifies if digit sequence of number `n` is monotonous and consistent 
    (for instance, 1234 or 543).
    
    Args:
        n (int): The number.
        
    Returns:
        bool
        
    >>> check_monotonous(1234)
    True
        
    >>> check_monotonous(543)
    True
        
    >>> check_monotonous(103)
    False
        
    >>> check_monotonous(1223)
    False
    """
    dig = list(map(int, str(n)))
    if len(dig) == len(set(dig)) and dig in [sorted(dig), sorted(dig)[::-1]] and abs(dig[0] - dig[-1]) + 1 == len(dig) and len(dig) >= 3:
        return True
    else:
        return False
    
def check_power_of_2(n):
    """Identifies if number `n` is a power of 2 and >= 32.
    
    Args:
        n (int): The number.
        
    Returns:
        bool
        
    >>> check_power_of_2(16)
    False
        
    >>> check_power_of_2(32)
    True
    
    >>> check_power_of_2(33)
    False
    """
    if (n & (n - 1) == 0) and n >= 32:
        return True
    else:
        return False


# In[279]:


# rules for detecting anniversaries

def rule_anniversary(dt1, dt2):
    """Identifies if `dt1` is an anniversary of `dt2` or vice versa.
    
    Args:
        dt1 (date): Date of event.
        dt2 (date): Arbitrary date.
        
    Returns:
        int or None
    """
    if dt1 < dt2 and dt1.month == dt2.month and dt1.day == dt2.day:
        return (dt2.year - dt1.year)
    else:
        return None

def rule_days_divisibility(dt1, dt2, imp):
    """Identifies if difference between `dt1` and `dt2` has one of described number properties.
    
    Args:
        dt1 (date): Date of event.
        dt2 (date): Arbitrary date.
        imp (int): Importance of dt2.
        
    Returns:
        int or None
    """
    day_s = (dt2 - dt1).days
    
    if dt1 < dt2 and (
#         day amount is divided by 100 or 1000 
        check_roundness(day_s, imp, 2)
        or
#         day amount consists of the same digits
        check_same_digits(day_s)
        or
#         day amount is monotonous and consistent sequence
        check_monotonous(day_s)
        or
#         day amount is a power of 2 and not very small
        check_power_of_2(day_s)
    ):
        return day_s
    else:
        return None

def rule_weeks_divisibility(dt1, dt2, imp):
    """Identifies if difference between `dt1` and `dt2` is a exact number of weeks 
    and this number has one of described number properties.
    
    Args:
        dt1 (date): Date of event.
        dt2 (date): Arbitrary date.
        imp (int): Importance of dt2.
        
    Returns:
        int or None
    """
    week_s = (dt2 - dt1).days // 7
    
    if dt1 < dt2 and (dt2 - dt1).days % 7 == 0 and (
#         week amount is divided by 10 or 100
        check_roundness(week_s, imp, 1)
        or
#         week amount consists of the same digits
        check_same_digits(week_s)
        or 
#         week amount is monotonous and consistent sequence
        check_monotonous(week_s)
        or
#         week amount is a power of 2 and not very small
        check_power_of_2(week_s)
    ):
        return week_s
    else:
        return None


# In[16]:


def birth_dates():
    """Returns dictionary with dates of all births in events dictionary.
    
    Returns:
        Dict
    """
    birth_dict = {}
    events = event_dict()
    for k, v in events.items():
        if v['category'] == 'birth':
            birth_dict[k] = v['dt']    
    return birth_dict


# ## 1.3. Functions for FastAPI

# In[137]:


def some_day_counter(dt_str=None):
    """Calculates amounts of days from each event in events dictionary to `dt_str`.
    
    Args:
        dt_str (str, optional): The string date in `DATE_FORMAT` format. Default value is None and uses for today's date.
        
    Returns:
        DataFrame
    """
    events = event_dict()
    birth_dict = birth_dates()
    output_dict = {}
    
    try:
        if dt_str is None:
            dt = date.today()
        else:
            dt = stod(dt_str)
    
        for k in birth_dict.keys():
            if dt >= birth_dict[k]:
                output_dict["Age: {0}".format(k)] = (dt - birth_dict[k]).days

        if len(birth_dict.keys()) > 1:
            output_dict["Age: total"] = sum([(dt - birth_dict[k]).days for k in birth_dict.keys() if dt >= birth_dict[k]])
            
        for event in events.keys():
            if events[event]['category'] != 'birth':
                if dt >= events[event]['dt']:
                    output_dict["From {0}".format(event)] = (dt - events[event]['dt']).days
                else:
                    output_dict["Before {0}".format(event)] = (events[event]['dt'] - dt).days

    except:
        print("Something wrong happened...")

    if len(output_dict):
        return pd.DataFrame.from_dict(output_dict, orient='index', columns=['days'])
    else:
        return "Sorry, there is no answer :("
    


# In[277]:


def range_calendar(start_dt_str, end_dt_str):
    """Returns anniversaries from `start_dt_str` to `end_dt_str`.
    
    Args:
        start_dt_str (str): The string date in `DATE_FORMAT` format.
        end_dt_str (str): The string date in `DATE_FORMAT` format.
    
    Returns:
        DataFrame
    """
    start_dt = stod(start_dt_str)
    end_dt = stod(end_dt_str)
    start_dt, end_dt = sorted([start_dt, end_dt])
    events = event_dict()
    birth_dict = birth_dates()
    output_df_set = []
    
    try:
        for dt in daterange(start_dt, end_dt):
            for event in events.keys():
                event_dt = events[event]['dt']
                event_imp = events[event]['importance']
                    
                if rule_anniversary(event_dt, dt):
                    temp_dict = {'date': dt.strftime('%Y-%m-%d'),
                                 'event': event, 
                                 'amount': rule_anniversary(event_dt, dt), 
                                 'unit': 'year'}
                    temp_df = pd.DataFrame.from_dict(temp_dict, orient='index').transpose()
                    output_df_set.append(temp_df)
                
                if rule_days_divisibility(event_dt, dt, event_imp):
                    temp_dict = {'date': dt.strftime('%Y-%m-%d'),
                                 'event': event, 
                                 'amount': rule_days_divisibility(event_dt, dt, event_imp), 
                                 'unit': 'day'}
                    temp_df = pd.DataFrame.from_dict(temp_dict, orient='index').transpose()
                    output_df_set.append(temp_df)
                    
                if rule_weeks_divisibility(event_dt, dt, event_imp):
                    temp_dict = {'date': dt.strftime('%Y-%m-%d'),
                                 'event': event, 
                                 'amount': rule_weeks_divisibility(event_dt, dt, event_imp), 
                                 'unit': 'week'}
                    temp_df = pd.DataFrame.from_dict(temp_dict, orient='index').transpose()
                    output_df_set.append(temp_df)
                                                    
            total_age = sum([(dt - birth_dict[k]).days for k in birth_dict.keys() if dt >= birth_dict[k]])
            if (
                total_age % 1000 in range(len(birth_dict))
                or
                check_same_digits(total_age)
                or
                check_monotonous(total_age)
                or
                check_power_of_2(total_age)
            ):
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


# In[171]:


def internal_counter(n=1):
    """Calculates distances between events in events dictionary with filtering by distances divided by `n`.
    
    Args:
        n (int, optional): The base of round dates. Default value is 1 for returning distances between all pairs of events. 
        
    Returns:
        DataFrame
    """
    events = event_dict()
    birth_dict = birth_dates()
    inside_dict = {}

    try:
        if len(birth_dict.keys()) > 1:
            for (k1, k2) in combinations(birth_dict.keys(), 2):
                if abs((birth_dict[k1] - birth_dict[k2]).days) % n == 0:
                    inside_dict["Age difference between {0} and {1}".format(k1, k2)] = abs((birth_dict[k1] - birth_dict[k2]).days)
        if len(events.keys()) > 1:
            for (event1, event2) in combinations(events.keys(), 2):
                if (events[event1]['category'], events[event2]['category']) != ('birth', 'birth') and (
                    abs((events[event1]['dt'] - events[event2]['dt']).days) % n == 0 and 
                    events[event1]['dt'] < events[event2]['dt']
                ):
                    inside_dict["From {} to {}".format(event1, event2)] = abs((events[event1]['dt'] - events[event2]['dt']).days)

    except:
        print("Something wrong happened...")

    if len(inside_dict):
        return pd.DataFrame.from_dict(inside_dict, orient='index', columns=['days'])
    else:
        return "Sorry, there is no answer :("



# # 2. Performing

# In[147]:


# DATE_FORMAT = "%Y-%m-%d"
# today_dt_str = date.today().strftime(DATE_FORMAT)
# today_dt_str


# In[142]:


# some_day_counter() # ok
# some_day_counter('2020-05-23') # ok
# some_day_counter('kek') # ok

# ok


# In[284]:


# range_calendar('2021-07-01', '2021-12-01') 

# ok


# In[170]:


# internal_counter()
# internal_counter(100)

# ok


# In[ ]:





# In[ ]:





# In[26]:


# str -> date: datetime.strptime(dt, "%Y-%m-%d").date()
# date -> str: dt.strftime('%Y-%m-%d')

#  in 'YYYY-MM-DD' format


# In[ ]:





# In[294]:


if __name__=="__main__":
    print(some_day_counter('2021-04-09'))


# In[ ]:





# In[ ]:





# In[ ]:





# # Testing

# In[ ]:





# In[293]:


import doctest
doctest.testmod()


# In[ ]:




