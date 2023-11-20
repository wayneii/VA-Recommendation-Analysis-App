
import streamlit as st
import importlib
import sys
import os
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu


st.set_page_config(layout='wide')

# Read the data
df = pd.read_excel('ACWV Recommendations with Categories and Similarity Groups.xlsx')


# Make the year column an integer
df['Year'] = df['Year'].astype(int)

################################## BANNER ######################################################################
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
  <h1 style="color:white;">ACWV Recommendations</h1>
</div>
""", unsafe_allow_html=True)

################################## PAGES TAB ##################################################################

# #Initialize session state for the main (entrypoint) page
# if 'current_page' not in st.session_state:
#     st.session_state['current_page'] = 'Home'  # This sets 'Home' as the default page

# #Add Home to the list of pages
# pages = ['Home']

# #Discover the rest of the pages in the 'pages' directory
# pages_dir = "pages"
# pages += [f[:-3] for f in os.listdir(pages_dir) if f.endswith('.py')]

# #Sort the pages to control the order in which they appear
# pages.sort()

################################ FILTER DATA ####################################################################
#columns = st.columns((1,1))

# Year selection
elected_year = st.sidebar.slider('Select a year range', min_value=df['Year'].min(), max_value=df['Year'].max(), value=(df['Year'].max()-10, df['Year'].max()))

# Extracting the minimum and maximum years
selected_min_year = elected_year[0]
selected_max_year = elected_year[1]



# Filter data based on selected years
# Filter the DataFrame based on the selected years
filtered_df = df[(df['Year'] >= selected_min_year) & (df['Year'] <= selected_max_year)]


# Now you would aggregate the data as per your requirement, for example, if you're interested in the 'Category' column:
aggregated_data = filtered_df['Category'].value_counts()

################################### STACKED BAR CHART ####################################################################################


#st.markdown("<h3 style='text-align: center;'>Volume Over Time</h3>", unsafe_allow_html=True)
#st.markdown(f"<h4 style='text-align: center;'>{selected_min_year} to {selected_max_year}</h4>", unsafe_allow_html=True)


colors = ['#1f77b4',  # muted blue
          '#E6E3D3',  # muted cream
          '#17becf',  # blue-teal
          '#9467bd',  # muted purple
          '#008080',  # cooked asparagus green
          '#98df8a',  # pale green
          '#DAA520',  # goldenrod
          '#c5b0d5',  # pale purple
          '#7f7f7f']  # middle gray
       


# Group by 'Year' and 'Category' and count the occurrences
aggregated_data = filtered_df.groupby(['Year', 'Category']).size().reset_index(name='Count')

# Reshape the data to have years as the index and categories as columns
pivot_df = aggregated_data.pivot(index='Year', columns='Category', values='Count').fillna(0)

# Create the stacked bar chart
fig = px.bar(pivot_df, 
             barmode='stack', 
             title=f'Volume Over Time: {selected_min_year} - {selected_max_year}',
             labels={'value':'Count', 'variable':'Category'},
             color_discrete_sequence=colors)

# Customize the layout
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Count of Recommendations',
    legend_title='Category',
    #plot_bgcolor='white',
    font=dict(size=12)
)

st.title('')
st.caption("The following figures give an aggregated view of the recommendations and results of every ACWV committee meeting since 1996. The recommendations were classified and grouped using text analytics methods. There are several interactive components including date range and category selection. Use the navigation bar to the left to navigate to other features.")

# Show the figure
st.plotly_chart(fig, use_container_width=True)

st.caption("In the figure above, the color is associated with the category each recommendation was placed in allowing the viewer to quickly see both the total count of recommendations per year as well as the count of recommendations from each category year over year.")


#with columns[1]:
    #st.markdown("<br><br><br>", unsafe_allow_html=True)
    #st.markdown("<p style='color: grey;'>In the figure above, the color is associated with the category each recommendation was placed in allowing the viewer to quickly see both the total count of recommendations per year as well as the count of recommendations from each category year over year.</p>", unsafe_allow_html=True)

st.markdown("___")


################################### RESULTS DONUT CHART #################################################################################

st.markdown(f"<h6>Recommendation Results: {selected_min_year} - {selected_max_year} </h6>", unsafe_allow_html=True)

# Assuming 'result_counts' contains the counts of each result
result_counts = filtered_df['Result '].value_counts()

# Create a donut chart with a larger hole
fig = px.pie(result_counts, 
             values=result_counts.values, 
             names=result_counts.index, 
             hole=0.5, 
             color_discrete_sequence=['#1f77b4','#17becf', '#E6E3D3'])  # Increase hole size

# Customizing the chart
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(
    autosize=False,
    width=800,  # Width of the chart
    height=600  # Height of the chart
)

# Display the donut chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.caption("In the figure above, the color is associated with the result of the recommendations, concur, concur in principle, or non-concur. The size of the pie slice is associated with the percentage of recommendations that reached a given result for the specified time period.")

st.markdown("___")

#################################### BAR CHART #######################################################
# create two columns
columns = st.columns((1,1))

categories = df['Category'].unique()

# Initialize selected_categories with all categories by default
selected_categories = categories.tolist()


with columns[0]:
    selected_category = st.radio(
    'Category Selection', categories.tolist()
    )
    st.title("")
    st.caption("In the figure to the right, the color of bar distinuishes between the following recommendation results: concur, non-concur, or concur in principle. The hight of the bar is gives the total count of recommendations for a given year for the selected category.")


# # 'Select All' checkbox
# select_all = st.sidebar.checkbox('Select All', value=True)

# if select_all:
#     selected_categories = categories.tolist()
#     title = f"Results by Year for All Categories"
# else:
#     # Allow individual selection when 'Select All' is not checked
#     selected_categories = []
#     for category in categories:
#         if st.sidebar.checkbox(category, key=category):
#             selected_categories.append(category)
#     title = f"Results by Year for Categories: {', '.join(selected_categories)}"

# Filter the DataFrame based on the selected categories
filtered_df = df[(df['Category'] == selected_category)]

# Group and count the data
grouped_df = filtered_df.groupby(['Year', 'Result ']).size().reset_index(name='Count')

# Display the chart
with columns[1]:
   # Bar Chart and Title
    st.markdown(f"<h6>Result of Recommendations Over Time: {selected_category}</h6>", unsafe_allow_html=True)
    fig = px.bar(grouped_df, x='Year', y='Count', color='Result ',
             labels={'Count':'Count of Recommendations'}, 
             barmode='stack', 
             color_discrete_sequence=['#1f77b4', '#E6E3D3','#17becf'])  
    st.plotly_chart(fig, use_container_width=True)



st.markdown("___")

# #################################### LINE CHART OF THEMES OVER THE YEARS #######################################################################

# st.markdown("<h1 style='text-align: center;'>Themes Over All Years</h1>", unsafe_allow_html=True)


# import plotly.express as px

# # Count the occurrences of each category per year
# category_counts = df.groupby(['Year', 'Category']).size().reset_index(name='Counts')

# # Pivot the results to get years as index and categories as columns
# category_counts_pivot = category_counts.pivot(index='Year', columns='Category', values='Counts').fillna(0)

# # Melt the DataFrame for Plotly
# category_counts_melted = category_counts_pivot.reset_index().melt(id_vars=['Year'], var_name='Category', value_name='Counts')

# # Create a line chart using Plotly Express
# fig = px.line(category_counts_melted, x='Year', y='Counts', color='Category')

# # Update layout for better readability and customization
# fig.update_layout(
#     xaxis_title='Year',
#     yaxis_title='Count',
#     hovermode='x unified',
#     autosize=False,
#     width=800,  # Width of the chart
#     height=600,  # Height of the chart
#     legend_title='Category'
# )

# # Update traces for better visualization, if necessary
# #for trace in fig.data:
#  #   trace.name = trace.name.split('=')[1]  # Updating trace names to be more readable

# # Display the plot in Streamlit
# st.plotly_chart(fig)

