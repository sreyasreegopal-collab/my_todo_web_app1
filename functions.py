FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Reads the text file and returns a list of todos
    """
    with open(filepath , "r") as file_local:                  # with context manager
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):      # default arg are declared at the end after non-default arg
    """
    Writes todos items list to a text file
    """
    with open(filepath , "w") as file:
        file.writelines(todos_arg)

if  __name__ == "__main__":
    print("Helloooooo")
    print(get_todos())


