import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

import variables as v

#Inventory Filter
st.header('Market of Used Cars')
st.write('Browse our inventory of used car. \n\n Narrow your selection by filtering by Manufacturer and Model Year. And no, you can\'t see the photos.')

#Selection box for manufacturers
selection = st.selectbox('Select a Manufacturer', v.unique_manufacturer)

#Slider range
year_range = st.slider('Year Filter',value=(v.min_year,v.max_year),min_value=v.min_year,max_value=v.max_year)
actual_range = list(range(year_range[0],year_range[1]+1))

#Adding the selection box and slider outcomes to the results of the dataframe.
car_filtered = v.car_ads[(v.car_ads.manufacturer_name == selection) & (v.car_ads.year_produced.isin(actual_range))]

#renaming dataframe columns to clean it up on the app
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


#print the inventory table on the app with formatting
st.dataframe(car_filtered.set_index(car_filtered.columns[0]).style.format({'Odometer Value':'{:,}',
                                                                           'Year Produced':'{}',
                                                                           'Engine Capacity':'{:.1f}',
                                                                           'Price (USD)':'{:,.2f}'}))



#New section of the page: Price Analysis
st.header('Price Analysis')
st.write("""
###### Let's analyze what influences price the most. We will check how distribution of price varies depending on transmission, engine, body type or state.
""")

#create a list for our drop down and then add the dropdown
list_for_hist = ['transmission','engine_type','body_type','state']
price_menu = st.selectbox('Select a Category',list_for_hist)

fig1 = px.histogram(v.car_ads,x='price_usd',color=price_menu)
fig1.update_layout(title='<b> Split of Price by {}'.format(price_menu))

st.plotly_chart(fig1)


#New report: Price Dependency
st.write("""
###### Now let's check how price is affected by things like odometer reading, engine capacity or number of photos in the ads
""")

#create a list for our drop down and then add the dropdown
list_for_scatter = ['odometer_value','engine_capacity','number_of_photos']
scatter_select = st.selectbox('Price dependency on:',list_for_scatter)

#create scatter plot
fig2 = px.scatter(v.car_ads,x='price_usd',y=scatter_select,color=v.car_ads['age_category'])

st.plotly_chart(fig2)