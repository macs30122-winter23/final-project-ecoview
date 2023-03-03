"""
Note the abnormality of New Hampshire in 2020 

The logic is to compare the the value of each feature as well as the rank of this state
against the median state of US as well as typical red and blue state 

Compute the correlation of emmision per capita against political leaning
"""
import numpy as np 
import pandas as pd 
import os 

root_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
df = pd.read_csv(os.path.join(root_path,
                              'data',
                              'clean_data',
                              'final_data_with_population.csv'))

df = df[df['year'] == 2020]
print(df[df.State == 'New Hampshire'])
df.describe()

# correlation of emmision per capita 
df_avg_by_year = df.groupby('State')['eminssion per capita'].mean().to_numpy()
df_politics = pd.read_csv(os.path.join(root_path,
                              'data',
                              'clean_data',
                              'political_leaning',
                              'political_leaning_2018-2021.csv'))
df_p_by_year = df_politics.groupby('State')['score'].mean().to_numpy()

