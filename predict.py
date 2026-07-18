import joblib

# Load the saved model
model = joblib.load("iris_model.pkl")

# Sample flower measurements
sample = [[5.1, 3.5, 1.4, 0.2]]

# Predict
prediction = model.predict(sample)

print("Predicted Species:", prediction[0])\

import joblib

model = joblib.load("iris_model.pkl")

sample = [[6.5, 3.0, 5.2, 2.0]]

prediction = model.predict(sample)

print("\nPrediction Result")
print("-----------------")
print("Flower Species:", prediction[0])