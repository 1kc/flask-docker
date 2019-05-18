FROM nginx:1.15

COPY nginx.conf /etc/nginx/nginx.conf

# Ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

RUN apt-get update && apt-get install \
    -y --no-install-recommends \
            python3 \
            python3-dev \
            build-essential \
            python3-pip \
            python3-setuptools \
            vim

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

# Set the working directory to /app in the container
WORKDIR /app

# Copy the app directory contents into the container at /app
COPY ./app /app

# CMD ["uwsgi", "--ini", "app.ini"]

EXPOSE 80
EXPOSE 5000
