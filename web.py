import streamlit as st
import functions

todos = functions.get_file()


def add_todo():
    todos.append(st.session_state["new_todo"].capitalize())
    functions.set_file(todos)


st.title("List of to-dos")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.set_file(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")