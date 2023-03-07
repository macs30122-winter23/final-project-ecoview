# Hi all, We are EcoView 

We are dedicated to exploring the relationship between political leaning and sustainability in each state of the United States.

To achieve this goal, we have created a GitHub repository containing all the raw data and code used in our project. 

## Our Project: 

  - Exploring the Link between the Political Leaning & Sustainability of Each State In U.S.

## Hypothesis:

  - States with more sustainability efforts are more democratic

## Result:

  - In cross-sectional analysis, sustainable policy score is the only steady indicator of political leaning. The higher the sustainable policy score, the bluer the states.

  - **Emission_per_capital, Policy_Score, Share** has a lag effect on Political leaning which aligns to our hypothesis


## Structure of our GitHub: 

- [**Data**](https://github.com/macs30122-winter23/final-project-ecoview/tree/main/data)

  - raw_data

    - AQI(Air quality Index) [link](https://aqs.epa.gov/aqsweb/airdata/download_files.html)
    - Bill [link](https://www.govtrack.us)
    - Emission [link](https://e2.org/resources/?type_param=report_post)
    - Employment [link](https://www.epa.gov/ghgreporting)
    - Energy_Efficiency_score [link](https://www.aceee.org/)
    - Electricity_Generation_ratio [link](https://www.eia.gov/)
    - Political_leaning [link](https://fivethirtyeight.com/features/how-red-or-blue-is-your-state-your-congressional-district/)
    - State_population [link](https://www.census.gov/)

  - clean_data

    - a concated tabel (master table) that aggregate all the data we use (.csv)
    - GOOD_DAY_RATIO
    - BILL
    - Emission_PER_CAPITAL
    - EMPLOYMENT
    - SHARE
    - GROW
    - Energy_Efficiency_score
    - Electricity_Generation_ratio 
    - Political_leaning 

- [**Figs**](https://github.com/macs30122-winter23/final-project-ecoview/tree/main/figs)
  
  The visualization result of our project

- [**Scripts**](https://github.com/macs30122-winter23/final-project-ecoview/tree/main/scripts)

  - Data_Collection (any operation on getting data)
  - Data_Visualization (any code on visualizing)
  - preprocess (any script that contribute to raw_data, clean_data and the master table)
  - Analysis (any operation on the master table)

- [**Presentation**](https://github.com/macs30122-winter23/final-project-ecoview/tree/main/scripts)
  
  - [Slides (explictly illustrating our project and result)](https://github.com/macs30122-winter23/final-project-ecoview/blob/main/presentation/Ecoview.pptx)
  - [Project writeup (a more in depth document of our project)] (TBD)
  - [Video](TBD)
  
## Division

  - Violet Huang {Data collection: (Clean_Energy_Jobs_Employment, Clean_Energy_Jobs_Growth, Clean_Energy_Jobs_Share), Preproces: (normalization of dataset, Clean_Energy_Jobs missing value), Analysis: (OLS Regression), Visualization: (heatmap)}
  - Hantao Xiao {Data collection: (Bill, Emission, Energy_Efficiency_score, Electricity_Generation_ratio), Preprocess:(Electricity_Generation_ratio, Emission_PER_CAPITAL), Analysis: (Panel Regression), Visualization: (Iterable Tableau Dashboard)}
  - Anmin Yang {Data collection: (Political Leaning, State Population, AQI), Preprocess: (good_day_ratio, political leaning missing value, final data incorpretation), Analysis: (dimension reduction), Visualization: (features on US map)}

## Library
  - Pandas: 1.3.3
  - Numpy: 1.21.2
  - Matplotlib.pyplot: 3.4.3
  - Seaborn: 0.11.2
  - Plotly: 5.4.0
  - Sklearn: 1.0
  - Statsmodels: 0.13.0
  - re: 2.2.1
  - tabula: 1.0.6
