
import streamlit as st
import importlib
import sys
import os

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

# Create the page selection box in the sidebar
page_selection = st.sidebar.selectbox("Navigate to:", pages)
st.session_state['current_page'] = page_selection

# Home page content
if st.session_state['current_page'] == 'Home':
    st.title("Welcome to My App")
    st.write("This is the Home page.")
    # Add any other content and functionality you want on the Home page here

# Dynamic import and display of other pages
else:
    page_module = importlib.import_module(f'pages.{page_selection}')
    page_module.show()

