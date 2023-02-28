"""
Data Visualization:
distinct features in US Maps:
1. Environmenatl Factors
2. Political Leaning

ordered by time 
Author: Anmin Yang 
"""
import numpy as np 
import pandas as pd 
import os 

root_path = os.path.abspath(os.path.join(os.getcwd(), "../"))
df_feature_path = os.path.join(root_path,
                       'data', 'clean_data',
                        'final_data_with_population.csv')
df_feature = pd.read_csv(df_feature_path)