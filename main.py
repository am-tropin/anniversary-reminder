#!/usr/bin/env python
# coding: utf-8

# In[4]:


from functions_store import some_day_counter, range_calendar, internal_counter

# API
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates


# In[6]:


app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/")
async def root():
    return "Welcome to the Anniversary Reminder!"


# without html

@app.get("/some_day_counter/{date}")
async def get_some_day_counter(date: str):
    return some_day_counter(date).to_dict()

@app.get("/range_calendar/{date}")
async def get_range_calendar(date1: str, date2: str, n: int):
    return range_calendar(date1, date2, n).to_dict()

@app.get("/internal_counter/{date}")
async def get_internal_counter(n: int):
    return internal_counter(n).to_dict()


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

@app.get("/{date1}_{date2}")
async def get_anniv_for_range(date1: str, date2: str):
    return {"Anniversaries in the range:": range_calendar(date1, date2)}

@app.get("/date1_date2/{form_range}")
def form_post_range(request: Request):
    result = "Write dates as YYYY-MM-DD"
    return templates.TemplateResponse('form_range.html', context={'request': request, 'result': result})

@app.post("/date1_date2/{form_range}")
def form_post_range(request: Request, date1: str = Form(...), date2: str = Form(...)):
    result = range_calendar(date1, date2)
    return templates.TemplateResponse('form_range.html', context={'request': request, 'result': result.to_html()})

