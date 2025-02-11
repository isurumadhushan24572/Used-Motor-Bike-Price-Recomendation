from flask import Flask, request, render_template
import pickle


app = Flask(__name__)

# Load the trained model
with open('predictor.pickle', 'rb') as f:
    best_model = pickle.load(f)

province_list = ['Central','Eastern','North Central','North Western','Northern','Sabaragamuwa','Southern','Uva','Western']
def province_encoding(provinces):
            list_provice = []
            for province in province_list:
                if provinces == province:
                    list_provice.append(1)
                else:
                    list_provice.append(0)

            return list_provice

@app.route('/', methods=['GET', 'POST'])
def home():
    pred_value = 0
    if request.method == 'POST':
        mileage = int(request.form['Mileage'])
        published_year = int(request.form['published_year'])
        manufactured_year = int(request.form['manufactured_year'])
        province = request.form['province']

        p_list = province_encoding(province)
        new_data = [mileage, published_year, manufactured_year]
        new_data.extend(p_list)

        y_pred_new1 = best_model.predict([new_data])
        pred_value = y_pred_new1[0]

    return render_template('index.html', pred_value = pred_value)

if __name__ == '__main__':
    app.run(debug=True)
