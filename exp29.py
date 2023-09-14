import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model with increased max_iter
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Calculate predict
predict = model.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, predict)
precision = precision_score(y_test, predict, average='weighted')
recall = recall_score(y_test, predict, average='weighted')
f1 = f1_score(y_test, predict, average='weighted')

# Display evaluation metrics
print(f"Evaluation metrics for the model:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
