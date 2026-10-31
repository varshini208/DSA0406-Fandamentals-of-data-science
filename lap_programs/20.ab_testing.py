import numpy as np
from scipy import stats

design_A = [0.12, 0.15, 0.10, 0.14, 0.13,
            0.16, 0.11, 0.15, 0.14, 0.13]

design_B = [0.16, 0.18, 0.14, 0.17, 0.15,
            0.19, 0.16, 0.18, 0.17, 0.16]

mean_A = np.mean(design_A)
mean_B = np.mean(design_B)

t_stat, p_value = stats.ttest_ind(
    design_A, design_B, equal_var=False)

print("Mean Conversion Rate of Design A:", round(mean_A, 3))
print("Mean Conversion Rate of Design B:", round(mean_B, 3))
print("P-value:", round(p_value, 5))

if p_value < 0.05:
    print("There is a significant difference.")
else:
    print("There is no significant difference.")