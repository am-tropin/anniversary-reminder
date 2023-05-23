# Anniversary Reminder

The project calculates round dates basing on a list of events and provides FastAPI service for launching with arbitrary dates.

Libraries: pandas, datetime, itertools, fastapi



## Table of contents
- [Dataset](#Dataset)
- [Guide](#Guide)


## Dataset

You can use [a default dataset with events of Elizabeth II and Prince Philip's lifes](https://github.com/am-tropin/anniversary-reminder/blob/main/events.csv) or you can create your own **event.csv** file with the same structure. 


## Guide

1. Run **git clone https://github.com/am-tropin/anniversary-reminder** on terminal

2. Create the environment with **cd anniversary-reminder**

3. Run the project with **uvicorn main:app --reload**

4. Go to **http://127.0.0.1:8000/docs/** and use boxes with green **POST**.

