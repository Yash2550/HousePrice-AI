from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import pandas as pd
from pathlib import Path
import os

# Define base directory paths
BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

# Initialize Flask app
# Fixed the typo from 'FRONTwEND_DIR' to 'FRONTEND_DIR'
app = Flask(__name__, static_folder=str(FRONTEND_DIR))
CORS(app)

# Load the trained machine learning model
if MODEL_PATH.exists():
    model = joblib.load(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
else:
    model = None
    print("Warning: Model file not found. Please run src/train.py first.")

@app.route('/')
def home():
    """Serve the main index.html file"""
    return send_from_directory(FRONTEND_DIR, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve CSS, JS, and other static assets"""
    return send_from_directory(FRONTEND_DIR, path)

@app.route("/predict", methods=["POST"])
def predict():
    """Handle the prediction request from the frontend"""
    if not model:
        return jsonify({"error": "Model is not trained. Run train.py first."}), 500

    try:
        data = request.json
        # Create DataFrame matching the features used during training
        df = pd.DataFrame([{
            "Area": float(data.get("Area")),
            "Bedrooms": int(data.get("Bedrooms")),
            "Bathrooms": int(data.get("Bathrooms")),
            "Stories": int(data.get("Stories")),
            "Parking": int(data.get("Parking"))
        }])
        
        # Perform prediction
        prediction = model.predict(df)[0]
        return jsonify({
            "predicted_price": round(float(prediction), 2)
        })
    except Exception as e:
        print(f"Prediction Error: {e}")
        return jsonify({"error": str(e)}), 400
    
if __name__ == "__main__":
    # Use environment variable for PORT to support Render deployment
    port = int(os.environ.get("PORT", 5000))
    print(f"Serving frontend from: {FRONTEND_DIR}")
    # Setting host to 0.0.0.0 is required for cloud hosting
    app.run(host='0.0.0.0', port=port, debug=False)