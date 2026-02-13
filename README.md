# 🏠 HousePrice-AI

A machine learning-powered web application for predicting house prices using artificial intelligence.

## 📋 Features

- 🤖 **AI-Powered Predictions**: Uses trained ML model for accurate house price predictions
- 🌐 **Interactive Web Interface**: User-friendly frontend for easy interaction
- 📊 **Data-Driven**: Built on comprehensive house price dataset
- 🔐 **User Authentication**: Login, signup, and password recovery
- 📈 **Visualization**: Interactive notebooks for data analysis

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Yash2550/HousePrice-AI.git
cd HousePrice-AI
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open in browser**
Navigate to `http://localhost:5000` (or the port displayed in terminal)

## 📁 Project Structure

```
HousePrice-AI/
├── app.py                  # Main Flask application
├── requirements.txt        # Project dependencies
├── data/                   # Dataset files
│   └── house_data.csv
├── models/                 # Trained ML models
│   └── house_price_model.pkl
├── src/                    # Source code
│   ├── train.py           # Model training script
│   └── predict.py         # Prediction logic
├── frontend/              # Web interface
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── about.html
│   ├── contact.html
│   ├── feature.html
│   ├── css/
│   └── js/
└── notebooks/             # Jupyter notebooks
    └── prediction.ipynb
```

## 💻 Usage

1. **Train the Model** (Optional - model already included)
```bash
python src/train.py
```

2. **Make Predictions**
   - Open the web interface
   - Enter house features (size, location, bedrooms, etc.)
   - Get instant price predictions

3. **Explore Data Analysis**
```bash
jupyter notebook notebooks/prediction.ipynb
```

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn, pandas, numpy
- **Frontend**: HTML, CSS, JavaScript
- **Data Analysis**: Jupyter Notebook

## 📊 Model Information

The prediction model is trained on real house price data and considers multiple features including:
- House size (square footage)
- Number of bedrooms/bathrooms
- Location
- Age of property
- And more...

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Yash2550**
- GitHub: [@Yash2550](https://github.com/Yash2550)

## 📧 Contact

For questions or feedback, please visit the contact page in the web application.

---

⭐ If you found this project helpful, please give it a star!
