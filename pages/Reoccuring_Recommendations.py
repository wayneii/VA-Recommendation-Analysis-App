



import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')


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

st.title('')

st.caption("Here you will find a list of reoccuring recommendations that have not yet reached a 'concur'. In order to identify recommendations that were similar to ones from previous years, recommendations were grouped, given a similarity score, and ordered by similarity. Here, we are only showing recommendations with a similarity score of 86 percent or higher. Click on a group to reveal the recommendations contained within and click on another to open a new group and close out the previous group.")



############################################## OLD STUFF ###########################################################################

import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_excel('ACWV Recommendations with Categories and Similarity Groups.xlsx')

    # Select a subset of columns if the DataFrame is very wide
    columns_to_display = ['ChainID', 'Year', 'ID', 'Category', 'Recommendation', 'Result ']
    data = data[columns_to_display]
    # Convert 'ChainID' to numeric, coercing errors to NaN
    data['ChainID'] = pd.to_numeric(data['ChainID'], errors='coerce')
    data = data.dropna(subset=['ChainID'])
    data = data.sort_values(by=['Year', 'ChainID'], ascending=[False, True])
    return data

data = load_data()

######################################### SIDEBAR FILTER #################################################################
# columns = st.columns((1,1))

# results = data['Result '].unique()

# # Initialize selected_categories with all categories by default
# results_list = results.tolist()


# selected_result = st.sidebar.checkbox(
# for result in results_list:

#     )
#     st.title("")


#################################### DISPLAY BUTTONS #####################################################################
# Iterate through each unique ChainID
for chain_id in data['ChainID'].unique():
    # Filter data for the selected ChainID
    chain_data = data[data['ChainID'] == chain_id]

    # Change the data type of ChainID to integer
    chain_data['ChainID'] = chain_data['ChainID'].astype(int)
    #chain_data = chain_data.style.format({'ChainID': '{:.0f}'}) 
 
    # Calculate the number of recommendations and the range of years
    num_recommendations = len(chain_data)
    year_range = f"{chain_data['Year'].min()} - {chain_data['Year'].max()}"

    # Extract unique categories and format them into a string
    unique_categories = chain_data['Category'].unique()
    categories_str = ', '.join(sorted(unique_categories))

    # Extract the result of the last recommendation
    last_recommendation_result = chain_data['Result '].iloc[0]

    # Convert to integer
    chainID = str(chain_id)

    # Create a button for each ChainID with additional information
    button_label = f'''
    Group: {chain_id} 
    {num_recommendations} Recommendations
    Years: {year_range} 
    Related to: {categories_str}
    Last Recommendation Result: {last_recommendation_result}
    '''
    if st.button(button_label):
        # Display the recommendations for the selected ChainID
        st.write(f"Recommendations for Group {chain_id}")
        chain_data.reset_index(drop=True)
        chain_data.index = pd.RangeIndex(start=1, stop=len(chain_data) + 1, step=1)
        st.table(chain_data[['Year', 'ID', 'Category', 'Recommendation', 'Result ']])

