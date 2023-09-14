import pandas as pd
import numpy as np
data = {
    'City': ['City A', 'City A', 'City A', 'City B', 'City B', 'City B', 'City C', 'City C', 'City C'],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03'],
    'Temperature': [25, 28, 30, 20, 22, 23, 18, 20, 19]}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
mean = df.groupby('City')['Temperature'].mean()
std= df.groupby('City')['Temperature'].std()
tempranges = df.groupby('City')['Temperature'].apply(lambda x: x.max() - x.min())
print("Mean Temperature for Each City:")
print(mean)
print("\nStandard Deviation of Temperature for Each City:")
print(std)
print(f"\nCity with the Highest Temperature Range: {tempranges.idxmax()}")
print(f"City with the Most Consistent Temperature: {std.idxmin()}")
