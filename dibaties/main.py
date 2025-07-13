from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load('diabetes_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[field]) for field in [
            'Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
            'BMI', 'DiabetesPedigreeFunction', 'Age'
        ]]
        input_data = np.array(features).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        result = "⚠️ High risk of diabetes" if prediction == 1 else "✅ Low risk of diabetes"
        return render_template('index.html', prediction_text=result)
    except:
        return render_template('index.html', prediction_text="❌ Please enter valid numeric inputs.")

if __name__ == '__main__':
    app.run(debug=True)
