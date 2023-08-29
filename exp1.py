import numpy as np
student_scores = np.array([[60, 70, 90, 65],[89, 67, 98, 20],[90, 87, 89, 70],[87, 90, 76, 87]])
average_scores = np.mean(student_scores, axis=0)
highest_average_subject_index = np.argmax(average_scores)
subjects = ['Math', 'Science', 'English', 'History']
subject_with_highest_average_score = subjects[highest_average_subject_index]
print("Average Scores for each subject:")
for subject, average_score in zip(subjects, average_scores):
    print(f"{subject}: {average_score}")
print(f"\nThe subject with the highest average score is: {subject_with_highest_average_score}")
