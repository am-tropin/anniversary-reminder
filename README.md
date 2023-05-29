# Anniversary Reminder

The project calculates round dates basing on a list of events and provides FastAPI service for launching with arbitrary dates.

Libraries: pandas, datetime, itertools, fastapi

[![codecov.io](https://codecov.io/gh/am-tropin/anniversary-reminder/coverage.svg?branch=master)]
(https://codecov.io/gh/am-tropin/anniversary-reminder?branch=master)
  

## Table of contents
- [Dataset](#dataset)
- [Guide](#guide)
- [Rules](#rules)


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
and use on of the following boxes to get info in dictionary view:

- **Get Some Day Counter**: Type a date in format YYYY-MM-DD and know how many days how many days have passed since each event.
- **Get Range Calendar**: Type start and end dates in format YYYY-MM-DD and know the anniversaries based on list of rules (see below). 
- **Get Internal Counter**: Type integer number **n** and know all pairs of events with date distances based on **n**.

Or

5. Go to web-browser and use one the following links to get the same info in table view:

- 5.1.
```bash
  http://127.0.0.1:8000/some_day/_
```

- 5.2.
```bash
  http://127.0.0.1:8000/range/_
```

- 5.3.
```bash
  http://127.0.0.1:8000/internal/_
```

Or 

6. Go to web-browser and use one the following types of links to get the same info in clear dictionary view:

- 6.1.
```bash
  http://127.0.0.1:8000/some_day_counter/2023-05-28
```

- 6.2.
```bash
  http://127.0.0.1:8000/range_calendar/2023-05-28_2023-10-28
```

- 6.3.
```bash
  http://127.0.0.1:8000/internal_counter/10
```


## Rules

- 1. Classical anniversary in terms of **years** (your date and event date have equal day number and equal month number).

- 2. Arithmetic anniversary in terms of **days**:
    - 1. Round amount of days (divided by 1000 if length >= 4 (for instance, **4000**), divided by 100 if length < 4 (for instance, **500**)); 
    - 2. Amount of days consisted of the same digits if length >= 3 (for instance, **111**); 
    - 3. Monotonous and consistent amount of days if length >= 3 (for instance, **1234** or **987**);
    - 4. Amount of days is palindrome if length >= 4 (for instance, **2552**);

- 3. Arithmetic anniversary in terms of **weeks**:
    - 1. Round amount of weeks (divided by 100 if length >= 3 (for instance, **400**), divided by 10 if length < 3 (for instance, **50**)); 
    - 2. Amount of weeks consisted of the same digits if length >= 3 (for instance, **111**); 
    - 3. Monotonous and consistent amount of weeks if length >= 3 (for instance, **1234** or **987**);
    - 4. Amount of weeks is palindrome if length >= 4 (for instance, **2552**);
