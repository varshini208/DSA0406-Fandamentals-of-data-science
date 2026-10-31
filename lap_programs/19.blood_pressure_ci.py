import numpy as np
from scipy import stats
drug = [8, 10, 12, 9, 11, 13, 7, 10, 12, 9]
placebo = [2, 3, 4, 1, 5, 2, 3, 4, 2, 3]
def confidence_interval(data):
    mean = np.mean(data)
    sem = stats.sem(data)
    ci = stats.t.interval(0.95, df=len(data)-1,loc=mean, scale=sem)
    return mean, ci
    
drug_mean, drug_ci = confidence_interval(drug)
placebo_mean, placebo_ci = confidence_interval(placebo)

print("Drug Group:")
print("Mean Reduction:", round(drug_mean, 2))
print("95% Confidence Interval:", drug_ci)

print("\nPlacebo Group:")
print("Mean Reduction:", round(placebo_mean, 2))
print("95% Confidence Interval:", placebo_ci)