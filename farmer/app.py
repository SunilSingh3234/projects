from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form input
        features = [float(request.form[f]) for f in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
        prediction = model.predict([features])[0]
        return render_template('result.html', prediction=prediction)
    except Exception as e:
        return render_template('result.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
