import numpy as np
from collections import Counter

# Question - 1
outcomes = np.array(np.meshgrid(range(1, 9), range(1, 9), range(1, 9), range(1, 9))).T.reshape(-1, 4)
sums = np.sum(outcomes, axis=1)

sum_frequencies = Counter(sums)
total_outcomes = 8**4

probability_distribution = {s: freq / total_outcomes for s, freq in sum_frequencies.items()}
for sum_value, probability in sorted(probability_distribution.items()):
    print(f"Sum: {sum_value}, Probability: {probability:.5f}")


# # Question - 2
# correct_answers = [0, 1, 2, 3, 4, 5]
# frequencies = [5, 7, 10, 20, 12, 6]
#
# total_students = sum(frequencies)
#
# mean_sum = 0
# for i in range(len(correct_answers)):
#     mean_sum += correct_answers[i] * frequencies[i]
# mean = mean_sum / total_students
#
#
# variance_sum = 0
# for i in range(len(correct_answers)):
#     variance_sum += frequencies[i] * (correct_answers[i] - mean) ** 2
# variance = variance_sum / total_students
#
# print(f"Mean: {mean:.2f}")
# print(f"Variance: {variance:.2f}")



# # Question - 3
# values = [1, 2, 3, 4]
# probabilities = [0.3, 0.4, 0.2, 0.1]
# random_numbers = np.random.choice(values, size=2000, p=probabilities)
# print(random_numbers[:2000])

import pandas

df[['First_Name', 'Last_Name']] = df['Name'].str.split(' ', n=1, expand=True)
