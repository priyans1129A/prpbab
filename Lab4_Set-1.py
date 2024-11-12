# red = 30
# blue = 20
# green = 10
# total = red+blue+green
# prob = input("Enter ur choice: ")
#
# match prob:
#     case "Red" | "red":
#         print(red/total)
#     case "Blue" | "blue":
#         print(blue/total)
#     case "Green" | "green":
#         print(blue/total)



sensitivity = 0.93
specificity = 0.88
prevalence = 0.03

P_no_breach = 1 - prevalence
P_breach_detected = (sensitivity * prevalence) + ((1 - specificity) * P_no_breach)
P_actual_breach_given_detected = (sensitivity * prevalence) / P_breach_detected
print(P_actual_breach_given_detected)


# Question - 3

P_disorder = 0.1
P_fatigue= 0.65
P_joint_pain = 0.55
P_fatigue_joint_pain = 0.2

P_fatigue_joint_pain_disorder = P_fatigue * P_joint_pain

P_disorder_fatigue_joint_pain = (P_fatigue_joint_pain_disorder * P_disorder) / P_fatigue_joint_pain

print(f"Probability of patient has the disorder given that they have both fatigue and joint pain is {P_disorder_fatigue_joint_pain:.4f}")
