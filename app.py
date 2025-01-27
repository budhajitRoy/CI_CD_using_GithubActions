# import libraries
from flask import Flask
import joblib


# Create app
app = Flask(__name__)

@app.route("/test")
def app_test():
    return "Hello Laon app!!"

## command to run : flask --app app run
