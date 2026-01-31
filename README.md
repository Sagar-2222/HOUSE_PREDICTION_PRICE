🏡 House Price Prediction Web Application
A modern, full-stack web application that uses machine learning to predict house prices based on various property features. Built with Flask, scikit-learn, and a beautiful responsive frontend.

Python Flask scikit-learn License

📋 Table of Contents
Features
Demo
Technology Stack
Project Structure
Installation
Usage
Model Training
API Endpoints
Features Explanation
Screenshots
Deployment
Contributing
License
✨ Features
🤖 Machine Learning Powered: Uses trained scikit-learn model for accurate predictions
🎨 Modern UI/UX: Beautiful, responsive design with gradient backgrounds and smooth animations
📱 Mobile Responsive: Works seamlessly on desktop, tablet, and mobile devices
🔍 Input Validation: Comprehensive form validation with helpful hints
⚡ Fast Performance: Optimized backend with efficient model loading
📊 Organized Input: 22 features grouped into logical sections for easy data entry
💡 User Guidance: Tooltips and examples for each input field
🛡️ Error Handling: Robust error handling with user-friendly messages
🏥 Health Check: API endpoint for monitoring application status
🎥 Demo
The application provides an intuitive interface to input property features and receive instant price predictions.

Key Sections:
Basic Information: Bedrooms, bathrooms, floors
Property Size: Living area, lot size, basement
Property Features: Waterfront, view quality, condition, grade
Property History: Year built, renovation details
Location: Zipcode, latitude, longitude
Neighborhood: Average nearby property sizes
Sale Information: Sale date details
🛠️ Technology Stack
Backend
Python 3.8+: Core programming language
Flask 2.0+: Web framework
scikit-learn: Machine learning library
NumPy: Numerical computations
joblib: Model serialization
Frontend
HTML5: Semantic markup
CSS3: Modern styling with custom properties and gradients
Google Fonts (Inter): Clean, modern typography
Responsive Design: Mobile-first approach
📁 Project Structure
house-price-prediction/
│
├── app.py                          # Main Flask application
├── house_price_model_lzma.pkl     # Trained ML model (LZMA compressed)
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
│
├── templates/
│   ├── index.html                 # Main prediction form
│   └── result.html                # Results display page
│
└── static/
    └── styles.css                 # Stylesheet
🚀 Installation
Prerequisites
Python 3.8 or higher
pip (Python package manager)
Virtual environment (recommended)
Step-by-Step Setup
Clone the repository

git clone https://github.com/yourusername/house-price-prediction.git
cd house-price-prediction
Create a virtual environment

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies

pip install -r requirements.txt
Ensure model file exists

Make sure house_price_model_lzma.pkl is in the root directory
If you need to train the model, see Model Training
Run the application

python app.py
Access the application

Open your browser and navigate to: http://localhost:5000
💻 Usage
Making a Prediction
Navigate to the home page (http://localhost:5000)

Fill in the property details:

Enter basic information (property ID, bedrooms, bathrooms, floors)
Specify property size (living area, lot size, basement)
Select property features (waterfront, view, condition, grade)
Provide property history (year built, year renovated)
Enter location details (zipcode, latitude, longitude)
Add neighborhood averages
Input sale information (year, month, day)
Click "Predict House Price"

View the prediction:

See the estimated house price
Read helpful notes about the prediction
Make another prediction if needed
Example Input Values
Property ID: 123456
Bedrooms: 3
Bathrooms: 2.5
Living Area: 2000 sqft
Lot Area: 5000 sqft
Floors: 2
Waterfront: No (0)
View: 2
Condition: 3
Grade: 7
Above Ground: 1500 sqft
Basement: 500 sqft
Year Built: 1990
Year Renovated: 0 (never)
Zipcode: 98001
Latitude: 47.5112
Longitude: -122.257
Avg Living Area: 1800 sqft
Avg Lot Area: 4500 sqft
Sale Year: 2024
Sale Month: 6
Sale Day: 15
🧠 Model Training
The machine learning model was trained using historical house price data. You can access the training notebook here:

Colab Notebook: https://colab.research.google.com/drive/1jnPaWXmZJ0Z_brUS6-mnc3a8CaOztiHb

Training Process Overview
Data Collection: Historical house sales data with 22 features
Data Preprocessing: Cleaning, handling missing values, feature engineering
Model Selection: Testing various regression algorithms
Training: Fitting the best performing model
Evaluation: Assessing model performance with metrics (R², RMSE, MAE)
Model Export: Saving the trained model using joblib with LZMA compression
Retraining the Model
If you want to retrain the model with new data:

import joblib
from sklearn.ensemble import RandomForestRegressor
# Or your chosen model

# Train your model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save with LZMA compression
joblib.dump(model, 'house_price_model_lzma.pkl', compress=('lzma', 3))
🔌 API Endpoints
1. Home Page
URL: /
Method: GET
Description: Renders the main prediction form
Response: HTML page with input form
2. Predict Price
URL: /predict
Method: POST
Description: Processes form data and returns price prediction
Parameters: All 22 features as form data
Response: HTML page with prediction result or error message
3. Health Check
URL: /health
Method: GET
Description: Check application and model status
Response:
{
  "status": "healthy",
  "model_loaded": true
}
📊 Features Explanation
Input Features (22 total)
Feature	Description	Example	Range/Type
id	Unique property identifier	123456	Integer
bedrooms	Number of bedrooms	3	Integer ≥ 0
bathrooms	Number of bathrooms	2.5	Float ≥ 0
sqft_living	Interior living space (sqft)	2000	Integer ≥ 0
sqft_lot	Total lot size (sqft)	5000	Integer ≥ 0
floors	Number of floors	2	Float ≥ 1
waterfront	Waterfront property	0 or 1	Binary
view	Quality of view	2	0-4
condition	Overall condition	3	1-5
grade	Construction quality	7	1-13
sqft_above	Above ground living space	1500	Integer ≥ 0
sqft_basement	Basement size	500	Integer ≥ 0
yr_built	Year property was built	1990	Year
yr_renovated	Year of last renovation	0	Year or 0
zipcode	Property zipcode	98001	5 digits
lat	Latitude coordinate	47.5112	Float
long	Longitude coordinate	-122.257	Float
sqft_living15	Avg living space of 15 nearest	1800	Integer ≥ 0
sqft_lot15	Avg lot size of 15 nearest	4500	Integer ≥ 0
year	Sale year	2024	Year
month	Sale month	6	1-12
day	Sale day	15	1-31
Feature Categories
🏠 Property Characteristics

Size metrics (living area, lot size, basement)
Structure (bedrooms, bathrooms, floors)
Quality ratings (condition, grade, view)
📍 Location Data

Geographic coordinates (latitude, longitude)
Administrative (zipcode)
Neighborhood context (sqft_living15, sqft_lot15)
⏰ Temporal Data

Property age (yr_built, yr_renovated)
Sale timing (year, month, day)
📸 Screenshots
Home Page - Prediction Form
Clean, organized input sections
Helpful placeholders and tooltips
Modern gradient design
Results Page
Large, easy-to-read price display
Success/error indicators
Helpful additional information
🌐 Deployment
Local Deployment (Development)
Already covered in Installation section.

Production Deployment
Option 1: Heroku
Create Procfile

web: gunicorn app:app
Update requirements.txt

pip install gunicorn
pip freeze > requirements.txt
Deploy to Heroku

heroku create your-app-name
git push heroku main
Option 2: Railway
Create account at Railway.app
Connect GitHub repository
Deploy automatically from main branch
Option 3: PythonAnywhere
Upload files to PythonAnywhere
Configure web app in dashboard
Set WSGI configuration
Option 4: Docker
Create Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
Build and run

docker build -t house-price-predictor .
docker run -p 5000:5000 house-price-predictor
Environment Variables
For production, consider setting:

FLASK_ENV=production
SECRET_KEY=your-secret-key
MODEL_PATH=house_price_model_lzma.pkl
🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a feature branch
git checkout -b feature/AmazingFeature
Commit your changes
git commit -m 'Add some AmazingFeature'
Push to the branch
git push origin feature/AmazingFeature
Open a Pull Request
Development Guidelines
Follow PEP 8 style guide for Python code
Write descriptive commit messages
Add comments for complex logic
Test your changes thoroughly
Update documentation as needed
🐛 Troubleshooting
Model Not Loading
Problem: Model file not found or corrupt Solution:

Ensure house_price_model_lzma.pkl exists in root directory
Retrain and export the model
Check file permissions
Import Errors
Problem: Missing dependencies Solution:

pip install -r requirements.txt
Port Already in Use
Problem: Port 5000 is occupied Solution:

# Change port in app.py
app.run(debug=True, host='0.0.0.0', port=5001)
CSS Not Loading
Problem: Styles not applying Solution:

Create static/ folder if missing
Move styles.css to static/styles.css
Update HTML template links
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👥 Authors
Your Name - Initial work - AAs6395
🙏 Acknowledgments
Dataset source: King County House Sales
Flask documentation
scikit-learn documentation
Design inspiration from modern web applications
📧 Contact
For questions or support, please open an issue or contact:

Email: sagarsarkar2424@gmail.com
🔮 Future Enhancements
 Add data visualization for predictions
 Implement user authentication
 Save prediction history
 Add comparison with similar properties
 Integrate with real estate APIs
 Add map visualization for property location
 Export predictions as PDF reports
 Multi-language support
 Dark mode toggle
⭐ If you found this project helpful, please consider giving it a star!
