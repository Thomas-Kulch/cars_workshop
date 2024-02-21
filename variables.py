import pandas as pd
import numpy as np

#read csv
car_ads = pd.read_csv('cars_workshop.csv')

#drop unwanted column
car_ads = car_ads.drop(car_ads.columns[0],axis=1)

#add age column
car_ads['age'] = 2024 - car_ads['year_produced']

#get distinct car manufacturers and store in a variable
unique_manufacturer = car_ads['manufacturer_name'].unique()

#assign min and max year to functions for the year slider on the app
min_year,max_year = int(car_ads['year_produced'].min()), int(car_ads['year_produced'].max())


#add filter function
def car_age(x):
    if x<5:
        return '<5'
    elif x<=5 and x<10:
        return '5-10'
    elif x>=10 and x<20:
        return '10-20'
    else:
        return '>20'

#add age category column to filter scatter plot by
car_ads['age_category'] = car_ads['age'].apply(car_age)