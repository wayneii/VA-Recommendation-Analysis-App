
import streamlit as st
import importlib
import sys
import os

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
  <h1 style="color:white;">Overview of VA Recommendations</h1>
</div>
""", unsafe_allow_html=True)

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

#### THIS IS WHERE WE PUT THE CODE TO CHANGE THE SIDEBAR
#### e.g. filter, year selection, or 
# Create the page selection box in the sidebar
#page_selection = st.sidebar.selectbox("Navigate to:", pages)
#st.session_state['current_page'] = page_selection

# Home page content
#if st.session_state['current_page'] == 'Home':
    #st.title("Welcome to My App")
    #st.write("This is the Home page.")
    # Add any other content and functionality you want on the Home page here

# Dynamic import and display of other pages
#else:
    #page_module = importlib.import_module(f'pages.{page_selection}')
    #page_module.show()


# Display of Themes
import streamlit as st
import matplotlib.pyplot as plt


st.title("Topic Distribution Pie Chart by Year")

# Dummy data: nested dictionary where the outer key is the year, and the inner dictionary contains topic sizes.
data = {
    2014: {'Healthcare Innovations': 10, 'Sexual Assault': 20, 'Homelessness': 25, 'Business Transformation': 10, 'Controversial Topics': 5, 'Data-Driven Outreach': 30},
    2016: {'Healthcare Innovations': 15, 'Sexual Assault': 35, 'Homelessness': 20, 'Business Transformation': 10, 'Controversial Topics': 10, 'Data-Driven Outreach': 10},
    2018: {'Healthcare Innovations': 20, 'Sexual Assault': 15, 'Homelessness': 25, 'Business Transformation': 20, 'Controversial Topics': 10, 'Data-Driven Outreach': 10},
    2020: {'Healthcare Innovations': 25, 'Sexual Assault': 30, 'Homelessness': 20, 'Business Transformation': 5,  'Controversial Topics': 10, 'Data-Driven Outreach': 10},
    2022: {'Healthcare Innovations': 30, 'Sexual Assault': 25, 'Homelessness': 15, 'Business Transformation': 15, 'Controversial Topics': 5,  'Data-Driven Outreach': 10},
}

# Sidebar: Year selection
selected_year = st.sidebar.slider('Select a year range', min_value=min(data.keys()), max_value=max(data.keys()), value=(min(data.keys()), max(data.keys())))

# Filter data based on selected years
filtered_data = {year: sizes for year, sizes in data.items() if year >= selected_year[0] and year <= selected_year[1]}

# Aggregate data across the selected years
aggregated_data = {}
for sizes in filtered_data.values():
    for topic, size in sizes.items():
        aggregated_data[topic] = aggregated_data.get(topic, 0) + size

labels = list(aggregated_data.keys())
sizes = list(aggregated_data.values())

# Pie chart settings
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'purple', 'orange']
explode = (0, 0.1, 0, 0, 0, 0)  # explode the 2nd slice (Sexual Assault)

plt.figure(figsize=(10, 6))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

# Display the pie chart
st.pyplot(plt)

