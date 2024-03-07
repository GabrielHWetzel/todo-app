import functions
import PySimpleGUI as Sg

todos = functions.get_file()

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter to-do",
                         key="todo")
list_box = Sg.Listbox(values=todos,
                      key='todos',
                      enable_events=True,
                      size=(45, 10))

# Buttons
add_button = Sg.Button("Add")
edit_button = Sg.Button("Edit")

window = Sg.Window('To-do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Helvetica', 10))

while True:
    event, values = window.read()
    print(event, values)
    match event:
        # Button Functions
        case "Add":
            if not values['todo'] == "":
                todos.append(values['todo'] + "\n")
                functions.set_file(todos)
                window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            functions.set_file(todos)
            window["todos"].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        # Quit
        case Sg.WINDOW_CLOSED:
            break

window.close()
