'''
This file plots and saves the heat map for each year's data and the averaged data
'''

#Import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read normalized data
norm_df = pd.read_csv('../data/clean_data/all_data_norm.csv', index_col=0)

#Calculate the average of four years
avg_df = norm_df.drop(columns=['Year']).groupby(['State']).mean()

#Create normalized dataframe for each year
df_2018 = norm_df[norm_df['Year'] == 2018]
df_2019 = norm_df[norm_df['Year'] == 2019]
df_2020 = norm_df[norm_df['Year'] == 2020]
df_2021 = norm_df[norm_df['Year'] == 2021]

def plot_heatmap(data, name):
    '''
    This function plots and saves the heat map for the given data frame
    Inputs:
        data (dataframe): dataframe for the analysis
        name (string): name of the heat map to be saved
    '''
    _, ax = plt.subplots(figsize=(13,13))
    if name == 'heatmap_average.png':
        hm = sns.heatmap(data[data.columns.to_list()].corr(),annot=True,cmap='RdYlGn', ax=ax);
    else:
        hm = sns.heatmap(data[data.columns[2:].to_list()].corr(),annot=True,cmap='RdYlGn', ax=ax);
    hm.figure.savefig(name)

plot_heatmap(avg_df, 'heatmap_average.png')
plot_heatmap(df_2018, 'heatmap_2018.png')
plot_heatmap(df_2019, 'heatmap_2019.png')
plot_heatmap(df_2020, 'heatmap_2020.png')
plot_heatmap(df_2021, 'heatmap_2021.png')