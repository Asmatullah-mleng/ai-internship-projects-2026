from pathlib import Path

import joblib
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)


# --------------------------------------------------
# Project paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"
RESULTS_DIR = BASE_DIR / "results"


# --------------------------------------------------
# Load Iris dataset
# --------------------------------------------------

iris = load_iris()

X = iris.data
y = iris.target


# --------------------------------------------------
# Create same train/test split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# --------------------------------------------------
# Load trained model and scaler
# --------------------------------------------------

model = joblib.load(
    MODEL_DIR / "knn_iris_model.pkl"
)

scaler = joblib.load(
    MODEL_DIR / "scaler.pkl"
)


# --------------------------------------------------
# Scale test data
# --------------------------------------------------

X_test_scaled = scaler.transform(X_test)


# --------------------------------------------------
# Make predictions
# --------------------------------------------------

y_pred = model.predict(X_test_scaled)


# --------------------------------------------------
# Calculate accuracy
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("=" * 50)
print("KNN MODEL EVALUATION")
print("=" * 50)

print(f"\nAccuracy: {accuracy:.4f}")
print(f"Accuracy: {accuracy * 100:.2f}%")


# --------------------------------------------------
# Classification report
# --------------------------------------------------

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)


# --------------------------------------------------
# Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)


# --------------------------------------------------
# Save results
# --------------------------------------------------

RESULTS_DIR.mkdir(exist_ok=True)

with open(
    RESULTS_DIR / "classification_report.txt",
    "w"
) as file:

    file.write("KNN Iris Classifier Evaluation\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Accuracy: {accuracy:.4f}\n\n")
    file.write(f"Accuracy: {accuracy * 100:.2f}%\n\n")

    file.write(
        classification_report(
            y_test,
            y_pred,
            target_names=iris.target_names
        )
    )


# --------------------------------------------------
# Create confusion matrix plot
# --------------------------------------------------

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=iris.target_names
)

disp.plot()

plt.title("KNN Iris Classifier - Confusion Matrix")
plt.tight_layout()

plt.savefig(
    RESULTS_DIR / "confusion_matrix.png"
)

plt.show()


print("\nEvaluation completed successfully.")
print(f"Results saved to: {RESULTS_DIR}")