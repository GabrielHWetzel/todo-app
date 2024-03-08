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
        # Button actions
        case "Add":
            if not values['todo'].strip() == "":
                todos.append(values['todo'].strip().capitalize())

                functions.set_file(todos)
                window["todos"].update(values=todos)
        case "Edit":
            try:
                index = todos.index(values['todos'][0])
                todos[index] = values['todo']

                functions.set_file(todos)
                window["todos"].update(values=todos)
            except IndexError:
                continue
        # Other actions
        case "todos":
            window['todo'].update(value=values['todos'][0])
        # Quit
        case Sg.WINDOW_CLOSED:
            break

window.close()
