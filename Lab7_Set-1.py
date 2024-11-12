## Question - 1
# from math import comb
#
# def binomial_distribution(n, p, k):
#     return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
#
# n = 3
# p = 4 / 10
#
# probabilities = {k: binomial_distribution(n, p, k) for k in range(n + 1)}
#
# for k, prob in probabilities.items():
#     print(f"Probability of drawing {k} fused bulbs: {prob:.4f}")


## Question - 2
# def geometric_pmf(p, k):
#     return (1 - p) ** (k - 1) * p
#
# def expected_value(p):
#     return 1 / p
#
# p = 0.02
# k = 7
# prob_seventh_component = geometric_pmf(p, k)
# expected_components = expected_value(p)
# print(f"Probability that the first defect is found on the 7th component: {prob_seventh_component:.4f}")
# print(f"Expected number of components to test until the first defect: {expected_components:.2f}")


# # Question - 3
# import math
# from scipy.stats import poisson
# sales_data = [(10, 2), (15, 3), (20, 4), (25, 3), (30, 2)]
#
# total_sales = sum(sales * days for sales, days in sales_data)
# total_days = sum(days for _, days in sales_data)
# mean_sales = total_sales / total_days
#
# prob_exact_20 = poisson.pmf(20, mean_sales)
#
# prob_less_than_15 = poisson.cdf(14, mean_sales)
#
# std_dev_sales = math.sqrt(mean_sales)
#
# print(f"(1) Mean number of croissants sold per hour: {mean_sales:.2f}")
# print(f"(2) Probability of selling exactly 20 croissants: {prob_exact_20:.4f}")
# print(f"(3) Probability of selling fewer than 15 croissants: {prob_less_than_15:.4f}")
# print(f"(4) Standard deviation of croissants sold per hour: {std_dev_sales:.2f}")



# Question - 4
import math
from scipy.stats import poisson


def find_min_agents(lambda_, target_prob):
    k = 0
    while poisson.cdf(k, lambda_) < target_prob:
        k += 1
    return k


lambda_ = 4.5
target_prob = 0.90

min_agents = find_min_agents(lambda_, target_prob)

print(f"Minimum number of agents needed: {min_agents}")
