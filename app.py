import streamlit as st  # Import the Streamlit library

# Set the title of the app
st.title("Job Application Tracker")

# Add a welcome message
st.write("Welcome! This app helps you track your job applications easily.")

# Add a button to test
if st.button("Click me!"):
    st.success("Button clicked! The app is working!")

