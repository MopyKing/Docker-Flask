from flask import Flask, redirect, url_for

# initiating a flask insatnce, __NAME__ tells the flask which  location to look for the information
app = Flask(__name__)

# this is the decorator that flask uses in order to handle the routing of the URLS
# when a user will enter localhost:5000/ping he will get a response PONG
# the returned value will be rendered in the browser
@app.route("/ping")
def pong():
    return "<h1>PONG<h1>"

#this is the default route that will be handled when accessing localhost:5000
@app.route("/")
def home():
    return "<h1>HELLO ! THIS IS THE HOME PAGE<h1>"

# when running this application, app.run() is being executed and the 0.0.0.0 implies which addresses can access this webserver
if __name__ == "__main__":
    app.run(host="0.0.0.0")

