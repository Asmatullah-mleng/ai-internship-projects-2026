from pathlib import Path
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


# --------------------------------------------------
# Project paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

MODEL_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# 1. Load Iris dataset
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target

print("Iris dataset loaded successfully.")
print(f"Number of samples: {X.shape[0]}")
print(f"Number of features: {X.shape[1]}")


# --------------------------------------------------
# 2. Split dataset
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nDataset split:")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# --------------------------------------------------
# 3. Feature scaling
# --------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)


print("\nFeature scaling completed.")


# --------------------------------------------------
# 4. Create KNN model
# --------------------------------------------------

knn = KNeighborsClassifier(
    n_neighbors=5
)


# --------------------------------------------------
# 5. Train model
# --------------------------------------------------

print("\nTraining KNN model...")

knn.fit(X_train_scaled, y_train)

print("Model training completed.")


# --------------------------------------------------
# 6. Save trained model
# --------------------------------------------------

model_path = MODEL_DIR / "knn_iris_model.pkl"
scaler_path = MODEL_DIR / "scaler.pkl"

joblib.dump(knn, model_path)
joblib.dump(scaler, scaler_path)


print("\nModels saved successfully:")
print(f"Model:  {model_path}")
print(f"Scaler: {scaler_path}")

print("\nTraining pipeline completed successfully.")