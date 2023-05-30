#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pytest


# In[15]:


from datetime import datetime


# In[16]:


import sys
sys.path.append('../')
from functions.functions_store import stod, daterange
from functions.functions_store import check_roundness, check_same_digits, check_palindrome, check_monotonous, check_power_of_2
from functions.functions_store import rule_anniversary, rule_days_divisibility, rule_weeks_divisibility
# from functions.functions_store import some_day_counter, range_calendar, internal_counter


# In[ ]:





# In[ ]:


# depend on ../event.csv:

# event_dict
# birth_dates
# some_day_counter
# range_calendar
# internal_counter


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
    assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2022, month=6, day=31).date(), 2) is None

# def test_for_corr_rule_days_divisibility():
#     assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=7, day=31).date(), 2) == 1

# def test_for_same_rule_days_divisibility():
#     assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2023, month=7, day=31).date()) is None

# def test_for_not_rule_days_divisibility():
#     assert rule_days_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2024, month=7, day=31).date()) is None


# In[ ]:


def test_for_past_rule_weeks_divisibility():
    assert rule_weeks_divisibility(datetime(year=2023, month=5, day=30).date(), datetime(year=2022, month=6, day=31).date(), 2) is None



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




