from flask import Flask, request, render_template
import joblib
import pandas as pd

# Create Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML page

# Define the predict route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data
    hour = int(request.form['hour'])
    month = int(request.form['month'])
    day_of_week = int(request.form['day_of_week'])

    # Prepare the input features
    features = [[hour, month, day_of_week]]

    # Make a prediction using the model
    prediction = model.predict(features)[0]

    # Output the prediction (1 = Arrest, 0 = No Arrest)
    result = "Arrest was made" if prediction == 1 else "No arrest made"
    return render_template('index.html', result=result)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
