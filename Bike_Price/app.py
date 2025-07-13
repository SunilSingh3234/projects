from flask import Flask, render_template, request, jsonify
import joblib


model = joblib.load('bike_price_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project', methods=["POST", "GET"])
def predict():
    prediction = None  

    if request.method == "POST":
        brand_name = request.form['brand_name']
        owner = request.form['owner']
        age = int(request.form['age'])
        power = float(request.form['power'])
        kms_driven = int(request.form['kms_driven'])

        brand_dict = {
            'TVS': 0, 'Royal Enfield': 1, 'Triumph': 2, 'Yamaha': 3, 'Honda': 4,
            'Hero': 5, 'Bajaj': 6, 'Suzuki': 7, 'Benelli': 8, 'KTM': 9,
            'Mahindra': 10, 'Kawasaki': 11, 'Ducati': 12, 'Hyosung': 13,
            'Harley-Davidson': 14, 'Jawa': 15, 'BMW': 16, 'Indian': 17,
            'Rajdoot': 18, 'LML': 19, 'Yezdi': 20, 'MV': 21, 'Ideal': 22
        }

        brand_code = brand_dict.get(brand_name, -1)

        
        owner_dict = {'First': 0, 'Second': 1, 'Third': 2, 'Fourth & Above': 3}
        owner_code = owner_dict.get(owner, 0)

        input_features = [[brand_code, owner_code, age, power, kms_driven]]
        prediction = model.predict(input_features)[0]  # get the scalar value

    return render_template('project.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
