FROM nginx
WORKDIR /home/ubuntu/docker-nginx/html
COPY . /usr/share/nginx/html/
EXPOSE 80
