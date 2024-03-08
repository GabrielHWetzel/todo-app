FILEPATH = "files/"
FILENAME = "todos.txt"


def get_file(filename: str = FILENAME, filepath: str = FILEPATH):
    """Read a text file and returns it as a list without linebreaks"""
    with open(filepath+filename, 'r') as file:
        items = file.readlines()
    for index, item in enumerate(items):
        items[index] = item.strip("\n")
    return items


def set_file(items: list, filename: str = FILENAME, filepath: str = FILEPATH):
    """Writes a List to a text file with linebreaks."""
    # Local variable to not mess up the global items input for some reason. Also removes the need to enumerate.
    new_items = []
    for item in items:
        new_items.append(item + "\n")
    with open(filepath+filename, "w") as file:
        file.writelines(new_items)
