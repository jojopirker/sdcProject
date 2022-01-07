# Solution Deployment and Communication Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is the Github Page for our SDC Project.

__Pipline Status__

![Frontend](https://github.com/ds20m007/sdcProject/actions/workflows/frontend_build.yml/badge.svg)
![Dashboard](https://github.com/ds20m007/sdcProject/actions/workflows/dash_app_build.yml/badge.svg)
![Backend](https://github.com/ds20m007/sdcProject/actions/workflows/backend_build.yml/badge.svg)

**Build with:**

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://www.javascript.com/)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)](https://reactjs.org/)
[![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

**Deployed to:**

[![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=azure-devops&logoColor=white)](https://azure.microsoft.com)

**Using:**

[![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)](https://www.nginx.com/)


## Data

[The Dataset](https://www.kaggle.com/benoit72/uk-accidents-10-years-history-with-many-variables) is from Kaggle. It representscar accidents in the UK over a timeframe of about 10 years.

## Deployment

![Deployment](https://github.com/ds20m007/sdcProject/blob/main/etc/infrastructure.jpeg)

The project ~~is~~ (TODO: will be) deployed to Azure.

## Project Structure

The structure of this repo is the following:

#### /backend
contains all the files for our backend
#### /frontend
contains all our frontend files
#### /dash_app
contains the dash app, which is integrated into our frontend
#### /data
empty folder for local usage, see /data/README.md
#### /notebooks
contains all the notebooks used for data analysis etc. 

## Build
First you'll need to install node.js. Then you can build the frontend. In the **/frontend/sdc-frontend/** folder run:
```
npm install
```
and (for *local* testing, for production substitute *local* for *prod*)
```
npm run build:local
```

To build all docker containers run (after substituting *user* and *token*) in the **root project folder**:
````
docker-compose build --build-arg kaggle_user=user --build-arg kaggle_token=token
````

## Run
After building you can start the project simply via:
````
docker compose up
````

And point your browser to *localhost*



## TODO

- [x] Descriptive Analysis
- [x] Train ML model (serverity ~ .)
- [x] Create Dash App
- [x] Update Frontend
- [x] Create Flask Backend
- [x] Create Github Actions
- [x] Update Dash App
- [ ] Setup Azure AppServices
- [ ] Update backend with model




