import seaborn as sns
import matplotlib.pyplot as plt

# Fictional dataset
hours_studied = [2, 3, 5, 1, 6, 4, 7, 8, 5, 3]
exam_scores = [60, 70, 75, 50, 85, 65, 90, 95, 80, 70]

# Creating a scatter plot using seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(x=hours_studied, y=exam_scores, color='red')

# Adding labels and title
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.title('Relationship Between Hours Studied and Exam Scores')

# Displaying the plot
plt.show()
