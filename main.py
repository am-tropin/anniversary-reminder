#!/usr/bin/env python
# coding: utf-8

# In[4]:


from functions_store import some_day_counter, range_calendar, total_age_anniversaries, differences_inside_set

# API
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates


# In[6]:


app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/")
async def root():
    return "Welcome to the Anniversary Reminder!"


@app.get("/{date}")
async def get_anniv_for_some_day(date: str):
    return {"Age counter:": some_day_counter(date)}


@app.get("/date/{form_some_day}")
def form_post(request: Request):
    result = "Write a date as YYYY-MM-DD"
    return templates.TemplateResponse('form_some_day.html', context={'request': request, 'result': result})


@app.post("/date/{form_some_day}")
def form_post(request: Request, date: str = Form(...)):
    result = some_day_counter(date)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result.to_html()})

