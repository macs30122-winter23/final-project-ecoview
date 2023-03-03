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
import plotly.express as px
import plotly.data as data
import plotly.io as pio
import matplotlib.pyplot as plt 

# load data 
root_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
df_feature_path = os.path.join(root_path,
                       'data', 'clean_data',
                        'final_data_with_population.csv')
df_feature = pd.read_csv(df_feature_path)

# convert state name to two-letter abbreviations
df_state_ab = pd.read_excel(os.path.join(root_path,
                                         'data', 'utils',
                                         'state_to_postal.xlsx'),
                            engine='openpyxl')
state_map = {}
for _,row in df_state_ab.iterrows():
    state_map[row['State']] = row['Postal']

df_feature['state_ab'] = df_feature['State'].map(state_map)

save_path = os.path.join(root_path, 'figs', 'choropleth')


### main loop 
years = [2018, 2019, 2020, 2021]
features = df_feature.columns.to_list()[2:-1]
for year in years:
    for feature in features:
        df_temp = df_feature[df_feature['year'] == year]
        
        fig = px.choropleth(df_temp,
                            locations='state_ab', 
                            locationmode="USA-states", 
                            scope="usa",
                            color=feature,
                            color_continuous_scale="plasma")

        fig.add_scattergeo(
            locations=df_temp['state_ab'],
            locationmode='USA-states',
            text=df_temp['state_ab'],
            mode='text',
            textfont=dict(color="white", size=20)
            )
        fig.update_layout(
            title=f"{year} {feature}",
            legend_title=f"{feature}",
            font=dict(
                size=30,
            )
        )
        
        fig.write_image(os.path.join(save_path, f'{year} {feature}.png'), 
                        width=10*300, height=5*300, scale=1)