# Hi all, We are EcoView 

We are dedicated to exploring the relationship between political leaning and sustainability in each state of the United States.

To achieve this goal, we have created a GitHub repository containing all the raw data and code used in our project. 

# Our Project: 

  - Exploring the Link between the Political Leaning & Sustainability of Each State In U.S.

## Hypothesis:

  - States with more sustainability efforts are more democratic

## Result:

  - In cross-sectional analysis, sustainable policy score is the only steady indicator of political leaning. The higher the sustainable policy score, the bluer the states.

  - **Emission_per_capital, Policy_Score, Share** has a lag effect on Political leaning which aligns to our hypothesis






## Structure of our GitHub: 

- [**Data**](https://github.com/macs30122-winter23/final-project-ecoview/tree/main/data)

  - raw_data

    - AQI(Air quality Index)
    - Bill
    - Emission
    - Employment
    - Energy_Efficiency_score
    - Electricity_Generation_ratio 
    - Political_leaning
    - State_population

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
  - analysis (any operation on the master table)

- [**Presentation**](https://github.com/macs30122-winter23/final-project-ecoview/tree/main/scripts)
  - Slides (explictly illustrating our project and result)

## Library
  - Pandas: 1.3.3
  - Numpy: 1.21.2
  - Matplotlib.pyplot: 3.4.3
  - Seaborn: 0.11.2
  - Plotly: 5.4.0
  - Sklearn: 1.0
  - Statsmodels: 0.13.0

