from pathlib import Path
from os import chdir


def main():
    """Main function."""
    path_to_file = Path("../../docs/day2/data.dat")

    with open(path_to_file, "r") as file:
        lines = file.read().splitlines()

    print(lines)


if __name__ == "__main__":
    exec_filepath = str(Path(__file__))
    exec_dir = "/".join(exec_filepath.split("/")[:-1])

    chdir(exec_dir)

    main()
