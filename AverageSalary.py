import pandas as pd

df = pd.read_csv('data.csv')

average_salary = df['salary'].mean()
print('Average salary:', average_salary)
