from pathlib import Path


STUDENT_ID = "23L-8058"
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "dataset.csv"

print(f"Student ID: {STUDENT_ID}")
print(f"Loading dataset from: {DATA_PATH}")
