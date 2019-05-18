FROM alpine:3.8

RUN apk add --no-cache bash python3 python3-dev build-base linux-headers pcre-dev vim

# Set the working directory to /app in the container

WORKDIR /app

COPY ./app/requirements.txt /app

# RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the app directory contents into the container at /app
COPY ./app /app

# run uwsgi as root
# CMD [ "uwsgi", "app.ini" ]

CMD [ "uwsgi", "dev.ini" ]

# uWSGI
EXPOSE 5000
