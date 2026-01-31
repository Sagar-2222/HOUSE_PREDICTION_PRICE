from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# ✅ Load trained model using joblib
MODEL_PATH = "house_price_model_lzma.pkl"
model = None

try:
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print("✅ Model Loaded Successfully!")
    else:
        print(f"⚠️ Model file '{MODEL_PATH}' not found.")
except Exception as e:
    print(f"❌ Model could not be loaded: {e}")

# ✅ Define the exact feature order with descriptions
FEATURE_INFO = {
    'id': {'label': 'Property ID', 'type': 'number', 'placeholder': 'e.g., 123456'},
    'bedrooms': {'label': 'Bedrooms', 'type': 'number', 'placeholder': 'e.g., 3'},
    'bathrooms': {'label': 'Bathrooms', 'type': 'number', 'placeholder': 'e.g., 2.5'},
    'sqft_living': {'label': 'Living Area (sqft)', 'type': 'number', 'placeholder': 'e.g., 2000'},
    'sqft_lot': {'label': 'Lot Area (sqft)', 'type': 'number', 'placeholder': 'e.g., 5000'},
    'floors': {'label': 'Number of Floors', 'type': 'number', 'placeholder': 'e.g., 2'},
    'waterfront': {'label': 'Waterfront', 'type': 'select', 'options': ['0 (No)', '1 (Yes)']},
    'view': {'label': 'View Quality (0-4)', 'type': 'number', 'placeholder': '0-4'},
    'condition': {'label': 'Condition (1-5)', 'type': 'number', 'placeholder': '1-5'},
    'grade': {'label': 'Grade (1-13)', 'type': 'number', 'placeholder': '1-13'},
    'sqft_above': {'label': 'Above Ground (sqft)', 'type': 'number', 'placeholder': 'e.g., 1500'},
    'sqft_basement': {'label': 'Basement (sqft)', 'type': 'number', 'placeholder': 'e.g., 500'},
    'yr_built': {'label': 'Year Built', 'type': 'number', 'placeholder': 'e.g., 1990'},
    'yr_renovated': {'label': 'Year Renovated', 'type': 'number', 'placeholder': '0 if never'},
    'zipcode': {'label': 'Zipcode', 'type': 'number', 'placeholder': 'e.g., 98001'},
    'lat': {'label': 'Latitude', 'type': 'number', 'placeholder': 'e.g., 47.5112'},
    'long': {'label': 'Longitude', 'type': 'number', 'placeholder': 'e.g., -122.257'},
    'sqft_living15': {'label': 'Avg Living Area (sqft)', 'type': 'number', 'placeholder': 'e.g., 1800'},
    'sqft_lot15': {'label': 'Avg Lot Area (sqft)', 'type': 'number', 'placeholder': 'e.g., 4500'},
    'year': {'label': 'Sale Year', 'type': 'number', 'placeholder': 'e.g., 2024'},
    'month': {'label': 'Sale Month', 'type': 'number', 'placeholder': '1-12'},
    'day': {'label': 'Sale Day', 'type': 'number', 'placeholder': '1-31'}
}

FEATURES = list(FEATURE_INFO.keys())

@app.route('/')
def home():
    return render_template("index.html", feature_info=FEATURE_INFO)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template("result.html", 
                             error="Model is not loaded. Please ensure the model file exists.",
                             price=None)

    try:
        # ✅ Extract input data
        input_data = []
        for feature in FEATURES:
            value = request.form.get(feature)
            if value is None or value == "":
                return render_template("result.html", 
                                     error=f"Missing input for {feature}",
                                     price=None)
            input_data.append(float(value))

        # ✅ Convert to NumPy array
        input_array = np.array(input_data).reshape(1, -1)

        # ✅ Validate feature count
        if input_array.shape[1] != len(FEATURES):
            return render_template("result.html",
                                 error=f"Expected {len(FEATURES)} features, got {input_array.shape[1]}",
                                 price=None)

        # ✅ Make prediction
        predicted_price = model.predict(input_array)[0]

        return render_template("result.html", 
                             price=round(predicted_price, 2),
                             error=None)

    except ValueError as ve:
        return render_template("result.html",
                             error=f"Invalid input value: {str(ve)}",
                             price=None)
    except Exception as e:
        return render_template("result.html",
                             error=f"Prediction error: {str(e)}",
                             price=None)

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)