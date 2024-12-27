def read_data(path_to_file):
    """Read data from file."""
    with open(path_to_file, "r") as file:
        yield file.read()


def method1():
    """Use the following steps:
    1. Read the file
    2. Create 2 lists by appending
    3. Sort the 2 lists
    4. Find the difference between each value of the sorted lists
    5. Print the total absolute differences
    """
    file_contents = next(read_data("../../docs/day01/day01.dat")).split("\n")
    left_items = []
    right_items = []
    for line in file_contents:
        line_items = line.split(" ")
        left_item, right_item = line_items[0], line_items[-1]
        if left_item and right_item:
            left_items.append(int(left_item))
            right_items.append(int(right_item))

    left_items = sorted(left_items)
    right_items = sorted(right_items)
    pairs = zip(left_items, right_items)

    total = 0

    for pair in pairs:
        left, right = pair
        total += abs(left - right)

    print(total)


if __name__ == "__main__":
    method1()
