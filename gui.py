import functions
import PySimpleGUI as sg
import os
# import time

if not os.path.exists("todos.txt"):
    functions.set_file([])

todos = functions.get_file()

sg.theme('SystemDefaultForReal')

# clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do",
                         key="todo",
                         expand_x=True)
list_box = sg.Listbox(values=todos,
                      key='todos',
                      enable_events=True,
                      size=(45, 10))
input_column = sg.Column([[input_box],
                          [list_box]])

# Buttons
add_button = sg.Button("Add", expand_x=True, mouseover_colors="LightBlue")
edit_button = sg.Button("Edit", expand_x=True, mouseover_colors="LightBlue")
complete_button = sg.Button("Complete", expand_x=True, mouseover_colors="LightBlue")
exit_button = sg.Button("Exit", expand_x=True, mouseover_colors="LightBlue")

button_column = sg.Column([[add_button],
                           [edit_button],
                           [complete_button],
                           [exit_button]],
                          vertical_alignment="top")

window = sg.Window('To-do App',
                   layout=[[label],
                           [input_column, button_column],
                           [sg.VPush()]],
                   font=('Helvetica', 10))

while True:
    event, values = window.read()
    # window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event, values)
    match event:
        # Button actions
        case "Add":
            if not values['todo'].strip() == "":
                todos.append(values['todo'].strip().capitalize())

                functions.set_file(todos)
                window["todos"].update(values=todos)
                window['todo'].update('')
        case "Edit":
            try:
                index = todos.index(values['todos'][0])
                todos[index] = values['todo'].capitalize()

                functions.set_file(todos)
                window["todos"].update(values=todos)
                window['todo'].update('')
            except IndexError:
                sg.Popup("Please select an item first", font=('Helvetica', 10))
                continue
        case "Complete":
            try:
                todos.remove(values['todos'][0])

                functions.set_file(todos)
                window["todos"].update(values=todos)
                window['todo'].update('')
            except IndexError:
                sg.Popup("Please select an item first", font=('Helvetica', 10))
                continue
        # Other actions
        case "todos":
            window['todo'].update(value=values['todos'][0])
        # Quit
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
