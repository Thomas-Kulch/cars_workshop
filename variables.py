import pandas as pd
import numpy as np

#read csv
car_ads = pd.read_csv('cars_workshop.csv')

#drop unwanted column
car_ads = car_ads.drop(car_ads.columns[0],axis=1)

#get distinct car manufacturers and store in a variable
unique_manufacturer = car_ads['manufacturer_name'].unique()

#assign min and max year to functions for the year slider on the app
min_year,max_year = int(car_ads['year_produced'].min()), int(car_ads['year_produced'].max())
