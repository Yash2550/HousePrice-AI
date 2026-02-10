import joblib
import pandas as pd
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

def predict_price(area, bedrooms, bathrooms, stories, parking):
    if not MODEL_PATH.exists():
        return "Error: Model file not found. Run train.py first."

    model = joblib.load(MODEL_PATH)

    data = pd.DataFrame([{
        "Area": area,
        "Bedrooms": bedrooms,
        "Bathrooms": bathrooms,
        "Stories": stories,
        "Parking": parking
    }])

    price = model.predict(data)[0]
    return round(price, 2)

if __name__ == "__main__":
    print(predict_price(1800, 3, 3, 2, 2))