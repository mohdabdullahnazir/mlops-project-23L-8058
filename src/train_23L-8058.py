"""Train a house-price model for Student ID 23L-8058."""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler


STUDENT_ID = "23L-8058"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "dataset.csv"
MODEL_DIRECTORY = PROJECT_ROOT / "model"
MODEL_PATH = MODEL_DIRECTORY / f"house_price_model_{STUDENT_ID}.joblib"
TARGET_COLUMN = "price"
RANDOM_STATE = 42


def load_dataset() -> pd.DataFrame:
    """Load the local CSV dataset and verify the target column."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found at {DATA_PATH}. "
            "Run 'python src/generate_dataset.py' first."
        )

    dataset = pd.read_csv(DATA_PATH)

    if TARGET_COLUMN not in dataset.columns:
        raise ValueError(
            f"Required target column '{TARGET_COLUMN}' is missing."
        )

    return dataset


def train_model(dataset: pd.DataFrame) -> Pipeline:
    """Split the dataset, train a model, and display evaluation metrics."""
    features = dataset.drop(columns=[TARGET_COLUMN])
    target = dataset[TARGET_COLUMN]

    features_train, features_test, target_train, target_test = train_test_split(
        features,
        target,
        test_size=0.20,
        random_state=RANDOM_STATE,
    )

    scaler = "passthrough"  # Feature branches will modify this exact line.

    pipeline = Pipeline(
        steps=[
            ("scaler", scaler),
            (
                "model",
                RandomForestRegressor(
                    n_estimators=100,
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )

    pipeline.fit(features_train, target_train)
    predictions = pipeline.predict(features_test)

    mae = mean_absolute_error(target_test, predictions)
    r2 = r2_score(target_test, predictions)

    print(f"Training rows: {len(features_train)}")
    print(f"Testing rows: {len(features_test)}")
    print(f"Mean Absolute Error: {mae:,.2f}")
    print(f"R-squared score: {r2:.4f}")

    return pipeline


def save_model(model: Pipeline) -> None:
    """Serialize the trained pipeline into the model directory."""
    MODEL_DIRECTORY.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to: {MODEL_PATH}")


def main() -> None:
    """Run the complete data-loading, training, and saving workflow."""
    print(f"Student ID: {STUDENT_ID}")
    print(f"Loading dataset from: {DATA_PATH}")

    dataset = load_dataset()
    print(f"Dataset shape: {dataset.shape}")

    trained_model = train_model(dataset)
    save_model(trained_model)


if __name__ == "__main__":
    main()