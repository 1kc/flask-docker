FROM alpine:3.8

RUN apk add --no-cache bash python3 python3-dev build-base linux-headers pcre-dev postgresql-dev musl-dev vim

# Set the working directory to /app in the container

WORKDIR /app

ADD . /app

# RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# run uwsgi as root with unix socket
CMD [ "uwsgi", "app.ini" ]

# run uwsgi as root on 5000
# CMD [ "uwsgi", "dev.ini" ]

# Flask dev server on 5000
# CMD [ "python3", "app.py" ]

# EXPOSE 5000
