# Solution Deployment and Communication Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Status](https://img.shields.io/website?label=frontend&url=http%3A%2F%2Fsdc-project.azurewebsites.net)

This is the Github Page for our SDC Project.

__Pipline Status__

*Builds:*

![Frontend](https://github.com/ds20m007/sdcProject/actions/workflows/frontend_build.yml/badge.svg)
![Dashboard](https://github.com/ds20m007/sdcProject/actions/workflows/dash_app_build.yml/badge.svg)
![Backend](https://github.com/ds20m007/sdcProject/actions/workflows/backend_build.yml/badge.svg)

*Deployment:*

![Backend](https://github.com/ds20m007/sdcProject/actions/workflows/azure_deploy.yml/badge.svg)

**Build with:**

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://www.javascript.com/)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)](https://reactjs.org/)
[![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)](https://www.nginx.com/)

**Deployed to:**

[![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=azure-devops&logoColor=white)](https://azure.microsoft.com)


## Data

[The Dataset](https://www.kaggle.com/benoit72/uk-accidents-10-years-history-with-many-variables) is from Kaggle. It represents car accidents in the UK over a time-frame of about 10 years.

## Deployment

The current deployed version can be visited under: http://sdc-project.azurewebsites.net. It gets automatically built and pushed on every new commit. 

*Below is a schematic of our pipline for deployment:*

![Pipleines](https://github.com/ds20m007/sdcProject/blob/main/etc/actions.png)

*And here a little overview of the infrastructure used in deployment:*

![Deployment](https://github.com/ds20m007/sdcProject/blob/main/etc/infrastructure.jpeg)

## Project Structure

The structure of this repo is the following:

Folder | Details  
--- | ---
/backend | contains all the files for our backend
/frontend | contains all our frontend files 
/dash_app | contains the dash app, which is integrated into our frontend 
/data | empty folder for local usage, see /data/README.md 
/etc | contains additional content for the project (for example pics) 
/notebooks | contains all the notebooks used for data analysis etc. 

## Build
First you'll need to install node.js. Then you can build the frontend. Inside the **/frontend/sdc-frontend/** folder run:
```
npm install
```
and (for *local* testing, for production substitute *local* for *prod*)
```
npm run build:local
```

Sidenote: Since env-cmd is used this command will not work on standard Windows cmd or Powershell. Execute the following commands prior to solve this:

```
npm update

npm install dotenv --save
```

To build all docker containers run (after substituting *user* and *token*) in the **root project folder**:
````
docker compose build --build-arg kaggle_user=user --build-arg kaggle_token=token
````

## Run
After building you can start the project simply via:
````
docker compose up
````

And point your browser to *localhost*

## Known Problems

### Dash-App Building Process
Error | Details | Solution
--- | --- | ---
401 | The credentials are wrong. | -
403 | The credentials are wrong. | -
404 | The dataset cannot be found on kaggle. | Run the build again.  
416 | The contigent for downloading the dataset was already used. | The process needs to be run again the next day.

### Frontend 
Error | Details | Solution
--- | --- | ---
env-cmd | env-cmd is used and does not work. | run commands found under *Build*

## TODO

- [x] Descriptive Analysis
- [x] Train ML model (serverity ~ .)
- [x] Create Dash App
- [x] Update Frontend
- [x] Create Flask Backend
- [x] Create Github Actions
- [x] Change Layout Dash App
- [x] Update Dash App
- [x] Add Filters to Dash App 1
- [x] Add Filters to Dash App 2
- [x] Setup Azure AppServices
- [x] Update backend with model
- [ ] Add Data Table Overview to GeneralInformation Page




