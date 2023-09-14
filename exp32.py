import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
np.random.seed(0)
num_samples = 100
house_size = np.random.rand(num_samples) * 200 + 800
house_price = 300000 + 1500 * house_size + np.random.randn(num_samples) * 50000
data = pd.DataFrame({'Size': house_size, 'Price': house_price})
X = data[['Size']]
y = data['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = model.score(X_test, y_test)
reliability = model.score(X_train, y_train)
print(f"Model Accuracy: {accuracy:.2f}")
print(f"Model Reliability: {reliability:.2f}") 
plt.scatter(X_test, y_test, label='Test Data')
plt.plot(X_test, y_pred, color='red', label='Regression Line')
plt.xlabel('House Size')
plt.ylabel('House Price')
plt.title('Linear Regression Model: House Size vs. Price')
plt.legend()
plt.show()
