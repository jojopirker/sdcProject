# Dash App - Dashboard

The dashboard is build via [Dash](https://dash.plotly.com/).

## Docker Build

The container can be build via
````
docker build . -t dash_app:latest --build-arg kaggle_user=user --build-arg kaggle_token=token
````
In order to work,kaggle user and api token have to be inserted. See [here](https://github.com/Kaggle/kaggle-api) for more information on the kaggle api

## Run

Start the container with
```
docker run -p 8000:8000 -it dash_app:latest
```
