from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)


data = pd.read_pickle('student_data.pkl')


def predict_marks(hours):

    coef = 3.93571802 
    intercept = 50.44735504  
    return hours * coef + intercept

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        study_hours = float(request.json['hours'])
        predicted_marks = predict_marks(study_hours)
        return jsonify({'marks': predicted_marks})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
