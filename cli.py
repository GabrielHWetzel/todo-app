import functions

while True:

    user_action = input("Type add, show, edit, complete, or exit: ").strip()
    command = user_action.split()[0].lower()
    todo = user_action.removeprefix(command).strip().capitalize()

    match command:
        case 'add':
            todos = functions.get_file()
            if not todo:
                todo = input("Enter a todo to add: ").strip().capitalize()

            todos.append(todo)
            functions.set_file(todos)

        case 'show':
            todos = functions.get_file()

            # No args. Shows entire List
            if not todo:
                for index, item in enumerate(todos):
                    print(f"{index + 1}-{item}")

            # Searches items to Show, int or string
            else:
                try:
                    index = int(todo) - 1
                    if index == -1:
                        index = len(todos) - 1
                    print(f"{index + 1}-{todos[index]}")
                except (ValueError, IndexError):
                    exists = False
                    for index, item in enumerate(todos):
                        if item == todo:
                            print(f"{index + 1}-{item}")
                            exists = True
                    if not exists:
                        print("Todo doesn't exist.")

        case 'edit':
            todos = functions.get_file()
            if not todo:
                todo = input("Enter a todo to edit: ").strip().capitalize()
            try:
                index = int(todo) - 1
                if index == -1:
                    index = len(todos)-1
                print(f"Editing: {index+1}-{todos[index]}")
                todos[index] = input("Enter new todo: ").capitalize()
                functions.set_file(todos)
            except (ValueError, IndexError):
                try:
                    index = todos.index(todo)
                    print(f"Editing: {index+1}-{todos[index]}")
                    todos[index] = input("Enter new todo: ").capitalize()
                    functions.set_file(todos)
                except ValueError:
                    print("Todo doesn't exist.")

        case 'complete':
            todos = functions.get_file()
            if not todo:
                todo = input("Enter a todo to complete: ").strip().capitalize()

            try:
                index = int(todo) - 1
                if index == -1:
                    index = len(todos)-1
                print(f"Completed: {index+1}-{todos.pop(index)}")
                functions.set_file(todos)
            except (ValueError, IndexError):
                try:
                    index = todos.index(todo)
                    print(f"Completed: {index+1}-{todos.pop(index)}")
                    functions.set_file(todos)
                except ValueError:
                    print("Todo doesn't exist.")

        case 'exit':
            print("Bye!")
            break

        case _:
            print("Unknown command")
