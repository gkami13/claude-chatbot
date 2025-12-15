import streamlit as st
st.title("My First Streamlit App")
st.write("Hello! This is a web application built with Python.")
name = st.text_input("What's your name?")
if name:
    st.write(f"Welcome, {name}!")