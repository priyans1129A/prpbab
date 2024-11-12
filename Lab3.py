import numpy as np
from collections import Counter

# list = ["I", "am", "Studying", "in", "BU"]

# sampled_words = np.random.choice(list, size=1500, replace=True)
#
# sample_BU = []
#
# for i in range(len(sampled_words) - 1):
#     if sampled_words[i] == "BU":
#         sample_BU.append(sampled_words[i + 1])
#
# sample_count = Counter(sample_BU)
# total_samples = len(sample_BU)
#
# probabilities = {word: count / total_samples for word, count in sample_count.items()}
#
# print("Sample Space for 'BU':", sample_BU)
# print("Probabilities:", probabilities)



# # Question-2
# import numpy as np
#
# list = ["H", "T"]
# arr = np.array(list)
#
# n = int(input("Enter any number: "))
# sampled_toss = np.random.choice(arr, size=n, replace=True)
#
# sample_toss = []
#
# for i in range(len(sampled_toss) - 1):
#     if sampled_toss[i] == "H":
#         sample_toss.append(sampled_toss[i])
#
# sample_count = len(sample_toss)
#
# probabilities = sample_count/n
#
# print(probabilities)



# import numpy as np
# import itertools
#
# N = int(input("Enter the value of n: "))
#
# sample_space = [''.join(x) for x in itertools.product('HT', repeat=N)]
#
# # print("Sample Space:")
# # for outcome in sample_space:
# #     print(outcome)
#
# # print("Probablity:-")
# # for i in range(N):
# #     print(i+1, "Head: ")
#
# probabilities = []
# for k in range(N + 1):
#     count_k_heads = sum(1 for outcome in sample_space if outcome.count('H') == k)
#     probability_k_heads = count_k_heads / len(sample_space)
#     probabilities.append(probability_k_heads)
#
# for k, prob in enumerate(probabilities):
#     print(f"P(X = {k}) = {prob:.4f}")



# # Sample Question
# k = int(input("Enter the value of k: "))
# n = int(input("Enter the value of n: "))
# sum = 0
# current_term = 0
# for i in range(1,n+1):
#     current_term = current_term*10+k
#     sum += current_term
#
# print(sum)