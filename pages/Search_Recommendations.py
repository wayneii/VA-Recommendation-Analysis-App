import streamlit as st
st.set_page_config(layout='wide')


def show():
    st.write("You're viewing the Search page content!")
    # Add your content and functionality for the "About" page here

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import openpyxl  # required for Excel file handling

# Function to compute cosine similarity
def find_similar_recommendations(query, tfidf_vectorizer, tfidf_matrix, features, df, top_n=8):
    query_vect = tfidf_vectorizer.transform([query])
    similarity = cosine_similarity(query_vect, tfidf_matrix)
    top_indices = similarity[0].argsort()[-top_n:][::-1]
    selected_columns = ['Year','Category','Result ' , 'Recommendation']
    results_df = df.iloc[top_indices][selected_columns]
    
    # Add cosine similarity scores to the results DataFrame
    results_df['Similarity_Score'] = similarity[0][top_indices]
    return results_df.reset_index(drop=True)

# Load dataset
#@st.cache
def load_data(filename):
    df = pd.read_excel(filename)
    df['Year'] = df['Year'].astype(str)
    return df
# Streamlit App
def main():
    st.title('Recommendation Finder')

    # Load Excel file
    df = load_data('ACWV Recommendations with Categories and Similarity Groups.xlsx')  # Replace with your Excel file name
    recommendations = df['Recommendation']  # Replace with your column name

    # Vectorize recommendations
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(recommendations)

    # User input
    query = st.text_input('Enter your recommendation query:')

    if st.button('Search'):
        results = find_similar_recommendations(query, tfidf_vectorizer, tfidf_matrix, recommendations, df)
        results.index = pd.RangeIndex(start=1, stop=len(results) + 1, step=1)
        st.write(results)

if __name__ == '__main__':
    main()
