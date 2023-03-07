'''
This file normalizes all data by year and exports the normalized data 
'''

#Import necessary packages
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#Read data
raw_df = pd.read_csv('../data/clean_data/final_data.csv')
raw_df_capita = pd.read_csv('../data/clean_data/final_data_with_population.csv')
political_leaning_all = pd.read_csv('../data/clean_data/political_leaning/political_leaning_2018-2021.csv')

#Rename columns
raw_df.rename(columns={'year': 'Year', 'Good Day Ratio': 'Good_Day_Ratio', \
    'GREEN RATIO': 'Green_Ratio', 'SCORE': 'Policy_Score'}, inplace=True)
political_leaning_all.rename(columns={'state': 'State', 'score': 'Political_Leaning'}, inplace=True)

#Combine needed data to one data frame
raw_df['emission_per_capita'] = raw_df_capita['eminssion per capita']
all_df = pd.merge(raw_df, political_leaning_all, on = ['State', 'Year'], how='left')

#Drop redundant columns
all_df = all_df.drop(columns=['CO2_emissions', 'CH4_emissions', 'N2O_emissions', 'TRADITIONAL RATIO', 'Total_emissions'])

#Export data
all_df.to_csv('all_included_data.csv')

#Create dataframe for each year for normalization
df_2018 = all_df[all_df['Year'] == 2018]
df_2018 = df_2018.reset_index(drop=True)
df_2019 = all_df[all_df['Year'] == 2019]
df_2019 = df_2019.reset_index(drop=True)
df_2020 = all_df[all_df['Year'] == 2020]
df_2020 = df_2020.reset_index(drop=True)
df_2021 = all_df[all_df['Year'] == 2021]
df_2021 = df_2021.reset_index(drop=True)

#Select columns to transform
transform_column = all_df.columns[2:].to_list()

#Initialize scaler
scaler = MinMaxScaler(feature_range=(0,1))

#Create normalized dataframe for each year
norm_2018_df = pd.DataFrame()
norm_2019_df = pd.DataFrame()
norm_2020_df = pd.DataFrame()
norm_2021_df = pd.DataFrame()

#Normalize each year's data
norm_2018_df['State'] = df_2018['State']
norm_2018_df['Year'] = df_2018['Year']
norm_2018_df[transform_column] = scaler.fit_transform(df_2018[transform_column])
norm_2019_df['State'] = df_2019['State']
norm_2019_df['Year'] = df_2019['Year']
norm_2019_df[transform_column] = scaler.fit_transform(df_2019[transform_column])
norm_2020_df['State'] = df_2020['State']
norm_2020_df['Year'] = df_2020['Year']
norm_2020_df[transform_column] = scaler.fit_transform(df_2020[transform_column])
norm_2021_df['State'] = df_2021['State']
norm_2021_df['Year'] = df_2021['Year']
norm_2021_df[transform_column] = scaler.fit_transform(df_2021[transform_column])

#Merge normalized data together
norm_concat = pd.concat([norm_2018_df, norm_2019_df, norm_2020_df, norm_2021_df], axis=0)

#Export data
norm_concat.to_csv('all_data_norm.csv')
