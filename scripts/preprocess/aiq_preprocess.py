"""
Sort AQI data
"""

import numpy as np 
import pandas as pd 
import os 

root_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
data_path = os.path.join(root_path, 
                            'data', 'raw_data',
                            'AQI')
NAME = 'annual_aqi_by_county_'

years = ['2018', '2019', '2020', '2021']
df_dic = {}
for year in years: 
    file_name = NAME + year + '.csv'

    df = pd.read_csv(os.path.join(data_path, file_name))

    # preserve columns of interest 
    df = df.loc[:, ['State', 'Year', 'Days with AQI', 'Good Days']]
    df['Good Day Ratio'] = df['Good Days'] / df['Days with AQI']
    df.drop(['Days with AQI', 'Good Days'],
            axis=1, inplace=True)

    # group by state
    df_state = df.groupby(['State']).mean() 
    df_state.reset_index(inplace=True)
    df_state['Year'] = df_state['Year'].astype('int')

    # drop irrelavant observations
    drop_state_lst = ['Country Of Mexico', 'Puerto Rico', 'Virgin Islands']
    df_state = df_state[~df_state['State'].isin(drop_state_lst)]
    df_state.reset_index(drop=True, inplace=True)

    # put in dictionary 
    df_dic[year] = df_state

df_merged = pd.concat([df_dic['2018'],
                        df_dic['2019'],
                        df_dic['2020'],
                        df_dic['2021']])

save_path = os.path.join(root_path, 'data', 'clean_data',
                        'AQI', 'aqi_merged.csv')
df_merged.to_csv(save_path, index=None)