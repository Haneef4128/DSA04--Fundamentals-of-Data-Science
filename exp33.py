import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
np.random.seed(0)
num_samples = 100
engine_size = np.random.rand(num_samples) * 2 + 1
horsepower = np.random.randint(100, 400, size=num_samples)
car_price = 20000 + 10000 * engine_size + 50 * horsepower + np.random.randn(num_samples) * 5000
data = pd.DataFrame({
    'EngineSize': engine_size,
    'Horsepower': horsepower,
    'Price': car_price
})
features = ['EngineSize', 'Horsepower']
target = 'Price'
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Price')
plt.ylabel('Predicted Price')
plt.title('Actual vs. Predicted Car Prices')
plt.show()
