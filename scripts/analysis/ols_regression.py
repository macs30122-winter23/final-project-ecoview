#Import required packages
import pandas as pd
import statsmodels.api as sm

#Read normalized data
norm_df = pd.read_csv('../data/clean_data/all_data_norm.csv', index_col=0)

#Create normalized dataframe for each year
df_2018 = norm_df[norm_df['Year'] == 2018]
df_2019 = norm_df[norm_df['Year'] == 2019]
df_2020 = norm_df[norm_df['Year'] == 2020]
df_2021 = norm_df[norm_df['Year'] == 2021]

#Run OLS regresion for year 2021
x = df_2021.iloc[:, 2:-1]
x = sm.add_constant(x)
y = df_2021['Political_Leaning']
ols_model = sm.OLS(y, x)  
results = ols_model.fit() 
print(results.summary())

#Run OLS regresion for year 2020
x = df_2020.iloc[:, 2:-1]
x = sm.add_constant(x)
y = df_2020['Political_Leaning']
ols_model = sm.OLS(y, x)  
results = ols_model.fit() 
print(results.summary())

#Run OLS regresion for year 2019
x = df_2019.iloc[:, 2:-1]
x = sm.add_constant(x)
y = df_2019['Political_Leaning']
ols_model = sm.OLS(y, x)  
results = ols_model.fit() 
print(results.summary())

#Run OLS regresion for year 2018
x = df_2018.iloc[:, 2:-1]
x = sm.add_constant(x)
y = df_2018['Political_Leaning']
ols_model = sm.OLS(y, x)  
results = ols_model.fit() 
print(results.summary())