# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report 

# Read the dataset
df = pd.read_csv("dataset/Iris.csv")

# Remove Id column
df = df.drop("Id", axis=1)

# Display first five rows
print("First 5 Rows:\n")
print(df.head())

# Dataset shape
print("\nShape of Dataset:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Information
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Count Plot
plt.figure(figsize=(6,4))
sns.countplot(x="Species", data=df)
plt.title("Count of Each Iris Species")
plt.show()

# Pair Plot
sns.pairplot(df, hue="Species")
plt.show()

# Heatmap
plt.figure(figsize=(8,6))

numeric_df = df.drop("Species", axis=1)

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Feature Correlation")
plt.show()

# Features (Input)
X = df.drop("Species", axis=1)

# Target (Output)
y = df["Species"]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# Create Model
model = DecisionTreeClassifier(random_state=42)

# Train Model
model.fit(X_train, y_train)

print("Model Trained Successfully!")

# Predict
y_pred = model.predict(X_test)

print("\nPredicted Values:")
print(y_pred)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy*100:.2f}%")

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

print("\nClassification Report:\n")

print(classification_report(y_test, y_pred))

import joblib

# Save the trained model
joblib.dump(model, "iris_model.pkl")

print("Model saved successfully as iris_model.pkl")