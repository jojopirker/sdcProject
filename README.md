# Solution Deployment and Communication Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is the Github Page for our SDC Project.

**Build with:**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

**Deployed to:**

![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=azure-devops&logoColor=white)

**Using:**

![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)

## General

The structure of this repo is the following:
````
-- backend
contains all the files for our backend
-- frontend
contains all our frontend files
-- dash_app
contains the dash app, which is integrated into our frontend
-- data
empty folder for local usage, see /data/README.md
-- notebooks
contains all the notebooks used for data analysis etc. 
````

## Data

[The Dataset](https://www.kaggle.com/benoit72/uk-accidents-10-years-history-with-many-variables) is from Kaggle. It representscar accidents in the UK over a timeframe of about 10 years.

## Build

To build run (after substituting *user* and *token*)
````
docker-compose build --build-arg kaggle_user=user --build-arg kaggle_token=token
````

## Run
After building you can start the project simply via:
````
docker compose up
````
## TODO

* Descriptive Analysis
* Train ML model (serverity ~ .)
* Create Dash App
* Update Frontend
* Create Flask Backend
* Setup Azure AppServices
* Create Github Actions

## Deployment
The project ~~is~~ (TODO: will be) deployed to Azure.


