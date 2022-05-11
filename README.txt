Dockerfile :
this file is created in order to create my own container image.

the image is based on python 3.8

the flask webserver is written in the FlaskTask file outside of the container

i used the command RUN pip install flask to install the necessary dependency

i used COPY command to copy the flask file into the container 

then the last command which should be run while running the cintainer is :
CMD ["python3", "FlaskTask.py"]

to execute the flask file.


about the FlaskTask.py :
first i import the necessary library and then i create an instance of Flask webserver

we need to use decorators in order to modify the functions that will handle an event

in our case the event is redirecting requests.

when a user enter his localhost it will display the home page.
when a user enter the localhost/ping it will get a response PONG
when a user is trying to access unavailable URL it will get an error NOT FOUND.



