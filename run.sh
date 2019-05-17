#!/usr/bin/env bash

# --rm delete all stopped containers
# -d for detached mode
sudo docker run -p 80:80 -p 5000:5000 flask-docker
