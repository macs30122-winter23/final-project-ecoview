'''
This file runs four OLS Regression models between X and y for year 2018 to year 2021.
For each year, it runs
- descriptive statistics of the dataset
- Distribution of the variables
- OLS Regression
- Residual plots for variables with significant correlation
In OLS Regreesion, the independent variables (x) include:
- Clean Energy Job Employment (Employment), Clean Energy Job Share (Share), Clean Energy Job Growth (Growth),
- Good Day Ratio (Good_Day_Ratio), Emission per capita (emission_per_capita),
- Policy Score(Policy_Score), Number of Bills (Number_bill), 
- Green Ratio (Green_Ratio)
The dependent variable (y) is the Political Leaning (Political_Leaning)
'''

#Import required packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

#Read normalized data
norm_df = pd.read_csv('../../data/clean_data/all_data_norm.csv', index_col=0)

#Create normalized dataframe for each year
df_2018 = norm_df[norm_df['Year'] == 2018]
df_2019 = norm_df[norm_df['Year'] == 2019]
df_2020 = norm_df[norm_df['Year'] == 2020]
df_2021 = norm_df[norm_df['Year'] == 2021]

def run_regression(data, year):
    '''
    This function gives descriptive statistics of the dataset, plots the distribution of the variables, 
    runs OLS Regression, and plots the residual plots for variables with significant correlation.
    Input:
        data (Dataframe): data for the year we want to analyze
        year (int): the year we want to analyze
    '''
    # check descriptive statistics of the dataset
    print('Descriptive statistics of all variables for year {}'.format(year))
    print(data.describe())

    # plots the distribution of the variables
    print('Checking distribution of variables for year {}'.format(year))
    dist_plot = sns.pairplot(data.drop(columns='Year'))
    plt.show()
    dist_plot.figure.savefig('distribution_of_variables_' + str(year) + '.png')

    #runs OLS regression
    x = data.iloc[:, 2:-1]
    x = sm.add_constant(x)
    y = data['Political_Leaning']
    ols_model = sm.OLS(y, x)  
    results = ols_model.fit()
    print('OLS regression results for year {}'.format(year)) 
    print(results.summary())

    #plot residual plot for policy_score
    print('Show residual plot of Policy_Score, the only variable that is significant for all four years')
    fig = sm.graphics.plot_ccpr(results, "Policy_Score")
    plt.show()

    #plot residual plot for policy_score for year 2019
    if year ==2019:
        print('Show residual plot of Growth for year 2019')
        fig = sm.graphics.plot_ccpr(results, "Growth")
        plt.show()

run_regression(df_2018, 2018)
run_regression(df_2019, 2019)
run_regression(df_2020, 2020)
run_regression(df_2021, 2021)
