# 🏡 House Price Prediction Web Application

A modern, full-stack web application that uses machine learning to predict house prices based on various property features. Built with Flask, scikit-learn, and a beautiful responsive frontend.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [API Endpoints](#api-endpoints)
- [Features Explanation](#features-explanation)
- [Screenshots](#screenshots)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **🤖 Machine Learning Powered**: Uses trained scikit-learn model for accurate predictions
- **🎨 Modern UI/UX**: Beautiful, responsive design with gradient backgrounds and smooth animations
- **📱 Mobile Responsive**: Works seamlessly on desktop, tablet, and mobile devices
- **🔍 Input Validation**: Comprehensive form validation with helpful hints
- **⚡ Fast Performance**: Optimized backend with efficient model loading
- **📊 Organized Input**: 22 features grouped into logical sections for easy data entry
- **💡 User Guidance**: Tooltips and examples for each input field
- **🛡️ Error Handling**: Robust error handling with user-friendly messages
- **🏥 Health Check**: API endpoint for monitoring application status

## 🎥 Demo

The application provides an intuitive interface to input property features and receive instant price predictions.

### Key Sections:
1. **Basic Information**: Bedrooms, bathrooms, floors
2. **Property Size**: Living area, lot size, basement
3. **Property Features**: Waterfront, view quality, condition, grade
4. **Property History**: Year built, renovation details
5. **Location**: Zipcode, latitude, longitude
6. **Neighborhood**: Average nearby property sizes
7. **Sale Information**: Sale date details

## 🛠️ Technology Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask 2.0+**: Web framework
- **scikit-learn**: Machine learning library
- **NumPy**: Numerical computations
- **joblib**: Model serialization

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with custom properties and gradients
- **Google Fonts (Inter)**: Clean, modern typography
- **Responsive Design**: Mobile-first approach

## 📁 Project Structure

```
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
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure model file exists**
   - Make sure `house_price_model_lzma.pkl` is in the root directory
   - If you need to train the model, see [Model Training](#model-training)

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`

## 💻 Usage

### Making a Prediction

1. **Navigate to the home page** (`http://localhost:5000`)

2. **Fill in the property details**:
   - Enter basic information (property ID, bedrooms, bathrooms, floors)
   - Specify property size (living area, lot size, basement)
   - Select property features (waterfront, view, condition, grade)
   - Provide property history (year built, year renovated)
   - Enter location details (zipcode, latitude, longitude)
   - Add neighborhood averages
   - Input sale information (year, month, day)

3. **Click "Predict House Price"**

4. **View the prediction**:
   - See the estimated house price
   - Read helpful notes about the prediction
   - Make another prediction if needed

### Example Input Values

```
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
```

## 🧠 Model Training

The machine learning model was trained using historical house price data. You can access the training notebook here:

**Colab Notebook**: [https://colab.research.google.com/drive/1jnPaWXmZJ0Z_brUS6-mnc3a8CaOztiHb](https://colab.research.google.com/drive/1jnPaWXmZJ0Z_brUS6-mnc3a8CaOztiHb)

### Training Process Overview

1. **Data Collection**: Historical house sales data with 22 features
2. **Data Preprocessing**: Cleaning, handling missing values, feature engineering
3. **Model Selection**: Testing various regression algorithms
4. **Training**: Fitting the best performing model
5. **Evaluation**: Assessing model performance with metrics (R², RMSE, MAE)
6. **Model Export**: Saving the trained model using joblib with LZMA compression

### Retraining the Model

If you want to retrain the model with new data:

```python
import joblib
from sklearn.ensemble import RandomForestRegressor
# Or your chosen model

# Train your model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save with LZMA compression
joblib.dump(model, 'house_price_model_lzma.pkl', compress=('lzma', 3))
```

## 🔌 API Endpoints

### 1. Home Page
- **URL**: `/`
- **Method**: `GET`
- **Description**: Renders the main prediction form
- **Response**: HTML page with input form

### 2. Predict Price
- **URL**: `/predict`
- **Method**: `POST`
- **Description**: Processes form data and returns price prediction
- **Parameters**: All 22 features as form data
- **Response**: HTML page with prediction result or error message

### 3. Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Description**: Check application and model status
- **Response**: 
  ```json
  {
    "status": "healthy",
    "model_loaded": true
  }
  ```

## 📊 Features Explanation

### Input Features (22 total)

| Feature | Description | Example | Range/Type |
|---------|-------------|---------|------------|
| `id` | Unique property identifier | 123456 | Integer |
| `bedrooms` | Number of bedrooms | 3 | Integer ≥ 0 |
| `bathrooms` | Number of bathrooms | 2.5 | Float ≥ 0 |
| `sqft_living` | Interior living space (sqft) | 2000 | Integer ≥ 0 |
| `sqft_lot` | Total lot size (sqft) | 5000 | Integer ≥ 0 |
| `floors` | Number of floors | 2 | Float ≥ 1 |
| `waterfront` | Waterfront property | 0 or 1 | Binary |
| `view` | Quality of view | 2 | 0-4 |
| `condition` | Overall condition | 3 | 1-5 |
| `grade` | Construction quality | 7 | 1-13 |
| `sqft_above` | Above ground living space | 1500 | Integer ≥ 0 |
| `sqft_basement` | Basement size | 500 | Integer ≥ 0 |
| `yr_built` | Year property was built | 1990 | Year |
| `yr_renovated` | Year of last renovation | 0 | Year or 0 |
| `zipcode` | Property zipcode | 98001 | 5 digits |
| `lat` | Latitude coordinate | 47.5112 | Float |
| `long` | Longitude coordinate | -122.257 | Float |
| `sqft_living15` | Avg living space of 15 nearest | 1800 | Integer ≥ 0 |
| `sqft_lot15` | Avg lot size of 15 nearest | 4500 | Integer ≥ 0 |
| `year` | Sale year | 2024 | Year |
| `month` | Sale month | 6 | 1-12 |
| `day` | Sale day | 15 | 1-31 |

### Feature Categories

**🏠 Property Characteristics**
- Size metrics (living area, lot size, basement)
- Structure (bedrooms, bathrooms, floors)
- Quality ratings (condition, grade, view)

**📍 Location Data**
- Geographic coordinates (latitude, longitude)
- Administrative (zipcode)
- Neighborhood context (sqft_living15, sqft_lot15)

**⏰ Temporal Data**
- Property age (yr_built, yr_renovated)
- Sale timing (year, month, day)

## 📸 Screenshots

### Home Page - Prediction Form
- Clean, organized input sections
- Helpful placeholders and tooltips
- Modern gradient design

### Results Page
- Large, easy-to-read price display
- Success/error indicators
- Helpful additional information

## 🌐 Deployment

### Local Deployment (Development)

Already covered in [Installation](#installation) section.

### Production Deployment

#### Option 1: Heroku

1. **Create `Procfile`**
   ```
   web: gunicorn app:app
   ```

2. **Update `requirements.txt`**
   ```bash
   pip install gunicorn
   pip freeze > requirements.txt
   ```

3. **Deploy to Heroku**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

#### Option 2: Railway

1. **Create account** at [Railway.app](https://railway.app)
2. **Connect GitHub repository**
3. **Deploy automatically** from main branch

#### Option 3: PythonAnywhere

1. **Upload files** to PythonAnywhere
2. **Configure web app** in dashboard
3. **Set WSGI configuration**

#### Option 4: Docker

1. **Create `Dockerfile`**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   EXPOSE 5000
   CMD ["python", "app.py"]
   ```

2. **Build and run**
   ```bash
   docker build -t house-price-predictor .
   docker run -p 5000:5000 house-price-predictor
   ```

### Environment Variables

For production, consider setting:
```bash
FLASK_ENV=production
SECRET_KEY=your-secret-key
MODEL_PATH=house_price_model_lzma.pkl
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write descriptive commit messages
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed

## 🐛 Troubleshooting

### Model Not Loading
**Problem**: Model file not found or corrupt
**Solution**: 
- Ensure `house_price_model_lzma.pkl` exists in root directory
- Retrain and export the model
- Check file permissions

### Import Errors
**Problem**: Missing dependencies
**Solution**:
```bash
pip install -r requirements.txt
```

### Port Already in Use
**Problem**: Port 5000 is occupied
**Solution**:
```python
# Change port in app.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

### CSS Not Loading
**Problem**: Styles not applying
**Solution**:
- Create `static/` folder if missing
- Move `styles.css` to `static/styles.css`
- Update HTML template links

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Your Name - Initial work - [AAs6395](https://github.com/AAs6395)

## 🙏 Acknowledgments

- Dataset source: [King County House Sales](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)
- Flask documentation
- scikit-learn documentation
- Design inspiration from modern web applications

## 📧 Contact

For questions or support, please open an issue or contact:
- Email: jaashish109@gmail.com
- GitHub: [@AAs6395](https://github.com/AAs6395)

## 🔮 Future Enhancements

- [ ] Add data visualization for predictions
- [ ] Implement user authentication
- [ ] Save prediction history
- [ ] Add comparison with similar properties
- [ ] Integrate with real estate APIs
- [ ] Add map visualization for property location
- [ ] Export predictions as PDF reports
- [ ] Multi-language support
- [ ] Dark mode toggle

---


**⭐ If you found this project helpful, please consider giving it a star!**
