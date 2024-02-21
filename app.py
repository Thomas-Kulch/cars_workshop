import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

import variables as v

#App headers
st.header('Market of Used Cars')
st.write('Browse our inventory of used cars. \n\n Narrow your selection by filtering by Manufacturer and Model Year. And no, you can\'t see the photos.')

#Selection box for manufacturers
selection = st.selectbox('Select a Manufacturer', v.unique_manufacturer)


#Slider
year_range = st.slider('Year Filter',value=(v.min_year,v.max_year),min_value=v.min_year,max_value=v.max_year)
actual_range = list(range(year_range[0],year_range[1]+1))

car_filtered = v.car_ads[(v.car_ads.manufacturer_name == selection) & (v.car_ads.year_produced.isin(actual_range))]

car_filtered.rename(columns={'manufacturer_name':'Manufacturer Name',
                             'model_name':'Model Name',
                             'transmission':'Transmission',
                             'color':'Color',
                             'odometer_value':'Odometer Value',
                             'year_produced':'Year Produced',
                             'engine_type':'Engine Type',
                             'engine_capacity':'Engine Capacity',
                             'body_type':'Body Type',
                             'has_warranty':'Has Warranty?',
                             'state':'State',
                             'price_usd':'Price (USD)',
                             'number_of_photos':'No. of Photos'},inplace=True)




st.dataframe(car_filtered.set_index(car_filtered.columns[0]).style.format({'Odometer Value':'{:,}',
                                                                           'Year Produced':'{}',
                                                                           'Engine Capacity':'{:.1f}',
                                                                           'Price (USD)':'{:,.2f}'}))
