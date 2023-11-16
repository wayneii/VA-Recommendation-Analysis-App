



import streamlit as st
import pandas as pd


##################################################### BANNER  #####################################################################

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
  <h1 style="color:white;">Reoccuring Recommendations</h1>
</div>
""", unsafe_allow_html=True)

######################################### DISPLAY SIMILAR RECOMMENDATIONS DF #######################################################



############################################## OLD STUFF ###########################################################################

import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_excel('ACWV Recommendations with Categories and Similarity Groups.xlsx')

    # Select a subset of columns if the DataFrame is very wide
    columns_to_display = ['ChainID', 'Year', 'ID', 'Category', 'Recommendation']
    data = data[columns_to_display]
    # Convert 'ChainID' to numeric, coercing errors to NaN
    data['ChainID'] = pd.to_numeric(data['ChainID'], errors='coerce')
    data = data.dropna(subset=['ChainID'])
    data = data.sort_values(by=['Year', 'ChainID'], ascending=[False, True])
    return data

data = load_data()

# Iterate through each unique ChainID
for chain_id in data['ChainID'].unique():
    # Filter data for the selected ChainID
    chain_data = data[data['ChainID'] == chain_id]

    # Calculate the number of recommendations and the range of years
    num_recommendations = len(chain_data)
    year_range = f"{chain_data['Year'].min()} - {chain_data['Year'].max()}"

    # Extract unique categories and format them into a string
    unique_categories = chain_data['Category'].unique()
    categories_str = ', '.join(sorted(unique_categories))

    # Create a button for each ChainID with additional information
    button_label = f'''
    Group: {chain_id} 
    {num_recommendations} Recommendations
    Years: {year_range} 
    Related to: {categories_str}
    '''
    if st.button(button_label):
        # Display the recommendations for the selected ChainID
        st.write(f"Recommendations for ChainID {chain_id}:")
        st.table(chain_data[['Year', 'ID', 'Category', 'Recommendation']])

