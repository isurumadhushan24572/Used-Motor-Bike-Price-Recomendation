from flask import Flask, request, render_template
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the trained model
with open('predictor.pickle', 'rb') as f:
    best_model = pickle.load(f)

# Prepare the label encoder for the Province column
# provinces = ['Western', 'Southern', 'North Central', 'Central', 'North Western', 'Sabaragamuwa', 'Northern', 'Uva', 'Eastern']
le = LabelEncoder()
# le.fit(provinces)

@app.route('/', methods=['GET', 'POST'])
def home():
    pred_value = 0
    if request.method == 'POST':
        mileage = int(request.form['Mileage'])
        published_year = int(request.form['published_year'])
        manufactured_year = int(request.form['manufactured_year'])
        province = request.form['province']

        new_data = {
            'Mileage': [mileage],
            'Published_Year': [published_year],
            'Manufactured_Year': [manufactured_year],
            'Province': [province]
        }

        new_df = pd.DataFrame(new_data)
        new_df['Province_Encoded'] = le.transform(new_df['Province'])
        feature_cols = ['Mileage', 'Published_Year', 'Manufactured_Year', 'Province_Encoded'] 
        X_new = new_df[feature_cols]

        y_pred_new1 = best_model.predict(X_new)
        pred_value = y_pred_new1[0]

    return render_template('index.html', pred_value=pred_value)

if __name__ == '__main__':
    app.run(debug=True)
