import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter to-do", key="todo")
add_button = Sg.Button("Add")

window = Sg.Window('To-do App',
                   layout=[[label],
                           [input_box, add_button]],
                   font=('Helvetica', 10))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_file()
            todos.append(values['todo'] + "\n")
            functions.set_file(todos)

        case Sg.WINDOW_CLOSED:
            break
window.close()
