#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pytest


# In[10]:


from datetime import datetime
import pandas as pd


# In[1]:


import sys
sys.path.append('../')
from functions.functions_store import stod, daterange
from functions.functions_store import check_roundness, check_same_digits, check_palindrome, check_monotonous, check_power_of_2
from functions.functions_store import rule_anniversary, rule_days_divisibility, rule_weeks_divisibility
# from functions.functions_store import event_dict, birth_dates, total_age
from functions.functions_store import date_dict_to_df
# from functions.functions_store import some_day_counter, range_calendar, internal_counter, 
# from functions.functions_store import announcement_upcoming_month


# In[ ]:





# In[ ]:


# depend on ../event.csv:
# event_dict
# birth_dates
# total_age


# depend on announcement_monthly.txt:
# announcement_upcoming_month


# depend on other functions:

# rule_days_divisibility
# rule_weeks_divisibility

# some_day_counter
# range_calendar
# internal_counter


# In[9]:


def test_for_corr_stod():
    assert stod("2023-05-30") == datetime(year=2023, month=5, day=30).date()
    
def test_for_incorr_stod():
    with pytest.raises(ValueError, match="Incorrect data format, should be YYYY-MM-DD"):
        stod("202-05-30")


# In[17]:


def test_for_corr_daterange():
    assert list(daterange(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=6, day=1).date())) == [
        datetime(year=2023, month=5, day=30).date(), 
        datetime(year=2023, month=5, day=31).date(), 
        datetime(year=2023, month=6, day=1).date()]


# In[ ]:


def test_for_1_check_roundness():
    assert check_roundness(2000, 2, 2) is True

def test_for_2_check_roundness():
    assert check_roundness(1200, 2, 2) is False

def test_for_3_check_roundness():
    assert check_roundness(200, 2, 2) is True

def test_for_4_check_roundness():
    assert check_roundness(200, 3, 2) is False

def test_for_5_check_roundness():
    assert check_roundness(201, 2, 3) is False

def test_for_valuerror_check_roundness():
    with pytest.raises(ValueError, match="Incorrect data format of importance, should be in 1, 2 or 3."):
        check_roundness(500, 0, 2)


# In[7]:


def test_for_long_same_digits():
    assert check_same_digits(111) is True
    
def test_for_short_same_digits():
    assert check_same_digits(11) is False
    
def test_for_var_same_digits():
    assert check_same_digits(112) is False


# In[ ]:


def test_for_long_palindrome():
    assert check_palindrome(1221) is True
    
def test_for_short_palindrome():
    assert check_palindrome(121) is False
    
def test_for_var_palindrome():
    assert check_palindrome(1231) is False


# In[ ]:


def test_for_incr_monotonous():
    assert check_monotonous(1234) is True
    
def test_for_decr_monotonous():
    assert check_monotonous(543) is True
    
def test_for_no_monotonous():
    assert check_monotonous(103) is False
    
def test_for_dupl_monotonous():
    assert check_monotonous(1223) is False


# In[ ]:


def test_for_corr_power_of_2():
    assert check_power_of_2(32) is True
    
def test_for_incorr_power_of_2():
    assert check_power_of_2(33) is False

def test_for_small_power_of_2():
    assert check_power_of_2(16) is False
    


# In[ ]:


def test_for_corr_rule_anniversary():
    assert rule_anniversary(datetime(year=2023, month=5, day=30).date(), datetime(year=2024, month=5, day=30).date()) == 1

def test_for_same_rule_anniversary():
    assert rule_anniversary(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=5, day=30).date()) is None

def test_for_past_rule_anniversary():
    assert rule_anniversary(datetime(year=2023, month=5, day=30).date(), datetime(year=2022, month=5, day=30).date()) is None

def test_for_not_rule_anniversary():
    assert rule_anniversary(datetime(year=2023, month=5, day=30).date(), datetime(year=2024, month=5, day=31).date()) is None


# In[ ]:


def test_for_past_rule_days_divisibility():
    assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2022, month=7, day=31).date(), 2) is None

def test_for_f10_rule_days_divisibility():
    assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=7, day=31).date(), 2) == [None, 62][check_roundness(62, 2, 2)]

def test_for_f11_rule_days_divisibility():
    assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2024, month=3, day=25).date(), 2) == [None, 300][check_roundness(300, 2, 2)]

def test_for_f20_rule_days_divisibility():
    assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=7, day=31).date(), 2) == [None, 62][check_same_digits(62)]

def test_for_f21_rule_days_divisibility():
    assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=9, day=18).date(), 2) == [None, 111][check_same_digits(111)]

def test_for_f30_rule_days_divisibility():
    assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=7, day=31).date(), 2) == [None, 62][check_monotonous(62)]

def test_for_f31_rule_days_divisibility():
    assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=9, day=30).date(), 2) == [None, 123][check_monotonous(123)]

def test_for_f40_rule_days_divisibility():
    assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=7, day=31).date(), 2) == [None, 62][check_power_of_2(62)]

def test_for_f41_rule_days_divisibility():
    assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=8, day=2).date(), 2) == [None, 64][check_power_of_2(64)]


# In[ ]:


def test_for_past_rule_weeks_divisibility():
    assert rule_weeks_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2022, month=7, day=31).date(), 2) is None

def test_for_f10_rule_weeks_divisibility():
    assert rule_weeks_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=7, day=31).date(), 2) == None # 62, check_roundness

def test_for_f11_rule_weeks_divisibility():
    assert rule_weeks_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=8, day=8).date(), 2) == 10 # 70, check_roundness

# def test_for_f20_rule_weeks_divisibility():
#     assert rule_weeks_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=7, day=31).date(), 2) == None # 62, check_same_digits

def test_for_f21_rule_weeks_divisibility():
    assert rule_weeks_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2025, month=7, day=15).date(), 2) == 111 # 777, check_same_digits

# def test_for_f30_rule_weeks_divisibility():
#     assert rule_weeks_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=7, day=31).date(), 2) == None # 62, check_monotonous

def test_for_f31_rule_weeks_divisibility():
    assert rule_weeks_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2025, month=10, day=7).date(), 2) == 123 # 861, check_monotonous

# def test_for_f40_rule_weeks_divisibility():
#     assert rule_weeks_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=7, day=31).date(), 2) == None # 62, check_power_of_2

def test_for_f41_rule_weeks_divisibility():
    assert rule_weeks_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2024, month=1, day=9).date(), 2) == 32 # 224, check_power_of_2


# In[2]:


def test_for_notempty_date_dict_to_df():
    dict_1 = {'date': datetime(year=2023, month=5, day=29).date(),
              'event': 'event 1', 
              'amount': 5, 
              'unit': 'day'}
    df_1 = pd.DataFrame.from_dict(dict_1, orient='index').transpose()
    dict_2 = {'date': "2023-05-31",
                 'event': 'event 3', 
                 'amount': 32, 
                 'unit': 'day'}
    df_2 = pd.DataFrame.from_dict(dict_2, orient='index').transpose()
    assert pd.testing.assert_frame_equal(date_dict_to_df(df_1, datetime(year=2023, month=5, day=31).date(), 'event 3', 32, 'day'), pd.concat([df_1, df_2]).reset_index(drop=True)) is None

    
def test_for_empty_date_dict_to_df():
    null_df = pd.DataFrame(columns=['date', 'event', 'amount', 'unit'])
    dict_2 = {'date': "2023-05-31",
                 'event': 'event 3', 
                 'amount': 32, 
                 'unit': 'day'}
    df_2 = pd.DataFrame.from_dict(dict_2, orient='index').transpose()
    assert pd.testing.assert_frame_equal(date_dict_to_df(null_df, datetime(year=2023, month=5, day=31).date(), 'event 3', 32, 'day'), df_2) is None

    


# In[ ]:





# In[ ]:





# In[ ]:




