



import streamlit as st
import pandas as pd



#df = pd.read_excel('ACWV Recommendations with Categories and Similarity Groups.xlsx')

# Display the DataFrame
#data = load_data()
#st.table(df)



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

# def load_data():
#     data = pd.read_excel('/workspaces/VA-Recommendation-Analysis-App/ACWV Recommendations with Categories and Similarity Groups.xlsx')

#     # Select a subset of columns if the DataFrame is very wide
#     columns_to_display = ['ChainID', 'Year', 'ID', 'Category', 'Recommendation']
#     data = data[columns_to_display]
    

#     # Filter out rows with nan chain ID
#     data = data.dropna(subset=['ChainID'])

#     # Sort the DataFrame by the chain ID in descending order
#     data = data.sort_values(by='ChainID', ascending=True)

#     return data
# data = load_data()
# st.table(data)

############################################## Button ###############################################################################
# import streamlit as st
# import pandas as pd

# def load_data():
#     data = pd.read_excel('/workspaces/VA-Recommendation-Analysis-App/ACWV Recommendations with Categories and Similarity Groups.xlsx')
#     columns_to_display = ['ChainID', 'Year', 'ID', 'Category', 'Recommendation']
#     data = data[columns_to_display]
#     data = data.dropna(subset=['ChainID'])
#     data = data.sort_values(by='ChainID', ascending=True)
#     return data

# data = load_data()

# # Iterate through each unique ChainID
# for chain_id in data['ChainID'].unique():
#     # Create a button for each ChainID
#     if st.button(f'Show Recommendations for ChainID {chain_id}'):
#         # Filter data for the selected ChainID
#         filtered_data = data[data['ChainID'] == chain_id]
#         # Display the recommendations for the selected ChainID
#         st.write(f"Recommendations for ChainID {chain_id}:")
#         st.table(filtered_data[['Year', 'ID', 'Category', 'Recommendation']])





############################################## OLD STUFF ###########################################################################

import streamlit as st
import pandas as pd

def load_data():
    data = pd.read_excel('/workspaces/VA-Recommendation-Analysis-App/ACWV Recommendations with Categories and Similarity Groups.xlsx')

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




######################################################################################################
# Sample data
# data = {
#     'ID': [1, 2, 3, 4, 5, 6, 7],
#     'Year': [1996, 2000, 2005, 2010, 2015, 2020, 2022],
#     'Short_Recommendation': ['Improve Security', 'Enhance Security', 'Boost Security', 'Upgrade Security', 'Strengthen Security', 'Improve Security Again', 'Strengthen Security Again'],
#     'Full_Recommendation': ['Full text for Improve Security', 'Full text for Enhance Security', 'Full text for Boost Security', 'Full text for Upgrade Security', 'Full text for Strengthen Security', 'Full text for Improve Security Again', 'Full text for Strengthen Security Again'],
#     'Similar_to': ['None', '1', '2', '3', '4', '5', '6'],
#     'Status': ['Not Concurred', 'Not Concurred', 'Concurred', 'Not Concurred', 'Concurred', 'Not Concurred', 'Concurred'],
#     'Category': ['Security', 'Security', 'Security', 'IT', 'IT', 'HR', 'HR']
# }
# df = pd.DataFrame(data)

# st.title('Recommendations on the Table')

# # Create a category filter with counts
# categories = df['Category'].unique()
# category_counts = df[df['Status'] == 'Not Concurred'].groupby('Category').size()
# category_options = [f"{category} ({category_counts.get(category, 0)})" for category in categories]

# # Use multiselect instead of dropdown
# selected_categories = st.sidebar.multiselect('Filter by Category:', category_options)
# selected_categories = [cat.split(' ')[0] for cat in selected_categories]

# # Filter the DataFrame based on the status 'Not Concurred' and selected categories
# if selected_categories:
#     df_filtered = df[(df['Status'] == 'Not Concurred') & (df['Category'].isin(selected_categories))]
# else:
#     df_filtered = df[df['Status'] == 'Not Concurred']

# # Loop through filtered DataFrame and display interactive elements
# for index, row in df_filtered.iterrows():
#     button_label = f"Recommendation {row['ID']} from {row['Year']} (Status: {row['Status']})"
#     if st.button(button_label):
#         st.write(f"**Full Recommendation**: {row['Full_Recommendation']}")
        
#         similar_to_ids = row['Similar_to'].split(',')
#         similar_recs = df[df['ID'].astype(str).isin(similar_to_ids)]
        
#         st.write("**Similar to the following recommendations:**")
#         for sim_index, sim_row in similar_recs.iterrows():
#             st.write(f"Recommendation {sim_row['ID']} from {sim_row['Year']}: {sim_row['Full_Recommendation']}")
