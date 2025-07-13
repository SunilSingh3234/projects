from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)


model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    age = int(request.form['age'])
    sex = int(request.form['sex'])  
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = int(request.form['smoker']) 
    region = int(request.form['region'])  

    features = np.array([[age, sex, bmi, children, smoker, region]])
    prediction = model.predict(features)[0]

    return render_template('result.html', prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
