import joblib
import numpy as np


# --------------------------------------------------
# 1. Load trained model
# --------------------------------------------------

model = joblib.load("models/knn_iris_model.pkl")

# Load scaler
scaler = joblib.load("models/scaler.pkl")


# --------------------------------------------------
# 2. Define a new flower
# --------------------------------------------------

# [sepal length, sepal width, petal length, petal width]

new_flower = np.array([
    [5.1, 3.5, 1.4, 0.2]
])


# --------------------------------------------------
# 3. Scale the new data
# --------------------------------------------------

new_flower_scaled = scaler.transform(new_flower)


# --------------------------------------------------
# 4. Make prediction
# --------------------------------------------------

prediction = model.predict(new_flower_scaled)

probability = model.predict_proba(new_flower_scaled)


# --------------------------------------------------
# 5. Iris class names
# --------------------------------------------------

class_names = [
    "setosa",
    "versicolor",
    "virginica"
]


predicted_class = class_names[prediction[0]]

confidence = probability[0][prediction[0]]


# --------------------------------------------------
# 6. Display result
# --------------------------------------------------

print("Flower Prediction")
print("-----------------")

print("Input features:")
print(new_flower[0])

print(f"\nPredicted species: {predicted_class}")
print(f"Confidence: {confidence:.2%}")