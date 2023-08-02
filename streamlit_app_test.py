import streamlit as st

# Create application title and file uploader widget.
st.title("OpenCV Streamlit demo")
st.header("header")

image = st.file_uploader("Upload an image file")
#st.image(image)
st.text("This is text")
selected_value = st.selectbox("Select Box",["None","Filter","filter 2"])
st.write(selected_value)

checkbox_value = st.checkbox("Apply filter")
st.write(checkbox_value)