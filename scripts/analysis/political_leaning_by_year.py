"""
Concate political leaning data from 2018 to 2022

Note as political geography changes every two years, the 2019 and 2021 data 
takes the mean of the conjacent years
e.g. L(2019) = avg(L(2018), L(2020))

Author: Anmin Yang
"""
import numpy as np 
import pandas as pd 
import os 

root_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
data_path = os.path.join(root_path, 
                            'data', 'raw_data',
                            'political_leaning')
# process two-year data 
df_two_year = pd.read_excel(os.path.join(data_path, 
                                       'political_leaning_2018_2020.xlsx'),
                        engine='openpyxl')
leaning_lst = []
for l in df_two_year.score:
    if 'R' in l:
        leaning_lst.append(-int(l[2:]))
    else:
        leaning_lst.append(int(l[2:]))
df_two_year['score'] = leaning_lst

# load 2022 data 
df_2022 = pd.read_excel(os.path.join(data_path, 
                                    'political_leaning_2022.xlsx'),
                        engine='openpyxl')

# insert estimated data 
df_2019 = df_2022.copy()
df_2019['Year'] = 2019
df_2019['score'] = (df_two_year[df_two_year['Year'] == 2018]['score'].values 
                    +
                    df_two_year[df_two_year['Year'] == 2020]['score'].values) / 2

df_2021 = df_2022.copy()
df_2021['Year'] = 2021
df_2021['score'] = (df_two_year[df_two_year['Year'] == 2020]['score'].values 
                    +
                    df_2022['score'].values) / 2

# concate data 
df = pd.concat([df_two_year,
                df_2019,
                df_2021])
df.to_csv(os.path.join(root_path,
                    'data', 'clean_data',
                    'political_leaning',
                    'political_leaning_2018-2021.csv'),
        index=False)