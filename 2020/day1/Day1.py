"""
Solves for Day 1 advent of code.
"""
import numpy as np
from itertools import combinations

# Reads in data into a numpy array
with open("data", 'r') as f:
    numbers = np.array(list(map(int, f.readlines())))

# Problem 1
# Loop over the array once
# Apply a vector sum mask for the unique 2020 sum
for i in range(len(numbers)):
    x = numbers[i]
    test = np.delete(numbers, i)
    y = test[test + x == 2020]
    if y.size > 0:
        print(x * y)

# Problem 2: Solution 1
# Loop over the truncated array once for each x in the array
# break out of the double loop
# use a boolean to break out of a double loop
calculate = True
i = 0
while i < len(numbers) and calculate is True:
    x = numbers[i]
    test = np.delete(numbers, i)
    i += 1
    for j in range(len(test)):
        y = test[j]
        test2 = np.delete(test, j)
        z = test2[test2 + x + y == 2020]
        if z.size > 0:
            z = int(z)
            print(f"Numbers: {x}, {y}, {z}")
            print(f"Sum: {x + y + z}")
            print(f"Product: {x * y * z}")
            calculate = False
            break

# Problem 2: Solution 2
# use itertools to break out of single loop
for x, y, z in combinations(numbers, 3):
    if x + y + z == 2020:
        print(f"Numbers: {x}, {y}, {z}")
        print(f"Sum: {x + y + z}")
        print(f"Product: {x * y * z}")
        break