from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# Label encoding dictionaries (must match training encoding!)
label_maps = {
    'brand': {'ASUS': 0, 'Lenovo': 1, 'acer': 2, 'Avita': 3, 'HP': 4, 'DELL': 5, 'MSI': 6, 'APPLE': 7},
    'processor_brand': {'Intel': 0, 'AMD': 1, 'M1': 2},
    'processor_name': {
        'Core i3': 0, 'Core i5': 1, 'Celeron Dual': 2, 'Ryzen 5': 3, 'Core i7': 4,
        'Core i9': 5, 'M1': 6, 'Pentium Quad': 7, 'Ryzen 3': 8, 'Ryzen 7': 9, 'Ryzen 9': 10
    },
    'processor_gnrtn': {'10th': 0, 'Not Available': 1, '11th': 2, '7th': 3, '8th': 4, '9th': 5, '4th': 6, '12th': 7},
    'ram_gb': {'4 GB': 0, '8 GB': 1, '16 GB': 2, '32 GB': 3},
    'ssd': {'0 GB': 0, '512 GB': 1, '256 GB': 2, '128 GB': 3, '1024 GB': 4, '2048 GB': 5, '3072 GB': 6},
    'hdd': {'1024 GB': 0, '0 GB': 1, '512 GB': 2, '2048 GB': 3},
    'graphic_card_gb': {'0 GB': 0, '2 GB': 1, '4 GB': 2, '6 GB': 3, '8 GB': 4},
    'warranty': {'No warranty': 0, '1 year': 1, '2 years': 2, '3 years': 3},
    'Touchscreen': {'No': 0, 'Yes': 1},
}

@app.route('/')
def home():
    return render_template('index.html', options=label_maps)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = []
        for key in label_maps:
            value = request.form[key]
            mapped_value = label_maps[key][value]
            input_data.append(mapped_value)

        features = np.array([input_data])
        prediction = model.predict(features)[0]
        return render_template('result.html', prediction=round(prediction, 2))
    except Exception as e:
        return render_template('result.html', prediction=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
