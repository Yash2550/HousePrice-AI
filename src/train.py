import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
DATA_PATH = BASE_DIR / "data" / "house_data.csv"
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

def main():
    if not DATA_PATH.exists():
        print(f"Error: Data file not found at {DATA_PATH}")
        return
    print(f"Loading data from:{DATA_PATH}")
    df = pd.read_csv(DATA_PATH)
    
    X = df.drop("Price", axis=1)
    y = df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print("R2 Score:", r2_score(y_test, preds))

    MODEL_PATH.parent.mkdir(exist_ok=True, parents=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()