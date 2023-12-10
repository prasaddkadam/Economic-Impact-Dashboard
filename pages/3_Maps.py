import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import json

data = pd.read_csv('data/Economic_Impact_Data.csv')
world_data = pd.read_csv('./data/World_Data.csv')
world_geojson = json.load(open('./data/world.geojson', 'r'))

st.title('Data on Maps')
st.markdown(
    """#### Our Data mapping tool gives you the freedom to choose the specific topic you want to visualize, whether it's population, GDP, CO2 emissions, or other relevant data. You can customize the chart based on the year you are interested in, allowing you to observe changes and trends over time."""
)

vizOptions = st.selectbox('Select topic to visualize', options=['GDP Per Capita','Life Expectancy (Years)', 
                                                                 'Population', 'Annual CO2 Emissions (Tonnes)', 
                                                                 'Child Mortality'])

year_list = world_data['Year'].unique().tolist()
yearOptions = st.selectbox('Select the Year', options=year_list)
map_data = world_data[world_data['Year'] == yearOptions]


if vizOptions == 'GDP Per Capita':
    fig = px.choropleth_mapbox(
    map_data,
    locations="id",
    geojson=world_geojson,
    color="GDP Per Capita",
    hover_name="Country",
    title="GDP Per Capita",
    mapbox_style="carto-positron",
    zoom=0.6, center = {"lat":43,"lon":5},
    opacity=0.7,
    #animation_frame = 'Population',
    color_continuous_scale=px.colors.diverging.Portland,)
    fig.update_layout(height=600,width = 1050, margin={"r":0,"t":30,"l":0,"b":0})
    
    st.write(fig)

elif vizOptions == 'Life Expectancy (Years)':
    fig = px.choropleth_mapbox(
    map_data,
    locations="id",
    geojson=world_geojson,
    color="Life Expectancy (Years)",
    hover_name="Country",
    title="Life Expectancy",
    mapbox_style="carto-positron",
    zoom=0.6, center = {"lat":43,"lon":5},
    opacity=0.7,
    color_continuous_scale=px.colors.diverging.Portland)
    fig.update_layout(height=600,width = 1050, margin={"r":0,"t":30,"l":0,"b":0})
    
    st.write(fig)


elif vizOptions =='Population':
    fig = px.choropleth_mapbox(
    map_data,
    locations="id",
    geojson=world_geojson,
    color="Population",
    hover_name="Country",
    title="Population",
    mapbox_style="carto-positron",
    zoom=0.6, center = {"lat":43,"lon":5},
    opacity=0.7,
    color_continuous_scale=px.colors.diverging.Portland)
    fig.update_layout(height=600,width = 1050, margin={"r":0,"t":30,"l":0,"b":0})
    
    st.write(fig)

elif vizOptions == 'Annual CO2 Emissions (Tonnes)':
    fig = px.choropleth_mapbox(
    map_data,
    locations="id",
    geojson=world_geojson,
    color="Annual CO2 Emissions (Tonnes)",
    hover_name="Country",
    title="Annual CO2 Emissions",
    mapbox_style="carto-positron",
    zoom=0.6, center = {"lat":43,"lon":5},
    opacity=0.7,
    color_continuous_scale=px.colors.diverging.Portland)
    fig.update_layout(height=600,width = 1050, margin={"r":0,"t":30,"l":0,"b":0})
    
    st.write(fig)

elif vizOptions == 'Child Mortality':
    fig = px.choropleth_mapbox(
    map_data,
    locations="id",
    geojson=world_geojson,
    color="Child Mortality",
    hover_name="Country",
    title="Child Mortality",
    mapbox_style="carto-positron",
    zoom=0.6, center = {"lat":43,"lon":5},
    opacity=0.7,
    color_continuous_scale=px.colors.diverging.Portland)
    fig.update_layout(height=600,width = 1050, margin={"r":0,"t":30,"l":0,"b":0})
    
    st.write(fig)

else:
    st.write('Please Select Topic to Visualize from above dropdown menu!')