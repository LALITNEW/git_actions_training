# use a python image
FROM python:3.6

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
COPY . /app

# pip install flask
RUN python /app/hello.py