



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

def load_data():
    data = pd.read_excel('/workspaces/VA-Recommendation-Analysis-App/ACWV Recommendations with Categories and Similarity Groups.xlsx')

    # Select a subset of columns if the DataFrame is very wide
    columns_to_display = ['ChainID', 'Year', 'ID', 'Category', 'Recommendation']
    data = data[columns_to_display]
    

    # Filter out rows with nan chain ID
    data = data.dropna(subset=['ChainID'])

    # Sort the DataFrame by the chain ID in descending order
    data = data.sort_values(by='ChainID', ascending=True)

    return data
data = load_data()
st.table(data)


############################################## OLD STUFF ###########################################################################

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
