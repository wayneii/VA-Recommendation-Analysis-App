
# Load Packages
import streamlit as st

# Another change 48

# Text to display
st.title('Hello, Streamlit!')
st.write('This is a simple Streamlit app. Edit')

#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import modules
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt


# In[2]:


# upload data
data = pd.read_excel("ACWV Recommendation.xlsx")
#data = pd.DataFrame(data)
#data.head()


# In[3]:


data.dropna(subset=['Recommendation'], inplace=True)

# Add a slider to the sidebar:
year_select = st.sidebar.slider(
    'Select a range of years',
    1996, 2020, (2004, 2010)
)

year_min, year_max = year_select


data = data[(data['Year'] >= year_min) & (data['Year'] <= year_max)]


data = pd.DataFrame({"Recommendation":" ".join(data["Recommendation"])},
                           index=[0])




def topN_words(data, ngram_min = 1, ngram_max = 1, n_results = 10):

    # Instantiates vectorizer
    v = CountVectorizer(stop_words="english",
                    ngram_range=(ngram_min, ngram_max))

    # Vectorizes text
    dtm = v.fit_transform(data["Recommendation"])

    # Creates dataframe
    dtm_df = pd.DataFrame(dtm.toarray(),
                     columns=v.get_feature_names_out())

    # transpose
    dtm_df = dtm_df.T
    dtm_df.reset_index(inplace=True)
    dtm_df.columns = ['Text', 'Frequency']

    df_sorted = dtm_df.sort_values(by="Frequency", ascending=False).head(n_results)

    base =   alt.Chart(df_sorted).encode(
        x=alt.X('Frequency'),
        y=alt.Y('Text', axis=alt.Axis(labelLimit=500), title = " ").sort('-x'),
        text='Frequency'
    )
    plot = base.mark_bar() + base.mark_text(align='left', dx=2)


    return plot


# In[17]:
st.write("Here are the top recurring phrases and their frequencies for the selected years:")
st.write(year_select)

plot = topN_words(data,5,5,10)
st.altair_chart(plot, use_container_width=True)



