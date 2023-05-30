#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pytest


# In[5]:


import sys
sys.path.append('../')
from functions.functions_store import check_same_digits, check_palindrome, check_monotonous, check_power_of_2


# In[ ]:





# In[9]:


def test_for_corr_stod():
    assert stod("2023-05-30") == datetime.date(2023, 5, 30)
    
def test_for_incorr_stod():
    with pytest.raises(ValueError, match="Incorrect data format, should be YYYY-MM-DD"):
                       validate_timestamp("202-05-30")


# In[ ]:





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
    


# In[ ]:





# In[ ]:




