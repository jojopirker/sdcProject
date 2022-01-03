FROM nginx:alpine


RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80

COPY sdc-frontend/build /usr/share/nginx/html