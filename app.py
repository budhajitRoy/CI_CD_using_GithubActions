# import libraries
from flask import Flask, request
import joblib


# Create app
app = Flask(__name__)

@app.route("/test", methods = ['GET'])
def ping():
    return "Hello Loan app!!"

# set up the model
loan_approval = joblib.load("loan_approval.pkl")

# set up data
# test_data = [0.0, 1.0, 3708.0, 173.0, 1.0]

test = {'Gender': 0.0,
 'Married': 1.0,
 'ApplicantIncome': 3708.0,
 'LoanAmount': 173.0,
 'Credit_History': 1.0}


@app.route("/predict", methods = ['GET'])
def predict():
    
    # result = loan_approval.predict([test_data])
    
    # get inputs from the request
    test_data = request.get_json()

    # encoding
    if test_data['Gender'] == 'Male':
        test_data['Gender'] = 0 
    else:
        test_data['Gender'] = 1 

    if test_data['Married'] == 'No':
        test_data['Married'] = 0 
    else:
        test_data['Married'] = 1

    input_data = list(test_data.values())
    result = loan_approval.predict([input_data])

    if result[0] == 1:
        return "Loan Approved"
    else:
        return "Loan Not Approved"

## command to run : flask --app app run
