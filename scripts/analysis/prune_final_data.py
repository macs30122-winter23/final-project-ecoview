"""
Modify final data
1. drop redundent columns
2. add state population( https://www.statsamerica.org/sip/rank_list.aspx?rank_label=pop1)
"""
import numpy as np 
import pandas as pd 
import os 

root_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
data_path = os.path.join(root_path, 
                            'data', 'clean_data',
                            'final_data.csv')
df = pd.read_csv(data_path)

# drop redundent columns 
drop_name = ['Employment', 'TRADITIONAL RATIO', 
             'CO2_emissions', 'CH4_emissions', 'N2O_emissions']
df.drop(drop_name, axis=1, inplace=True)

# add state population 
df_population = pd.read_excel(os.path.join(root_path,
                                            'data', 'raw_data',
                                            'state_population',
                                            'state_population.xlsx'),
                                            engine='openpyxl')
df = df.merge(df_population)

# save
df.to_csv(os.path.join(root_path,
                    'data', 'clean_data','final_data_with_population.csv'))