# Backend

The backend is using FastAPI to server our model.

## Build

```
docker build . -t ds20m007/sdc-backend:latest     
```

## Run

```
docker run -p 8000:8000 -it backend:latest
```

The currently used model is a kNN (due to performance issues of the randomForest Model) using the following variables as input features:

	Accidents: Day_of_Week, 1st_Road_Class, Weather_Conditions, Road_Surface_Conditions, Special_Conditions_at_Site, Urban_or_Rural_Area, Time of year (Season), Time of day, Longitude, Latitude
	Vehicles: Vehicle Types in Accident

Predicted will be the accident severity
