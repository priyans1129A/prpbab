# Question - 1

yellow = 35
red = 15
blue = 25

total = yellow+red+blue

P_yellow = yellow/total
P_not_blue = 1-(blue/total)
P_red_given_red_yellow = red/(red+yellow)

print(P_yellow)
print(P_not_blue)
print(P_red_given_red_yellow)


# Question - 2

P_acc_rain = 0.7
P_acc_fog = 0.5
P_acc_rain_fog = 0.8
print(P_acc_rain_fog)



# Question - 3

sensitivity = 0.91
specificity = 0.86
P_churn = 0.04
P_no_churn = 1 - P_churn

P_churn_predicted_given_no_churn = 1 - specificity

P_churn_predicted = (sensitivity * P_churn) + (P_churn_predicted_given_no_churn * P_no_churn)

P_churn_given_churn_predicted = (sensitivity * P_churn) / P_churn_predicted

print(f"The probability that a customer will actually churn given that the model has predicted churn is {P_churn_given_churn_predicted:.4f}")
