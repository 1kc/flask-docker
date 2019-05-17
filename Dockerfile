FROM nginx:1.15

# Ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

RUN apt-get update && apt-get install \
    -y --no-install-recommends \
            python3 \
            python3-pip \
            python3-dev \
            build-essential \
            python3-setuptools \
            python3-virtualenv \
            vim

# Activate virtual env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m virtualenv --python=/usr/bin/python3 $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt

# Serve the static content by nginx directly
COPY ./static /usr/share/nginx/html/

# Set the working directory to /app in the container
WORKDIR /app

# Copy the app directory contents into the container at /app
COPY ./app /app

EXPOSE 80
