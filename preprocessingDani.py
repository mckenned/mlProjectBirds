import pandas as pd

df = pd.read_csv('/Users/daniellemckenney/Programming/erasmusCourses/ML/mlProjectsBirbs/mlProjectBirds/dataset.csv', sep="\t", on_bad_lines="warn")

# Useful stats: 
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df['locality'].value_counts())
print(df.isnull().sum())
