#Import necessary packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Read normalized data
# norm_df = pd.read_csv('../data/clean_data/all_data_norm.csv')
norm_df = pd.read_csv('all_data_norm.csv', index_col=0)

#Calculate the average of four years
avg_df = norm_df.drop(columns=['Year']).groupby(['State']).mean()

#Create normalized dataframe for each year
df_2018 = norm_df[norm_df['Year'] == 2018]
df_2019 = norm_df[norm_df['Year'] == 2019]
df_2020 = norm_df[norm_df['Year'] == 2020]
df_2021 = norm_df[norm_df['Year'] == 2021]

#Heat map for average data
_, ax = plt.subplots(figsize=(13,13))
hm_avg = sns.heatmap(avg_df[avg_df.columns.to_list()].corr(),annot=True,cmap='RdYlGn', ax=ax);
hm_avg.figure.savefig('heatmap_average.png')

#Heat map for 2018 data
_, ax = plt.subplots(figsize=(13,13))
hm_2018 = sns.heatmap(df_2018[df_2018.columns[2:].to_list()].corr(),annot=True,cmap='RdYlGn', ax=ax);
hm_2018.figure.savefig('heatmap_2018.png')

#Heat map for 2019 data
_, ax = plt.subplots(figsize=(13,13))
hm_2019 = sns.heatmap(df_2019[df_2019.columns[2:].to_list()].corr(),annot=True,cmap='RdYlGn', ax=ax);
hm_2019.figure.savefig('heatmap_2019.png')

#Heat map for 2020 data
_, ax = plt.subplots(figsize=(13,13))
hm_2020 = sns.heatmap(df_2020[df_2020.columns[2:].to_list()].corr(),annot=True,cmap='RdYlGn', ax=ax);
hm_2020.figure.savefig('heatmap_2020.png')

#Heat map for 2021 data
_, ax = plt.subplots(figsize=(13,13))
hm_2021 = sns.heatmap(df_2021[df_2021.columns[2:].to_list()].corr(),annot=True,cmap='RdYlGn', ax=ax);
hm_2021.figure.savefig('heatmap_2021.png')