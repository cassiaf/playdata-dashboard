import streamlit as st

st.title("PlayData Project Analyzer")
st.write("Upload your playdata .sb3 file to analyze your project.")

label = "Upload your file"
st.file_uploader(label, type="sb3", accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")