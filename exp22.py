import pandas as pd
import numpy as np
from scipy import stats
def calculate(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_error = stats.sem(data)
    t_critical = stats.t.ppf((1 + confidence) / 2, df=n-1)
    margin_of_error = t_critical * std_error
    lower= mean - margin_of_error
    upper = mean + margin_of_error
    return (lower, upper)
def main():
    ratings = [4.5, 4.8, 4.2, 4.9, 4.6, 4.7, 4.3, 4.8, 4.4, 4.6]
    confidence_interval = calculate(ratings )
    print("Sample Mean Rating:", np.mean(ratings))
    print("95% Confidence Interval:", confidence_interval)
if __name__ == "__main__":
    main()
