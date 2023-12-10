import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data = pd.read_csv('data/Economic_Impact_Data.csv')
st.title('Comparative Viz Tool')
st.markdown(
    """#### Use our Comparison tool to customize your scatter chart. By selecting your desired variables for the x and y axes, you can compare different factors and explore their relationships. Additionally, you have the flexibility to choose the number of countries to include in your analysis, allowing for targeted comparisons and regional insights. Our interactive interface empowers you to uncover trends, patterns, and correlations that matter to you. So go ahead, unleash your curiosity, and dive into the world of data visualization by customizing your scatter chart now!"""
)

xAxis = st.selectbox('Select your X-Axis', options=['GDP Per Capita','Life Expectancy (Years)', 
                                                                 'Annual CO2 Emissions (Tonnes)', 'Child Mortality'])

yAxis = st.selectbox('Select your Y-Axis', options=['GDP Per Capita','Life Expectancy (Years)', 
                                                                 'Annual CO2 Emissions (Tonnes)', 'Child Mortality'])

country_list = data['Country'].unique().tolist()
countryOptions = st.multiselect('Which Countries would you like to view?', country_list, ['India'])

scatterPlot = data[data['Country'].isin(countryOptions)]

fig = px.scatter(scatterPlot, x=xAxis, y=yAxis, animation_frame='Year', animation_group='Country', 
                  size='Population', color='Country', range_y = [0,scatterPlot[yAxis].max() + 10], 
                  range_x = [0,scatterPlot[xAxis].max() + 10])
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
fig.update_layout(height=600,width = 1000, margin={"r":0,"t":0,"l":0,"b":0})
fig.add_shape(
        # Rectangle with reference to the plot
            type="rect",
            xref="paper",
            yref="paper",
            x0=0,
            y0=0,
            x1=1.0,
            y1=1.0,
            line=dict(
                color="black",
                 width=1,
             )
         )

st.write(fig)