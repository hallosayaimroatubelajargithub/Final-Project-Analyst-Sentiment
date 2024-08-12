import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="images/home.png",
)
st.sidebar.success("Select a page above.")

# Showing images
st.image('images/gambar.png', use_column_width=True)

st.markdown('<div style="text-align: center; font-size: 30px; font-weight: bold; padding-top: 20px">\
           Welcome to the Sentiment Analysis App for Google Play Store Reviews</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; font-size: 25px; padding-bottom: 20px">Final Project FGA UDINUS 2024</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify; font-size: 20px">Sentiment Analysis App for Google Play Store Reviews\
            This sentiment analysis app is designed to provide deeper insights into app reviews on the Google Play Store.\
            Its purpose is to measure and display the percentage of reviews categorized as positive, negative, and neutral, allowing users to clearly and comprehensively understand the general response to an app.</div>', unsafe_allow_html=True)