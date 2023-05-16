import streamlit as st 

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)
st.sidemar.title("This is written inside the sidebar")
