import streamlit as st

st.title("Streamlit Components Demo")

#Text elements
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is plain text")
st.markdown("This is **bold** text with *markdown*")

#Divider
st.divider()

#Input widgets
username = st.text_input("Enter your name:")
user_age = st.number_input("Enter your age:", min_value=0, max_value=120, value=25)
user_color = st.selectbox("Pick a color:", ["Red", "Green", "Blue"])

# Button
if st.button("Submit"):
    st.success(f"Hello {username}, age {user_age}, who likes {user_color}!")

# Divider
st.divider()

#Columns
col1, col2 = st.columns(2)

with col1:
    st.write("This is column 1")
    st.info("Info message")

with col2:
    st.write("This is column 2")
    st.warning("Warning message")

#Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("Content in the sidebar stays on the left")