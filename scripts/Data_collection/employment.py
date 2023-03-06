#Import necessary packages
import tabula as tb
import pandas as pd
import numpy as np

#Read data for year 2021
data_2021_1 = tb.read_pdf('E2-2022-Clean-Jobs-America.pdf',pages='9',  area=(107, 39, 745, 600), lattice=True)
data_2021_2 = tb.read_pdf('E2-2022-Clean-Jobs-America.pdf',pages='10', area=(107, 39, 310, 650), lattice=True)

# Extract data from read list
data_2021_1 = data_2021_1[0]
data_2021_2 = data_2021_2[0]

#combine data frames to form the whole dtaset for 2021
employment_2021 = pd.concat([data_2021_1, data_2021_2], ignore_index=True, sort=False)

#export data to csv format
employment_2021.to_csv('2021_employment.csv', index=False)

#Read data for year 2020
data_2020_1 = tb.read_pdf('E2-2021-Clean-Jobs-America.pdf',pages='15', area=(470, 40, 732, 575), lattice=True)
data_2020_2 = tb.read_pdf('E2-2021-Clean-Jobs-America.pdf', pages='16', area=(68, 33, 740, 600), lattice=True)
data_2020_3 = tb.read_pdf('E2-2021-Clean-Jobs-America.pdf',pages='17', area=(68, 38, 423, 578), lattice=True)

# Extract data from read list
data_2020_1 = data_2020_1[0]
data_2020_2 = data_2020_2[0]
data_2020_3 = data_2020_3[0]

#Add a column of Rank to the data
data_2020_2_t = data_2020_2.T
for i in range(28):
    data_2020_2_t[i] = data_2020_2_t[i].shift(1)
data_2020_2 = data_2020_2_t.T
data_2020_2['Rank'] = range(11,39)

#Add a column of Rank to the data
data_2020_3_t = data_2020_3.T
for i in range(14):
    data_2020_3_t[i] = data_2020_3_t[i].shift(1)
data_2020_3 = data_2020_3_t.T
data_2020_3['Rank'] = range(39,53)

#combine data frames to form the whole dtaset for 2020
employment_2020 = pd.concat([data_2020_1, data_2020_2, data_2020_3], ignore_index=True, sort=False)

#export data to csv file
employment_2020.to_csv('2020_employment.csv', index=False)

#Read data for year 2019
data_2019_1 = tb.read_pdf('E2-2020-Clean-Jobs-America.pdf',pages='6', area=(392, 35, 580, 600), lattice=True)
data_2019_2 = tb.read_pdf('E2-2020-Clean-Jobs-America.pdf',pages='6', area=(580, 35, 710, 650), lattice=True)
data_2019_3 = tb.read_pdf('E2-2020-Clean-Jobs-America.pdf', pages='7')

# Extract data from read list
data_2019_1 = data_2019_1[0]
data_2019_2 = data_2019_2[0]
data_2019_3 = data_2019_3[0]

#Correct column names for misread data
data_2019_1.rename(columns={'TOTAL*':'Total', 'STATE':'State'}, inplace=True)
data_2019_2 = data_2019_2.columns.to_frame().T.append(data_2019_2, ignore_index=True)
data_2019_2.columns = data_2019_1.columns[1:7]

#Add missed columns
data_2019_2['Rank'] = range(11,21)
data_2019_2['Clean Vehicles'] = [7541, 16369, 3351, 2839, 7423, 9971, 4615, 3212, 3077, 3191]

#Rearrange orders of the columns
cols = data_2019_2.columns.to_list()
new_cols = [cols[6]]
new_cols.extend(cols[:6])
new_cols.append(cols[-1])
data_2019_2 = data_2019_2[new_cols]

#Correct column names for misread data
data_2019_3 = data_2019_3.columns.to_frame().T.append(data_2019_3, ignore_index=True)
data_2019_3.columns = data_2019_1.columns[:]
data_2019_3.drop(labels=0, axis=0, inplace=True)

#combine data frames to form the whole dtaset for 2019
employment_2019 = pd.concat([data_2019_1, data_2019_2, data_2019_3], ignore_index=True, sort=False)

#export data to csv file
employment_2019.to_csv('2019_employment.csv', index=False)

#Read data for year 2018
data_2018_1 = tb.read_pdf('E2-2019-Clean-Jobs-America.pdf',pages='1',  area=(338, 36, 500, 400), lattice=True)

# Extract data from read list
data_2018_1 = data_2018_1[0]

#Export data to csv
data_2018_1.to_csv('2018_employment.csv', index=False)