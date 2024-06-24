import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('students_exams.csv')

x = df['writing score'].hist(bins=[10,20,30,40,50,60,70,80,90,100])
print(x)
plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('students_exams.csv')

# # Plotting the histogram
# plt.hist(df['writing score'], bins=[10,20,30,40,50,60,70,80,90,100])
# plt.title('Distribution of Writing Scores')
# plt.xlabel('Writing Score')
# plt.ylabel('Frequency')
# plt.show()