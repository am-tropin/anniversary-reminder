#!/usr/bin/env python
# coding: utf-8

# In[4]:


from functions_store import some_day_counter, range_calendar, total_age_anniversaries, differences_inside_set

# API
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates


# In[6]:


@app.get("/")
async def root():
    return "Welcome to the Anniversary Reminder!"


# for some day

@app.get("/{date}")
async def get_anniv_for_some_day(date: str):
    return {"Duration to the date:": some_day_counter(date)}

@app.get("/date/{form_some_day}")
def form_post(request: Request):
    result = "Write a date as YYYY-MM-DD"
    return templates.TemplateResponse('form_some_day.html', context={'request': request, 'result': result})

@app.post("/date/{form_some_day}")
def form_post(request: Request, date: str = Form(...)):
    result = some_day_counter(date)
    return templates.TemplateResponse('form_some_day.html', context={'request': request, 'result': result.to_html()})


# for range

# @app.get("/{date1}_{date2}")
# async def get_anniv_for_range(date1: str, date2: str):
#     return {"Anniversaries in the range:": range_calendar(date1, date2)}

# @app.get("/date1_date2/{form_range}")
# def form_post_range(request: Request):
#     result = "Write dates as YYYY-MM-DD"
#     return templates.TemplateResponse('form_range.html', context={'request': request, 'result': result})

# @app.post("/date1_date2/{form_range}")
# def form_post_range(request: Request, date1: str = Form(...), date2: str = Form(...)):
#     result = range_calendar(date1, date2)
#     return templates.TemplateResponse('form_range.html', context={'request': request, 'result': result.to_html()})
