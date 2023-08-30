import numpy as np
from scipy import stats
def calculate(conversions, visitors):
    return conversions / visitors

def ab_test(conversions_A, visitors_A, conversions_B, visitors_B):
    rate_A = calculate(conversions_A, visitors_A)
    rate_B = calculate(conversions_B, visitors_B)

    t_statistic, p_value = stats.ttest_ind_from_stats(rate_A, np.sqrt(rate_A / visitors_A),
                                                     visitors_A, rate_B, np.sqrt(rate_B / visitors_B),
                                                     visitors_B)
    return p_value
def main():
    conversions_A = 120
    visitors_A = 1000
    conversions_B = 150
    visitors_B = 1000
    p_value = ab_test(conversions_A, visitors_A, conversions_B, visitors_B)

    alpha = 0.05
    if p_value < alpha:
        print("There is a statistically significant difference in between website design A and website design B.")
    else:
        print("There is no statistically significant difference in between website design A and website design B.")
if __name__ == "__main__":
    main()
