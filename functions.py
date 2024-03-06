FILEPATH = "files/todos.txt"


def set_file(items: list, filepath: str = FILEPATH):
    """Writes a List to a text file."""
    with open(filepath, "w") as file:
        file.writelines(items)


def get_file(filepath: str = FILEPATH):
    """Read a text file and returns it as a list"""
    with open(filepath, 'r') as file:
        items = file.readlines()
    return items
