import streamlit as st
import functions

todos = functions.get_file()

st.title("List of to-dos")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")
