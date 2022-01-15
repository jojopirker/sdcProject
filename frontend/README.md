# Frontend
The frontend is build using [React](https://reactjs.org/). 

## Build
To build the frontend run:
````
npm install
npm run build:local
````

Then it is possible to build the docker container with:
````
docker build . -t ds20m007/frontend:latest
````

## Run
After the container was build, it can easily be started with:
`````
docker run -p 8081:80 -it frontend:latest
`````

Alternatively it can also run locally via:
````
npm install
npm run start:local
````

