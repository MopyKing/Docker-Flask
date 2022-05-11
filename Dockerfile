#!bin/bash
#this image will be using python 3.8
FROM python:3.8

# the next command will copy the necessary files from my directory into the container
COPY ./FlaskTask.py FlaskTask.py

# the command will install flask on the container
RUN pip install flask

# last command is the command that will be executed when running the container
# in this case the python script.
CMD ["python3", "FlaskTask.py"]

