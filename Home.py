
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

# Initialize session state for the main (entrypoint) page
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'Home'  # This sets 'Home' as the default page

# Add Home to the list of pages
pages = ['Home']

# Discover the rest of the pages in the 'pages' directory
pages_dir = "pages"
pages += [f[:-3] for f in os.listdir(pages_dir) if f.endswith('.py')]

# Sort the pages to control the order in which they appear
pages.sort()


################################ FILTER DATA ####################################################################

# Sidebar: Year selection
elected_year = st.sidebar.slider('Select a year range', min_value=df['Year'].min(), max_value=df['Year'].max(), value=(df['Year'].min(), df['Year'].max()))

# Extracting the minimum and maximum years
selected_min_year = elected_year[0]
selected_max_year = elected_year[1]



# Filter data based on selected years
# Filter the DataFrame based on the selected years
filtered_df = df[(df['Year'] >= selected_min_year) & (df['Year'] <= selected_max_year)]


# Now you would aggregate the data as per your requirement, for example, if you're interested in the 'Category' column:
aggregated_data = filtered_df['Category'].value_counts()

################################### STACKED BAR CHART ####################################################################################


st.markdown("<h1 style='text-align: center;'>Themes</h1>", unsafe_allow_html=True)

st.markdown(f"<h3 style='text-align: center;'>{selected_min_year} to {selected_max_year}</h2>", unsafe_allow_html=True)


colors = ['#1f77b4',  # muted blue
          '#2ca02c',  # cooked asparagus green
          '#17becf',  # blue-teal
          '#98df8a',  # pale green
          '#d62728',  # brick red
          '#9467bd',  # muted purple
          '#c5b0d5',  # pale purple
          '#7f7f7f']  # middle gray


# Group by 'Year' and 'Category' and count the occurrences
aggregated_data = filtered_df.groupby(['Year', 'Category']).size().reset_index(name='Count')

# Reshape the data to have years as the index and categories as columns
pivot_df = aggregated_data.pivot(index='Year', columns='Category', values='Count').fillna(0)

# Create the stacked bar chart
fig = px.bar(pivot_df, 
             barmode='stack', 
             title='Category Count by Year',
             labels={'value':'Count', 'variable':'Category'},
             color_discrete_sequence=colors)

# Customize the layout
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Count',
    legend_title='Category',
    plot_bgcolor='white',
    font=dict(size=12)
)

# Show the figure
st.plotly_chart(fig)

################################### RESULTS DONUT CHART #################################################################################

# st.markdown("<h1 style='text-align: center;'>Results of Recommendation</h1>", unsafe_allow_html=True)


# # Now count the occurrences of each result in the filtered data
# result_counts = filtered_df['Result '].value_counts()

# # Assuming 'result_counts' contains the counts of each result
# labels = result_counts.index
# sizes = result_counts.values
# colors = plt.cm.tab20c.colors  # Using a colormap for variety

# fig, ax = plt.subplots()
# #ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4, edgecolor='w'))

# #explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)  # explode the 2nd slice (Sexual Assault)
# explode = [0] * len(labels)  # No slice is exploded, but can be customized as needed.

# # Set chart size
# plt.figure(figsize=(12, 8))
# wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.25, edgecolor= 'black'))

# # Here's where you can set the size of the labels.
# plt.setp(texts, size=19) # Set the property 'size' for label texts to 12, or any other value you prefer
# plt.setp(autotexts, size=19) # Set the property 'size' for autotexts (the percentage labels) to 12 and make them bold

# # Adjust subplot parameters to move the pie chart
# plt.subplots_adjust(top=1.5, bottom=0.1)  # Adjust the bottom parameter to move the chart down

# plt.axis('equal')

# # Display the donut chart in Streamlit
# st.pyplot(plt)
##################################### RESULTS DONUT CHART 2 ####################################################################################

st.markdown("<h1 style='text-align: center;'>Results of Recommendation</h1>", unsafe_allow_html=True)

# Assuming 'result_counts' contains the counts of each result
result_counts = filtered_df['Result '].value_counts()

# Create a donut chart with a larger hole
fig = px.pie(result_counts, values=result_counts.values, names=result_counts.index, hole=0.5)  # Increase hole size

# Customizing the chart
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(
    autosize=False,
    width=800,  # Width of the chart
    height=600  # Height of the chart
)

# Display the donut chart in Streamlit
st.plotly_chart(fig)

#################################### LINE CHART OF THEMES OVER THE YEARS #######################################################################

st.markdown("<h1 style='text-align: center;'>Themes Over All Years</h1>", unsafe_allow_html=True)

# # Count the occurrences of each category per year
# category_counts = df.groupby(['Year', 'Category']).size().reset_index(name='Counts')

# # Pivot the results to get years as index and categories as columns
# category_counts_pivot = category_counts.pivot(index='Year', columns='Category', values='Counts').fillna(0)

# # Plotting
# # Plotting with a specified figure size (width, height)
# fig, ax = plt.subplots(figsize=(14, 6))  # Increase the width for a longer chart


# # Plot each category count as a line
# for category in category_counts_pivot.columns:
#     ax.plot(category_counts_pivot.index, category_counts_pivot[category], label=category)

# # Formatting
# #ax.figure(figsize=(12, 10))
# ax.set_xlabel('Year')
# ax.set_ylabel('Count')
# ax.legend()

# # Show the plot in Streamlit
# st.pyplot(fig)

################################# LINE CHART 2 ############################################################
import plotly.express as px

# Count the occurrences of each category per year
category_counts = df.groupby(['Year', 'Category']).size().reset_index(name='Counts')

# Pivot the results to get years as index and categories as columns
category_counts_pivot = category_counts.pivot(index='Year', columns='Category', values='Counts').fillna(0)

# Melt the DataFrame for Plotly
category_counts_melted = category_counts_pivot.reset_index().melt(id_vars=['Year'], var_name='Category', value_name='Counts')

# Create a line chart using Plotly Express
fig = px.line(category_counts_melted, x='Year', y='Counts', color='Category')

# Update layout for better readability and customization
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Count',
    hovermode='x unified',
    autosize=False,
    width=800,  # Width of the chart
    height=600,  # Height of the chart
    legend_title='Category'
)

# Update traces for better visualization, if necessary
#for trace in fig.data:
 #   trace.name = trace.name.split('=')[1]  # Updating trace names to be more readable

# Display the plot in Streamlit
st.plotly_chart(fig)

###############################

# import plotly.express as px

# # # Count the occurrences of each category per year
# category_counts = df.groupby(['Year', 'Category']).size().reset_index(name='Counts')

# # # Pivot the results to get years as index and categories as columns
# category_counts_pivot = category_counts.pivot(index='Year', columns='Category', values='Counts').fillna(0)


# # Create a line chart using Plotly Express
# fig = px.line(category_counts_pivot, x=category_counts_pivot.index, y=category_counts_pivot.columns, title='Category Counts per Year')

# # Update layout for better readability and customization
# fig.update_layout(
#     xaxis_title='Year',
#     yaxis_title='Count',
#     hovermode= 'x unified',
#     autosize=False,
#     width=800,  # Width of the chart
#     height=600,  # Height of the chart
#     legend_title='Category'
# )

# # Formatting
# #ax.figure(figsize=(12, 10))
# # ax.set_xlabel('Year')
# # ax.set_ylabel('Count')
# # ax.legend()

# # Show the plot in Streamlit
# st.pyplot(fig)