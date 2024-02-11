from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__, template_folder='.')

model = pickle.load(open("model_final.pkl", "rb"))

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            # Collect user input from the form
            model_name = request.form['Model']
            brand = request.form['Brand']
            mileage = request.form['Mileage']
            year = request.form['Year']

            # Validate numeric inputs
            if not is_numeric(mileage) or not is_numeric(year):
                raise ValueError("Invalid input. Please enter numeric values for Mileage and Year.")

            # Create a DataFrame from the user input
            user_input = pd.DataFrame([[model_name, brand, float(mileage), int(year)]],
                                      columns=['Model', 'Brand', 'Mileage', 'Year'])

            # Perform one-hot encoding on the user input
            user_encoded = pd.get_dummies(user_input, columns=['Model', 'Brand'])

            # Use the trained model to make predictions on the encoded input
            prediction = model.predict(user_encoded)

            # Format the predicted price for better readability
            formatted_prediction = 'RS Lac :- {:.2f}'.format(prediction[0])

            return render_template('index.html', prediction_text=formatted_prediction)

    except Exception as e:
        # Handle errors gracefully and provide feedback to the user
        error_message = f"An error occurred: {str(e)}"
        return render_template('index.html', prediction_text=error_message)

if __name__ == '__main__':
    app.run(debug=True)
