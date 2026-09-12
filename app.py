from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

pipeline = joblib.load('dt_pipeline.joblib')
data = pd.read_csv('test_data_set.csv', index_col= 0)

app = Flask(__name__)

@app.route('/predict', methods= ['POST'])
def default_predict():

    customer_id = int(request.form['customer_id'])
    customer = data.iloc[customer_id, :].to_dict()
    customer_df = pd.DataFrame([customer])
    predict_proba = (pipeline.predict_proba(customer_df)[0, 1])
    if predict_proba >= 0.3:
        decision = f'Customer credit request is REJECTED as default probability is:{(100 * predict_proba):.2f}% >= 30%'
    else:
        decision = f'Customer credit request is ACCEPTED as default probability is:{(100 * predict_proba):.2f}% < 30%'

    return render_template("new_predict.html", decision= decision)

@app.route('/', methods= ['GET'])
def welcome_to():

    return render_template("pana_bank.html")

if __name__ == '__main__':
    app.run(debug= True, host= 'localhost', port= 5000)
