 # 🌸 Iris Flower Classification using Machine Learning

## 📌 Project Overview

This project is developed as part of the **CodeAlpha Data Science Internship**.

The objective is to build a Machine Learning classification model that predicts the species of an Iris flower based on its sepal and petal measurements.

The model is trained using the famous **Iris Dataset** and implemented using Python and Scikit-learn.

---

## 🎯 Objectives

- Load and analyze the Iris dataset.
- Perform Exploratory Data Analysis (EDA).
- Visualize relationships between features.
- Preprocess the dataset.
- Train a Machine Learning classification model.
- Evaluate model performance.
- Predict the species of new Iris flowers.

---

## 📂 Dataset

The project uses the **Iris Dataset**, which contains **150 flower samples** from three species:

- Iris-setosa
- Iris-versicolor
- Iris-virginica

### Features

- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

### Target

- Species

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib

---

## 📊 Exploratory Data Analysis

The following visualizations were created:

- Count Plot
- Pair Plot
- Correlation Heatmap

These visualizations help understand the relationships between different flower measurements and species.

---

## 🤖 Machine Learning Model

Algorithm Used:

- Decision Tree Classifier

The dataset was divided into:

- Training Data: 80%
- Testing Data: 20%

---

## 📈 Model Evaluation

Evaluation Metrics:

- Accuracy Score
- Confusion Matrix
- Classification Report

The trained model achieves high accuracy on the test dataset.

---

## 💾 Model Saving

The trained model is saved using **Joblib**.

```python
joblib.dump(model, "iris_model.pkl")
```

---

## 🔮 Prediction

The saved model can predict the species of a new flower using four measurements.

Example:

```python
sample = [[5.1, 3.5, 1.4, 0.2]]
```

Output:

```
Iris-setosa
```

---

## 📁 Project Structure

```
CodeAlpha_IrisFlowerClassification/
│
├── dataset/
│   └── Iris.csv
├── iris.py
├── predict.py
├── iris_model.pkl
├── requirements.txt
├── README.md
└── images/
```

---

## ▶️ How to Run

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/CodeAlpha_IrisFlowerClassification.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Project

```bash
python iris.py
```

### 4. Run Prediction

```bash
python predict.py
```

---

## 📷 Project Output

- Dataset Analysis
- Data Visualization
- Trained Decision Tree Model
- Accuracy Report
- Confusion Matrix
- Flower Species Prediction

---

## 🚀 Future Improvements

- Add Random Forest Classifier
- Add Support Vector Machine (SVM)
- Deploy using Streamlit
- Create a Web Interface
- Compare multiple ML algorithms

---

 👨‍💻 Author

**Your Name**

CodeAlpha Data Science Intern

---

📜 License

This project is developed for educational purposes as part of the CodeAlpha Data Science Internship.
