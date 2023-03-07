'''
This file normalizes all data by year and exports the normalized data 
'''

#Import necessary packages
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

#Read data
raw_df = pd.read_csv('../../data/clean_data/final_data.csv')
raw_df_capita = pd.read_csv('../../data/clean_data/final_data_with_population.csv')
political_leaning_all = pd.read_csv('../../data/clean_data/political_leaning/political_leaning_2018-2021.csv')

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

def normalize(data):
    '''
    Normalize the given data frame for each year and merge them to a master data frame
    Input:
        data (Dataframe): Dataframe containing unnormalized data for year 2018 to year 2021
    '''
    
    #Select columns to transform
    transform_column = data.columns[2:].to_list()

    #Initialize scaler
    scaler = MinMaxScaler(feature_range=(0,1))

    #Create Master dataframe
    master_df = pd.DataFrame()
    
    #loop over four years
    for year in range(2018, 2022):
        #Create dataframe for each year for normalization
        df = data[data['Year'] == year]
        df= df.reset_index(drop=True)

        #Create normalized dataframe for each year
        norm_df = pd.DataFrame()

        #Normalize each year's data
        norm_df['State'] = df['State']
        norm_df['Year'] = df['Year']
        norm_df[transform_column] = scaler.fit_transform(df[transform_column])

        #Merge normalized data together
        master_df = pd.concat([master_df, norm_df], axis=0)
    
    #Export data
    master_df.to_csv('all_data_norm.csv')

#Normalize the data we have
normalize(all_df)
