# Frontend
The frontend is build using [React](https://reactjs.org/). 

## Build
To build the frontend run 
````
npm install
npm run build
````

Then it is possilbe to build the docker container with
````
docker build . -t frontend:latest
````

## Run
After the container was build, it can be easily started with
`````
docker run -p 8081:80 -it frontend:latest
`````
