#!/usr/bin/env python
# coding: utf-8

# In[4]:


from anniversary_counter import age_counter_2

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
async def get_anniv(date: str):
    return {"Age counter:": age_counter_2(date)}

@app.get("/date/{form}")
def form_post(request: Request):
    result = "Write a date in format YYYY-MM-DD"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})

# @app.post("/date/{form}")
# def form_post(request: Request, date: str = Form(...)):
#     result = age_counter_2(date)
#     return templates.TemplateResponse('form.html', context={'request': request, 'result': result.to_html()})



# In[8]:


# uvicorn main:app --reload


# In[ ]:




