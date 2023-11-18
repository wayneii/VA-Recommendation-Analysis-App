
import streamlit as st
import importlib
import sys
import os
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


# Read the data
df = pd.read_excel('ACWV Recommendations with Categories and Similarity Groups.xlsx')

# Make the year column an integer
df['Year'] = df['Year'].astype(int)

#################################### BANNER ##########################################################
# Create a banner using Markdown with HTML/CSS styling
st.markdown("""
<style>
.banner {
  background-color: black;
  padding: 10px;
  border-radius: 5px;
  text-align: center;
}
</style>

<div class="banner">
  <h1 style="color:white;">Recommendations Broken-Down by Theme</h1>
</div>
""", unsafe_allow_html=True)

#################################### BAR CHART #######################################################

st.sidebar.header("Select Categories")
categories = df['Category'].unique()

# Initialize selected_categories with all categories by default
selected_categories = categories.tolist()

# 'Select All' checkbox
select_all = st.sidebar.checkbox('Select All', value=True)

if select_all:
    selected_categories = categories.tolist()
    title = f"Results by Year for All Categories"
else:
    # Allow individual selection when 'Select All' is not checked
    selected_categories = []
    for category in categories:
        if st.sidebar.checkbox(category, key=category):
            selected_categories.append(category)
    title = f"Results by Year for Categories: {', '.join(selected_categories)}"

# Filter the dataframe based on selected categories
filtered_df = df[df['Category'].isin(selected_categories)]

# Group and count the data
grouped_df = filtered_df.groupby(['Year', 'Result ']).size().reset_index(name='Count')

# Bar Chart and Title
st.markdown(f"<h3 style='text-align: center;'>{title}</h3>", unsafe_allow_html=True)
fig = px.bar(grouped_df, x='Year', y='Count', color='Result ',
             labels={'Count':'Count of Result'}, barmode='stack')

# Display the chart
st.plotly_chart(fig)

