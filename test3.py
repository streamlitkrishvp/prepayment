import streamlit as st
st.header("Streamlit Machine Learning App")
EMI_amount = st.number_input(label='EMI amount per month', min_value=None, max_value=None, value=100, step=100)
