#!/usr/bin/env bash

# --rm delete all stopped containers
# -d for detached mode
sudo docker run --rm -d -p 80:80 flask-docker
