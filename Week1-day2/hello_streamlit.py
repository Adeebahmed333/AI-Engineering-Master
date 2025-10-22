import streamlit as st

# Page config
st.set_page_config(
    page_title="My First Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 Hello Streamlit!")

# Text
st.write("This is my first web app!")

# Input
name = st.text_input("What's your name?")

# Button
if st.button("Greet Me"):
    st.success(f"Hello, {name}! 👋")

# Columns
col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.write("Some content here")

with col2:
    st.header("Column 2")
    st.write("More content here")

# Sidebar
st.sidebar.title("Settings")
age = st.sidebar.slider("Your age", 0, 100, 25)
st.sidebar.write(f"You are {age} years old")