import streamlit as st
import functions as f

todos = f.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    f.write_todos(todos)
    st.session_state.new_todo = ""

st.title("My Todo App")
st.subheader("This is my first app")
st.text("Hope this is useful to check your activity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:    #Checking with True
        todos.pop(index)
        #todos.remove(todo)
        f.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = "", placeholder = "Add a new todo...",
              on_change =  add_todo, key = "new_todo")

print("Hello")


