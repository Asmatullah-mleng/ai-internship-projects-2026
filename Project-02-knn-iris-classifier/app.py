from pathlib import Path

import joblib
import numpy as np
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent
MODEL_PATH = PROJECT_ROOT / "models" / "knn_iris_model.pkl"
SCALER_PATH = PROJECT_ROOT / "models" / "scaler.pkl"

CLASS_NAMES = ["setosa", "versicolor", "virginica"]


@st.cache_resource
def load_artifacts():
	return joblib.load(MODEL_PATH), joblib.load(SCALER_PATH)


def measurement_options(start, stop, step=0.1):
	return [round(value, 1) for value in np.arange(start, stop + step / 2, step)]


st.set_page_config(page_title="Iris Classifier")

st.title("Iris Flower Classifier")
st.write("Choose the four flower measurements to predict the Iris species.")

sepal_length = st.selectbox(
	"Sepal length (cm)", measurement_options(4.0, 8.0), index=11
)
sepal_width = st.selectbox(
	"Sepal width (cm)", measurement_options(2.0, 4.5), index=15
)
petal_length = st.selectbox(
	"Petal length (cm)", measurement_options(1.0, 7.0), index=4
)
petal_width = st.selectbox(
	"Petal width (cm)", measurement_options(0.1, 2.5), index=1
)

if st.button("Predict species", type="primary", use_container_width=True):
	model, scaler = load_artifacts()
	flower = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
	flower_scaled = scaler.transform(flower)

	prediction = model.predict(flower_scaled)[0]
	probabilities = model.predict_proba(flower_scaled)[0]
	predicted_class = CLASS_NAMES[prediction]
	confidence = probabilities[prediction]

	st.success(f"Predicted species: {predicted_class.title()}")
	st.metric("Confidence", f"{confidence:.1%}")
