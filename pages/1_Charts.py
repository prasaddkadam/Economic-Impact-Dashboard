import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv('data/Economic_Impact_Data.csv')
st.title('Standalone Charts')
vizOptions = st.selectbox('Select topic to visualize', options=['GDP Per Capita','Life Expectancy (Years)', 
                                                                 'Population', 'Annual CO2 Emissions (Tonnes)', 
                                                                 'Child Mortality'])

chartOptions = st.selectbox('Select chart type', options=['Line', 'Bar Chart', 'Scatter'])

country_list = data['Country'].unique().tolist()

if vizOptions == 'GDP Per Capita':
    countryOptions = st.multiselect('Which Countries would you like to view?', country_list, ['India'])
    dataPlot = data[data['Country'].isin(countryOptions)]
    st.markdown(
        """#### The average economic production per person in a nation is gauged by the Gross Domestic Product (GDP) per capita. It offers insightful information about the population's level of living and economic health. GDP per capita provides a comparison of economic prosperity between nations and across time by dividing the total GDP by the population."""
    )

    if chartOptions == 'Line':
        fig = px.line(dataPlot, x='Year', y=vizOptions,color='Country', range_x=[1950,2018],
                   line_shape="spline", range_y=[0,dataPlot[vizOptions].max()])
        fig.update_layout(height=450,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
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
    elif chartOptions == 'Bar Chart':
        fig = px.bar(dataPlot,x='Country', y=vizOptions, color='Country', animation_frame='Year',
              range_y=[0,dataPlot[vizOptions].max()])
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
        fig.update_layout(height=450,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
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
    elif chartOptions == 'Scatter':
        fig = px.scatter(dataPlot, x='Year', y=vizOptions,color='Country', range_x=[1950,2018], 
                      animation_frame='Year', range_y=[0,dataPlot[vizOptions].max()], size='Population')
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
        fig.update_layout(height=500,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
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
        #fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
        st.write(fig)

elif vizOptions == 'Life Expectancy (Years)':
    countryOptions = st.multiselect('Which Countries would you like to view?', country_list, ['India'])
    dataPlot = data[data['Country'].isin(countryOptions)]
    st.markdown(
        """#### Life expectancy is the key metric for assessing population health. The mortality during the whole life period is represented by life expectancy. It provides information on the typical death age for a population."""
    )

    if chartOptions == 'Line':
        fig = px.line(dataPlot, x='Year', y=vizOptions,color='Country', range_x=[1950,2018],
                   line_shape="spline", range_y=[0,100])
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

        fig.update_layout(height=450,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
        st.write(fig)
    elif chartOptions == 'Bar Chart':
        fig = px.bar(dataPlot,x='Country', y=vizOptions, color='Country', animation_frame='Year',
              range_y=[0,100])
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

        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
        fig.update_layout(height=450,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
        st.write(fig)
    elif chartOptions == 'Scatter':
        fig = px.scatter(dataPlot, x='Year', y=vizOptions,color='Country', range_x=[1950,2018], 
                      animation_frame='Year', range_y=[0,100], size='Population')
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
        
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
        fig.update_layout(height=500,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
        #fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
        st.write(fig)

elif vizOptions == 'Population':
    countryOptions = st.multiselect('Which Countries would you like to view?', country_list, ['India'])
    dataPlot = data[data['Country'].isin(countryOptions)]
    st.markdown(
        """#### The total number of people residing in a given region is represented by the demographic variable known as population. Understanding social, economic, and environmental processes within an area depends on it. We can better understand the quantity, distribution, and trends in population increase over time by visualising population data."""
    )

    if chartOptions == 'Line':
        fig = px.line(dataPlot, x='Year', y=vizOptions,color='Country', range_x=[1950,2018],
                   line_shape="spline", range_y=[0,dataPlot[vizOptions].max()])
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
        
        fig.update_layout(height=450,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
        st.write(fig)
    elif chartOptions == 'Bar Chart':
        fig = px.bar(dataPlot,x='Country', y=vizOptions, color='Country', animation_frame='Year',
              range_y=[0,dataPlot[vizOptions].max()])
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
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
        fig.update_layout(height=450,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
        st.write(fig)
    elif chartOptions == 'Scatter':
        fig = px.scatter(dataPlot, x='Year', y=vizOptions,color='Country', range_x=[1950,2018], 
                      animation_frame='Year', range_y=[0,dataPlot[vizOptions].max()], size='Population')
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
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
        fig.update_layout(height=500,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
        #fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
        st.write(fig)

elif vizOptions == 'Annual CO2 Emissions (Tonnes)':
    countryOptions = st.multiselect('Which Countries would you like to view?', country_list, ['India'])
    dataPlot = data[data['Country'].isin(countryOptions)]
    st.markdown(
        """#### A crucial environmental indicator, annual CO2 emissions count the quantity of carbon dioxide that humans emit into the atmosphere each year. Fossil fuel combustion for energy production, transportation, and industrial activities is the main source of these emissions. The influence on climate change and global warming is highlighted by using annual CO2 emissions statistics to create a clear depiction of the scope and patterns of human-induced carbon dioxide pollution."""
    )
       
    if chartOptions == 'Line':
        fig = px.line(dataPlot, x='Year', y=vizOptions,color='Country', range_x=[1950,2018],
                   line_shape="spline", range_y=[0,dataPlot[vizOptions].max()])
        fig.update_layout(height=450,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
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
    elif chartOptions == 'Bar Chart':
        fig = px.bar(dataPlot,x='Country', y=vizOptions, color='Country', animation_frame='Year',
              range_y=[0,dataPlot[vizOptions].max()])
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
        fig.update_layout(height=450,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
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
    elif chartOptions == 'Scatter':
        fig = px.scatter(dataPlot, x='Year', y=vizOptions,color='Country', range_x=[1950,2018], 
                      animation_frame='Year', range_y=[0,dataPlot[vizOptions].max()], size='Population')
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
        fig.update_layout(height=500,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
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
        #fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
        st.write(fig)

elif vizOptions == 'Child Mortality':
    countryOptions = st.multiselect('Which Countries would you like to view?', country_list, ['India'])
    dataPlot = data[data['Country'].isin(countryOptions)]
    st.markdown(
        """#### Child mortality is the unfortunate loss of life of children before they turn five. It is a crucial determinant of the general health and well-being of a society, reflecting the accessibility and standard of healthcare, as well as socioeconomic situations, nutrition, sanitation, and hygiene. High rates of child mortality are an upsetting reality in many areas of the world."""
    )

    if chartOptions == 'Line':
        fig = px.line(dataPlot, x='Year', y=vizOptions,color='Country', range_x=[1950,2018],
                   line_shape="spline", range_y=[0,dataPlot[vizOptions].max()])
        fig.update_layout(height=450,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
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
    elif chartOptions == 'Bar Chart':
        fig = px.bar(dataPlot,x='Country', y=vizOptions, color='Country', animation_frame='Year',
              range_y=[0,dataPlot[vizOptions].max()])
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
        fig.update_layout(height=450,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
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
    elif chartOptions == 'Scatter':
        fig = px.scatter(dataPlot, x='Year', y=vizOptions,color='Country', range_x=[1950,2018], 
                      animation_frame='Year', range_y=[0,dataPlot[vizOptions].max()], size='Population')
        fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 100
        fig.update_layout(height=500,width = 900, margin={"r":0,"t":30,"l":0,"b":0})
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
        #fig.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5
        st.write(fig)
else:
    st.write('Please Select what you wish to Vizualise!')
