# Dash App - Dashboard

The dashboard is build via [Dash](https://dash.plotly.com/).

## Docker Build

The container can be build via:
````
docker build . -t ds20m007/sdc-dash_app:latest --build-arg kaggle_user=user --build-arg kaggle_token=token
````
In order for the build to work, kaggle user and a kaggle api token have to be inserted. More Information about the kaggle api can be found [here](https://github.com/Kaggle/kaggle-api).

## Run

Start the container with:
```
docker run -p 8000:8000 -it dash_app:latest
```
