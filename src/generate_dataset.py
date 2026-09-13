"""Generate a reproducible house-price dataset for Student ID 23L-8058."""

from pathlib import Path
import random

import pandas as pd


STUDENT_ID = "23L-8058"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "dataset.csv"
NUMBER_OF_HOUSES = 120
RANDOM_SEED = 8058


def generate_dataset() -> pd.DataFrame:
    """Create synthetic house information and corresponding prices."""
    random_generator = random.Random(RANDOM_SEED)
    records = []

    for _ in range(NUMBER_OF_HOUSES):
        area_sqft = random_generator.randint(600, 3500)
        bedrooms = random_generator.randint(1, 5)
        bathrooms = random_generator.randint(1, 4)
        age_years = random_generator.randint(0, 40)
        distance_city_km = round(random_generator.uniform(1, 30), 2)
        random_noise = random_generator.gauss(0, 20_000)

        price = (
            50_000
            + area_sqft * 160
            + bedrooms * 12_000
            + bathrooms * 20_000
            - age_years * 1_500
            - distance_city_km * 2_000
            + random_noise
        )

        records.append(
            {
                "area_sqft": area_sqft,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
                "age_years": age_years,
                "distance_city_km": distance_city_km,
                "price": round(price, 2),
            }
        )

    return pd.DataFrame(records)


def main() -> None:
    """Generate and save the dataset in the local data directory."""
    dataset = generate_dataset()
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    dataset.to_csv(DATA_PATH, index=False)

    print(f"Student ID: {STUDENT_ID}")
    print(f"Generated rows: {len(dataset)}")
    print(f"Dataset saved to: {DATA_PATH}")


if __name__ == "__main__":
    main()