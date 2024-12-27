def read_data(path_to_file):
    """Read data from file."""
    with open(path_to_file, "r") as file:
        yield file.read()
