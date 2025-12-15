import streamlit as st

st.title("Session State Demo")

#Initialize session state variables if it does not exist
if "counter" not in st.session_state:
    st.session_state.counter = 0

#Display current count
st.write(f"Current count: {st.session_state.counter}")

#button to increment
if st.button("Add 1"):
    st.session_state.counter += 1
    st.rerun() # Force a rerun to show new value


