# Iris Flower Classifier

A simple machine learning project that predicts the species of an Iris flower from four measurements. The project trains a K-Nearest Neighbors (KNN) classifier and provides an interactive Streamlit application for making predictions.

## Features

- KNN classification with `n_neighbors=5`
- Standardized input features using `StandardScaler`
- Three supported Iris species: setosa, versicolor, and virginica
- Interactive Streamlit form with dropdown inputs
- Prediction confidence displayed for each prediction
- Saved model and scaler artifacts for reuse

## Input Features

The application accepts these measurements in centimeters:

| Feature | Description |
| --- | --- |
| Sepal length | Length of the sepal |
| Sepal width | Width of the sepal |
| Petal length | Length of the petal |
| Petal width | Width of the petal |

## Project Structure

```text
Project-02-knn-iris-classifier/
|-- app.py                    # Streamlit prediction interface
|-- requirement.txt           # Python dependencies
|-- models/
|   |-- knn_iris_model.pkl    # Trained KNN model
|   |-- scaler.pkl            # Fitted feature scaler
|-- notebook/
|   |-- iris_eda.ipynb        # Exploratory data analysis
|-- src/
|   |-- train_model.py        # Training and artifact generation
|   |-- predict.py            # Command-line prediction example
|-- results/                  # Generated analysis output
``` 

## Getting Started

### 1. Clone or download the project

Open a terminal in the project directory:

```bash
cd Project-02-knn-iris-classifier
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirement.txt
```

## Run the Application

The repository includes trained model artifacts in `models/`. Start the Streamlit interface with:

```bash
streamlit run app.py
```

Then open the local URL displayed in the terminal, usually `http://localhost:8501`.

Select the four flower measurements and click **Predict species** to view the predicted class and confidence score.

## Retrain the Model

To regenerate the saved model and scaler:

```bash
python src/train_model.py
```

The training script uses the Iris dataset included with scikit-learn, performs an 80/20 stratified train-test split, scales the features, and saves these files:

- `models/knn_iris_model.pkl`
- `models/scaler.pkl`

## Run a Command-Line Prediction

```bash
python src/predict.py
```

The example predicts the species for a flower with measurements `[5.1, 3.5, 1.4, 0.2]`.

## Machine Learning Workflow

1. Load the built-in Iris dataset.
2. Split the data into training and testing sets using stratification.
3. Fit a `StandardScaler` on the training features.
4. Train a KNN classifier using the scaled features.
5. Save the trained model and scaler with `joblib`.
6. Scale user input with the saved scaler and generate a prediction in Streamlit.

## License

This project is intended for educational and internship practice purposes.
