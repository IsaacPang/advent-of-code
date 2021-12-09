from pathlib import Path

path_to_file = Path("../../docs/day1/data.dat")

with open(path_to_file, 'r') as file:
    ref_data = next(file).strip('\n')
    num_data = 1
    greater_counter = 0
    for data_point in file:
        data_point = data_point.strip('\n')
        if isinstance(data_point, str) and not data_point:
            continue

        num_data += 1
        if int(data_point) > int(ref_data):
            greater_counter += 1
        ref_data = data_point

    print('Measurements that are larger than the previous:', greater_counter)
    print('Data in file: ', num_data)
