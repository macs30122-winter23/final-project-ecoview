#Import necessary packages
import pandas as pd
import numpy as np
import re
from sklearn.linear_model import LinearRegression

#Import data from csv
employment_2021 = pd.read_csv('2021_employment.csv')
employment_2020 = pd.read_csv('2020_employment.csv')
employment_2019 = pd.read_csv('2019_employment.csv')
employment_2018 = pd.read_csv('2018_employment.csv')

#Format column names
employment_2021.columns = employment_2021.columns.str.replace('\r', ' ')
employment_2020.columns = employment_2020.columns.str.replace('\r', ' ')
employment_2018.set_axis(['Rank', 'State', 'Total', 'Solar', 'Wind', 'Energy Efficiency', 'Clean Vehicles'], axis=1, inplace=True)

#Split data stored in one column to two
employment_2020[['Year-End Job Lost (%)', 'Year-End Job Lost (Counts)']] = employment_2020['Year-End Jobs Lost (Total)'].apply\
    (lambda x: pd.Series(str(x).split('\r')))

#Cleaning and formatting data
employment_2020['Year-End Job Lost (Counts)'] = employment_2020['Year-End Job Lost (Counts)'].str.replace('\(|\)', '')

#drop unnecessary columns
employment_2020.drop(columns='Job Growth\rJune–Dec. 2020', inplace=True)
employment_2020.drop(columns='Year-End Jobs Lost (Total)', inplace=True)

#Add column Rank
employment_2018['Rank'] = range(1,10)

#Replace misread data with correct data
employment_2018.replace(['CaOliHfoIOrn ia', '2T5e xas', 'FloVrIiRdGaINIA', '1075,1720,39 34', \
    '1 5 8 , 6 5 2',  '8,019226 ,507 96', '1 0 ,5 2 8 9', '5,785 7', ',054 4,461', \
    ',6533181,554,322 0', '1 1 8 , 4 1 42, 19', '9 , 3 6 0 1'], ['California', 'Texas', \
    'Florida', '512,934', '158,652', '126,507', '10,528', '5,785', '4,461', '318,542', '118,412', '9,360'], inplace=True)

#Add rows that was not picked up by Tabula
employment_2018.loc[2, employment_2018.columns.to_list()] = [3, 'Florida', '158,652', '10,528', '4,461', '118,412', '9,360']
employment_2018.loc[9] = [10, 'Virginia', '95,158', '4,241', '1,628', '78,670', '5,436']

#Drop unnecessary data
employment_2018 = employment_2018.drop(-1)

#Copy the state employment data of all sectors from BLS table
data = '2,247,478 346,310 3,604,759 1,366,290 19,509,906 5,166,741 3,180,764 1,929,411 488,853 413,052 10,440,201 \
    1,391,585 5,147,592 668,088 890,197 6,417,561 3,700,452 3,392,608 1,754,487 1,493,793 2,084,842 2,107,116 694,218 \
    3,276,534 3,836,139 4,946,944 2,167,356 3,124,221 1,279,445 3,110,835 536,528 1,039,902 1,555,119 778,188 4,551,736 \
    961,059 9,543,300 4,054,735 5,110,694 404,266 5,818,260 1,042,722 1,845,647 2,103,977 6,548,713 557,474 2,387,273 \
    466,504 3,367,292 14,180,672 1,626,958 340,554 4,453,902 3,955,209 1,744,388 804,798 3,110,404 293,284 1,055,984'
state = 'Alabama............................... Alaska................................. Arizona.........................\
    ....... Arkansas.............................. California.............................Los Angeles-Long Beach-Glendale1\
    . . . . Colorado.............................. Connecticut............................ Delaware.....................\
    ......... District of Columbia..................... Florida................................Miami-Miami Beach-Kendall1\
    . . . . . . . . . . . Georgia............................... Hawaii................................. Idaho.............\
    ..................... Illinois.................................Chicago-Naperville-Arlington Heights1. . . Indiana.........\
    ....................... Iowa.................................. Kansas................................ Kentucky.............\
    ................. Louisiana.............................. Maine................................. Maryland...................\
    ........... Massachusetts......................... Michigan...............................Detroit-Warren-Dearborn2. . . . . .\
    . . . . . . .. Minnesota............................. Mississippi............................. Missouri....................\
    ........... Montana............................... Nebraska.............................. Nevada.............................\
    ... New Hampshire........................ New Jersey............................ New Mexico............................ New \
    York..............................New York City........................ North Carolina.......................... North Dakota\
    ........................... Ohio..................................Cleveland-Elyria2..................... Oklahoma.............\
    ................ Oregon................................ Pennsylvania........................... Rhode Island...................\
    ........ South Carolina......................... South Dakota.......................... Tennessee............................. \
    Texas................................. Utah.................................. Vermont............................... Virginia\
    ................................ Washington............................Seattle-Bellevue-Everett1.............. West Virginia\
    ........................... Wisconsin............................. Wyoming.............................. Puerto Rico'

#Cleaning state employment data
state_employment_2019 = data.split()
cleaned_state =  re.sub("\.+", ",", state)
cleaned_state = re.sub("(\,\s)+", ",", cleaned_state)
cleaned_state = re.sub("\d", "", cleaned_state)
cleaned_state = cleaned_state.split(',')

#Create Dataframe of state employment data
state_employment = pd.DataFrame(data={'State': cleaned_state, 'Employment': state_employment_2019})

#Drop unneeded data
state_employment = state_employment.drop([5, 11, 16, 26, 41, 54, 58])

#Change the State name to match with other dataframe
state_employment.at[9, 'State'] = 'District of Col.'

#Merge state employment data with clean energy sector employment data
merged_df_2019 = pd.merge(employment_2019, state_employment, on='State')

#Transform textual data to numerical data
merged_df_2019['All Employment'] = merged_df_2019['Employment'].str.replace(',', '').astype(int)
merged_df_2019['Total'] = merged_df_2019['Total'].str.replace(',', '').astype(int)

#Calculate desired attribute
merged_df_2019['Share of Statewide Workforce'] = (merged_df_2019['Total'] / merged_df_2019['All Employment']).round(4)

#Drop unnecessary columns
merged_df_2019.drop(columns=['Employment', 'All Employment'], inplace=True)

#Export data
merged_df_2019.to_csv('data/2019_employment_cleaned.csv', index=False)

#Select needed columns for year 2021
short_2021 = employment_2021.drop(columns=['Rank', 'Renewable Energy', 'Energy Efficiency', \
    'Grid & Storage', 'Clean Fuels', 'Clean Vehicles', 'Growth'])

#Transform textual data to numerical data
short_2021['Total Clean Energy Jobs'] = short_2021['Total Clean Energy Jobs'].str.replace(',', '').astype(int)
short_2021['Share of Statewide Workforce %'] = short_2021['Share of Statewide Workforce'].str.replace('%', '').astype(float)

#Drop unnecessary columns
short_2021.drop(columns='Share of Statewide Workforce', inplace=True)

#Select needed columns for year 2020
short_2020 = employment_2020[['State', 'Total Clean Energy Employment', 'Share of Statewide Workforce']]

#Cleaning data
#Transform textual data to numerical data
short_2020['State'] = short_2020['State'].str.replace('\r', ' ')
short_2020['Total Clean Energy Jobs'] = short_2020['Total Clean Energy Employment'].str.replace(',', '').astype(int)
short_2020['Share of Statewide Workforce %'] = short_2020['Share of Statewide Workforce'].str.replace('%', '').astype(float)

#Drop unnecessary columns
short_2020.drop(columns=['Share of Statewide Workforce', 'Total Clean Energy Employment', 'Growth'], inplace=True)

#Select needed columns for year 2019
short_2019 = merged_df_2019[['State', 'Total', 'Share of Statewide Workforce']]

#Sort dataframe by state
short_2021 = short_2021.sort_values('State')
short_2020 = short_2020.sort_values('State')
short_2019 = short_2019.sort_values('State')
short_2021.reset_index(drop=True, inplace=True)
short_2020.reset_index(drop=True, inplace=True)
short_2019.reset_index(drop=True, inplace=True)

#Calculate desired variables for year 2021
short_2021['Growth'] = (short_2021['Total Clean Energy Jobs'] - short_2020['Total Clean Energy Jobs'])/\
    short_2020['Total Clean Energy Jobs']
short_2021['Share of Statewide Workforce %'] = short_2021['Share of Statewide Workforce %'] / 100

#Calculate desired variables for year 2020
short_2020['Share of Statewide Workforce %'] = short_2020['Share of Statewide Workforce %'] / 100
short_2020['Growth'] = (short_2020['Total Clean Energy Jobs'] - short_2019['Total']) / short_2019['Total']

#Transform textual data to numerical data
employment_2018['Total'] = employment_2018['Total'].str.replace(',', '').astype(int)

#Add states not recorded by the original data
short_2018 = pd.merge(short_2019['State'], employment_2018, how='left', on='State').fillna(0)

#Drop unnecessary columns
short_2018 = short_2018.drop(columns=['Rank', 'Solar', 'Wind', 'Energy Efficiency', 'Clean Vehicles'])

#Copy the state employment data of all sectors from BLS table
emp_2018 = '2,183,939 358,363 3,377,091 1,351,032 19,260,712 5,118,365 3,046,551 1,888,060 480,151 404,462 \
    10,159,334 1,377,133 5,098,068 679,831 847,719 6,479,722 3,754,106 3,356,351 1,678,369 1,477,124 2,055,146 \
    2,107,710 698,887 3,198,871 3,749,077 4,899,261 2,113,355 3,062,941 1,276,449 3,055,212 526,070 1,016,122 \
    1,479,897 757,967 4,429,810 935,343 9,534,415 4,118,765 4,962,163 406,979 5,751,639 1,033,339 1,845,590 \
    2,101,664 6,402,980 555,440 2,316,095 458,008 3,223,746 13,737,417 1,562,805 346,808 4,322,135 3,752,500 \
    1,674,059 782,251 3,141,387 290,567 1,084,403'

#Clean all employment data
emp_2018 = emp_2018.split()
del_i = [5, 11, 16, 26, 37, 41, 54, -1]
for i in sorted(del_i, reverse=True):
    del emp_2018[i]

#Add all employment data to the dataframe, transform data type
short_2018['All Emp'] = emp_2018
short_2018['All Emp'] = short_2018['All Emp'].str.replace(',', '').astype(int)

#Predict 2018 clean energy employment from 2019 to 2021 data
X = np.array([2019, 2020, 2021]).reshape(-1, 1)
X_pred = [[2018]]
model = LinearRegression()
for i in range(51):
    y = np.array([short_2019.at[i, 'Total'], short_2020.at[i, 'Total Clean Energy Jobs'], \
        short_2021.at[i, 'Total Clean Energy Jobs']]).reshape(-1, 1)
    model.fit(X, y)
    y_pred = model.predict(X_pred)
    short_2018.loc[i, 'Linear Regression Pred'] = y_pred[0][0]

#If there are states in 2018 with recorded employment data, we use it.
#Otherwise we use the predicted data
for i in range(51):
    if short_2018.at[i, 'Total'] == 0.0:
        short_2018.loc[i, 'Total Comb'] = short_2018.at[i, 'Linear Regression Pred']
    else:
        short_2018.loc[i, 'Total Comb'] = short_2018.at[i, 'Total']

#Calculate desired variable growth
short_2019['Growth'] = (short_2019['Total'] - short_2018['Total Comb'])/short_2018['Total Comb']
short_2018['Share of Statewide Workforce'] = short_2018['Total Comb'] / short_2018['All Emp']

#Import 2017 clean energy employment data
short_2017 = pd.DataFrame({'State': short_2018['State']})
short_2017['Total'] = 0
short_2017.at[4, 'Total'] = 301000
short_2017.at[43, 'Total'] = 147000
short_2017.at[32, 'Total'] = 111000
short_2017.at[9, 'Total'] = 109000
short_2017.at[25, 'Total'] = 87000
short_2017.at[13, 'Total'] = 84000
short_2017.at[33, 'Total'] = 81000
short_2017.at[21, 'Total'] = 80000
short_2017.at[35, 'Total'] = 79000
short_2017.at[46, 'Total'] = 76000

#Predict 2017 clean energy employment from 2019 to 2021 data
for i in range(51):
    y = np.array([short_2019.at[i, 'Total'], short_2020.at[i, 'Total Clean Energy Jobs'], \
        short_2021.at[i, 'Total Clean Energy Jobs']]).reshape(-1, 1)
    X = np.array([2019, 2020, 2021]).reshape(-1, 1)
    model.fit(X, y)
    y_pred = model.predict([[2017], [2018]])
    short_2017.loc[i, 'Linear Regression Pred'] = y_pred[0][0]

#If there are states in 2017 with recorded employment data, we use it.
#Otherwise we use the predicted data
for i in range(51):
    if short_2017.at[i, 'Total'] == 0:
        short_2017.loc[i, 'Total Comb'] = short_2017.at[i, 'Linear Regression Pred']
    else:
        short_2017.loc[i, 'Total Comb'] = short_2017.at[i, 'Total']

#Calculate desired variable growth
short_2018['Growth'] = (short_2018['Total Comb'] - short_2017['Total Comb']) / short_2017['Total Comb']

#Merge all data together
master_df = pd.DataFrame({'State': short_2018['State'], '2018 Employment': short_2018['Total Comb'], \
    '2018 Share': short_2018['Share of Statewide Workforce'], '2018 Growth': short_2018['Growth'],\
    '2019 Employment': short_2019['Total'], '2019 Share': short_2019['Share of Statewide Workforce'],\
    '2019 Growth': short_2019['Growth'],'2020 Employment': short_2020['Total Clean Energy Jobs'], \
    '2020 Share': short_2020['Share of Statewide Workforce %'], '2020 Growth': short_2020['Growth'],\
    '2021 Employment': short_2021['Total Clean Energy Jobs'], '2021 Share': short_2021['Share of Statewide Workforce %'], \
    '2021 Growth': short_2021['Growth']})

#Export data
master_df.to_csv('employment_all_year.csv', index=False)