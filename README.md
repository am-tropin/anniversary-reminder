# Anniversary Reminder

The project calculates round dates basing on a list of events and provides FastAPI service for launching with arbitrary dates.

Libraries: pandas, datetime, itertools, fastapi



## Table of contents
- [Dataset](#Dataset)
- [Guide](#Guide)


## Dataset

You can use [a default dataset with events of Elizabeth II and Prince Philip's lifes](https://github.com/am-tropin/anniversary-reminder/blob/main/events.csv) or you can create your own **event.csv** file with the same structure. 


## Run locally

1. Clone the project:
```bash
  git clone https://github.com/am-tropin/anniversary-reminder
```

2. Go to the project directory:
```bash
  cd anniversary-reminder
```

<!-- Create vitual enviroment and install dependencies
```bash
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
``` -->

3. Start the server:
```bash
  uvicorn main:app --reload
```

4. Go to web-browser 
```bash
  http://127.0.0.1:8000/docs/
```
and use on of the following boxes:

- **Get Some Day Counter**: Type a date in format YYYY-MM-DD and know how many days how many days have passed since each event.
- **Get Range Calendar**: Type start and end dates in format YYYY-MM-DD and integer number **n** and know the anniversaries based on **n** in this date range. 
- **Get Internal Counter**: Type integer number **n** and know all pairs of events with date distances based on **n**.
