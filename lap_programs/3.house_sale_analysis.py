import numpy as np
house_data = np.array([
    [3, 1200, 200000],
    [5, 1800, 350000],
    [6, 2200, 450000],
    [4, 1500, 280000],
    [5, 2000, 400000]])
houses = house_data[house_data[:, 0] > 4]          # Select houses with more than 4 bedrooms

average_price = np.mean(houses[:, 2])              

print("Average sale price:", average_price)