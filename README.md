# MLOps House Price Prediction Project — 23L-8058

This repository contains the MLOps Assignment 1 project for Student ID **23L-8058**.

The project demonstrates a reproducible machine-learning workflow using Python, Visual Studio Code, Git, and GitHub. It generates a synthetic house-price dataset, trains a regression model, evaluates it, and saves the trained model as a serialized artifact.

## Project Structure

```text
mlops-project-23L-8058/
├── data/
│   ├── README.md
│   └── dataset.csv                 # Generated locally and ignored by Git
├── model/
│   ├── README.md
│   └── house_price_model_23L-8058.joblib
│                                     # Generated locally and ignored by Git
├── src/
│   ├── generate_dataset.py
│   ├── train.py
│   └── train_23L-8058.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Why Data and Models Are Excluded

Raw datasets and trained model artifacts can be large and may contain private or sensitive information. They are excluded from Git to keep the repository lightweight and safe.

The project tracks the code and dependency versions required to reproduce these artifacts.

## Requirements

- Python 3.14 or a compatible Python 3 version
- Git
- Visual Studio Code
- PowerShell on Windows

## Setup Instructions

Run all commands from the repository root.

### 1. Create a virtual environment

```powershell
python -m venv venv
```

### 2. Activate the environment

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks the activation script, temporarily allow it for the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### 3. Install exact dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Generate the local dataset

```powershell
python src/generate_dataset.py
```

This creates:

```text
data/dataset.csv
```

The dataset uses a fixed random seed based on Student ID 23L-8058, making its generation reproducible.

### 5. Train and evaluate the model

```powershell
python src/train.py
```

The training workflow:

1. Loads `data/dataset.csv`.
2. Separates the features and target.
3. Creates an 80/20 training and testing split.
4. Trains a Random Forest regression model.
5. Reports Mean Absolute Error and R-squared.
6. Saves the trained pipeline.

The generated model is stored at:

```text
model/house_price_model_23L-8058.joblib
```

## Standard Entry Point

The standard training command is:

```powershell
python src/train.py
```

This entry point runs the student-specific script:

```text
src/train_23L-8058.py
```

## Git Ignore Policy

The `.gitignore` file excludes:

- Raw datasets under `data/`
- Generated models under `model/`
- Python virtual environments
- Python cache files
- `.pkl`, `.joblib`, and `.h5` model artifacts
- Jupyter temporary files
- Operating-system temporary files

Only source code, dependency configuration, and documentation are committed.

## Student Information

- Student ID: 23L-8058
- Project: MLOps Assignment 1