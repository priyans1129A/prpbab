import random
import numpy as np
import matplotlib.pyplot as plt

# # Question - 1
# # Function to calculate the mean of a dataset
def calculate_mean(data):
    return np.sum(data) / len(data)

# def calculate_covariance(x_data, y_data):
#     mean_x = calculate_mean(x_data)
#     mean_y = calculate_mean(y_data)
#
#     covariance = np.sum((x_data - mean_x) * (y_data - mean_y)) / (len(x_data))
#     return covariance
#
# x_data = np.random.randint(1, 100, size = 100)
# y_data = np.random.randint(1, 100, size = 100)
#
# covariance = calculate_covariance(x_data, y_data)
# print(f"Covariance: {covariance:.2f}")


# # Question 2
def calculate_std(data):
    return np.std(data)

def calculate_pearson(x, y):
    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)
    std_x = calculate_std(x)
    std_y = calculate_std(y)

    covariance = np.mean((x - mean_x) * (y - mean_y))
    pearson_correlation = covariance / (std_x * std_y)

    return pearson_correlation

np.random.seed(0)
data_x = np.random.rand(1000)
data_y = np.random.rand(1000)

pearson_coefficient = calculate_pearson(data_x, data_y)
print(f"Pearson Correlation between two data points: {pearson_coefficient: .2f}")


# Question - 3
# Possible outcomes of rolling a fair six-sided die
outcomes = np.arange(1, 7)

# PMF for a fair die (each outcome has an equal probability of 1/6)
pmf = np.full(6, 1/6)

# Plotting the PMF
plt.bar(outcomes, pmf, width=0.5, color='skyblue', edgecolor='black')
plt.title("PMF of Rolling a Fair Six-Sided Die")
plt.xlabel("Outcome")
plt.ylabel("Probability")
plt.xticks(outcomes)
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()