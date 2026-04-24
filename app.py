import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="My Streamlit App", layout="centered")

# App Header
st.title("🚀 Streamlit Deployment Test")
st.write("If you see this, your app is running successfully!")

# Add a simple interactive element
name = st.text_input("Enter your name:", "Guest")
st.success(f"Welcome, {name}!")

# Add a data visualization example
st.subheader("Random Data Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# Sidebar info
st.sidebar.header("About")
st.sidebar.info("This is a basic Streamlit app template for deployment testing.")
