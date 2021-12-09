from pathlib import Path

path_to_file = Path("../../docs/day1/data.dat")

with open(path_to_file, 'r', encoding='utf-8') as file:
    data = file.read().splitlines()

def sum_triplet(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)
    return x + y + z

prev_sum = sum_triplet(data[0], data[1], data[2])
greater_counter = 0
for triplet in zip(data[1:-2], data[2:-1], data[3:]):
    this_sum = sum_triplet(*triplet)
    if this_sum > prev_sum:
        greater_counter += 1

    prev_sum = this_sum

print("Triplet sums larger than previous:", greater_counter)
