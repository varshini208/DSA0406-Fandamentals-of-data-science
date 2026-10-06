import numpy as np
student_scores = np.array([
    [80, 75, 90, 70],
    [85, 80, 88, 75],
    [90, 85, 92, 80],
    [75, 70, 85, 78]
])
subjects = ["Math", "Science", "English", "History"]
averages = np.mean(student_scores, axis=0)                # Calculate average of each subject

for i in range(4):                                        # Display averages
    print(subjects[i], "Average:", averages[i])

highest_index = np.argmax(averages)                       # Find subject with highest average

print("Subject with highest average:", subjects[highest_index])
print("Highest average:", averages[highest_index])