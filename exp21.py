import numpy as np
import pandas as pd
import scipy.stats as stats
data = pd.read_csv('rare_elements.csv')
def calculate_sample_size(confidence_level, precision):
    z = abs(stats.norm.ppf((1 - (1 - confidence_level) / 2)))
    sample_size = ((z / precision) ** 2) * (data.shape[0] / (data.shape[0] - 1))
    return int(np.ceil(sample_size))
sample_size = int(input("Enter the desired sample size: "))
confidence_level = float(input("Enter the desired confidence level (e.g., 0.95 for 95% confidence): "))
precision = float(input("Enter the desired level of precision: "))
required_sample_size = calculate_sample_size(confidence_level, precision)

if required_sample_size > data.shape[0]:
    print("The required sample size is greater than the available data size.")
    print(f"Available data size: {data.shape[0]}")
else:
    z=abs(stats.norm.ppf((1-(1-confidence_level)/2)))
    random_sample = np.random.choice(data['Concentration'], size=required_sample_size, replace=False)
    sample_mean = np.mean(random_sample)
    std_error = np.std(random_sample, ddof=1) / np.sqrt(required_sample_size)
    margin_of_error = z * std_error
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    print(f"Sample Mean: {sample_mean:.4f}")
    print(f"Confidence Interval ({confidence_level * 100}%): ({lower_bound:.4f}, {upper_bound:.4f})")
