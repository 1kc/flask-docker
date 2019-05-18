#!/usr/bin/env bash

# --rm delete all stopped containers
# -d for detached mode
# sudo docker run -p 5000:5000 flask-docker
# docker run -p 5000:5000 -it flask-docker /bin/bash

docker run -p 5000:5000 flask-docker
