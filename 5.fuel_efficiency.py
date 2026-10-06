import numpy as np
fuel_efficiency = np.array([30, 35, 40, 45])
average = np.mean(fuel_efficiency)

# Compare first and second car
percentage_improvement = ((fuel_efficiency[1] - fuel_efficiency[0])/ fuel_efficiency[0]) * 100

print("Average fuel efficiency:", average)
print("Percentage improvement:", percentage_improvement, "%")