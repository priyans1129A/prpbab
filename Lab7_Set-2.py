# # Question - 1
# from scipy.stats import hypergeom
# import numpy as np
#
# N = 100
# K = 30
# n = 10
#
# k_values = np.arange(0, n + 1)
# probabilities = hypergeom.pmf(k_values, N, K, n)
#
# print("Number of defective pencils | Probability")
# for k, p in zip(k_values, probabilities):
#     print(f"{k:24} | {p:.4f}")