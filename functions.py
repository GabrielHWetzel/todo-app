FILEPATH = "files/todos.txt"


def get_file(filepath: str = FILEPATH):
    """Read a text file and returns it as a list without linebreaks"""
    with open(filepath, 'r') as file:
        items = file.readlines()
    for index, item in enumerate(items):
        items[index] = item.strip("\n")
    return items


def set_file(items: list, filepath: str = FILEPATH):
    """Writes a List to a text file with linebreaks."""
    # Local variable to not mess up the global todo for some reason
    new_items = []
    for item in items:
        new_items.append(item + "\n")
    with open(filepath, "w") as file:
        file.writelines(new_items)

