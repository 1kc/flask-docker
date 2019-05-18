FROM alpine:3.8

RUN apk add --no-cache bash python3 python3-dev build-base linux-headers pcre-dev

# Set the working directory to /app in the container

WORKDIR /app

ADD . /app

# RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# run uwsgi as root
# CMD [ "uwsgi", "app.ini" ]

# CMD [ "uwsgi", "dev.ini" ]

# Flask dev server
CMD [ "python3", "app.py" ]

# uWSGI
EXPOSE 5000
