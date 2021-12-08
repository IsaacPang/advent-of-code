from collections import deque

def binary_partition(instructions, target_list, upper, lower):
    """
    Applies binary partition recursively on a target_list for a given
    set of instructions, subjected to the upper and lower condition.
    Args:
        instructions (str): set of instructions
        target_list (list or range): target list for partitioning
        upper (str): instruction to return upper half of partition
        lower (str): instruction to return lower hafl of partition
    """
    if type(instructions) != deque:
        instructions = deque(instructions)

    if instructions and len(target_list) > 1:
        curr = instructions.popleft()
        half_index = len(target_list) // 2
        lower_half = target_list[:half_index]
        upper_half = target_list[half_index:]
        if curr == upper:
            return binary_partition(instructions, upper_half, upper, lower)
        elif curr == lower:
            return binary_partition(instructions, lower_half, upper, lower)
        else:
            return "Error in Instructions"
    else:
        return list(target_list)

def boarding_partition(boarding_pass):
    """
    Applies the binary partition twice to the entire boarding pass string.
    Note that the upper half for the row selection should be the B rows.
    Note that the upper half for the column selection should be the R cols.
    """
    rows = boarding_pass[:-3]
    cols = boarding_pass[-3:]
    row_nums = range(128)
    col_nums = range(8)
    target_row = binary_partition(rows, row_nums, 'B', 'F').pop()
    target_col = binary_partition(cols, col_nums, 'R', 'L').pop()
    seat_id = target_row * 8 + target_col
    return {"row": target_row, "col": target_col, "id": seat_id}

with open('data', 'r') as f:
    id_list = []
    for line in f.readlines():
        line = line.rstrip('\n')
        id_list.append(boarding_partition(line).get('id'))
    
    # Problem 1
    # Return max seat ID    
    print(max(id_list))

    # Problem 2
    # Return number in missing sequence.
    id_list = sorted(id_list)
    while id_list:
        curr = id_list.pop()
        if id_list[-1] != curr - 1:
            print(f"Missing ID (Your Seat): {curr - 1}")
            break