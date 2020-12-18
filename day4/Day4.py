from collections import defaultdict as dd
from collections import Counter

# Problem 1
# create a default dictionary for all the passport batches
# append each consecutive non-empty line to each list
batches = dd(list)
counter = 1
batch_name = 'batch' + str(counter)

with open('data', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        if line:
            batches[batch_name].append(line)
        else:
            counter += 1
            batch_name = 'batch' + str(counter)

valid_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']
valid_passports = 0

for batch in batches.keys():
    fields = [item.split(':')[0] for item in ' '.join(batches[batch]).split(' ')]
    field_counter = Counter(fields)
    field_counts = 0
    for field in valid_fields:
        if field == 'cid':
            field_counts += 1
        elif field_counter.get(field):
            field_counts += 1
    
    if field_counts == len(valid_fields):
        valid_passports += 1

print(f"Total Passports = {len(batches.keys())}")
print(f"Valid Passports (Problem 1) = {valid_passports}")

# Problem 2
# More intricate and each condition has its own details
# simpler to fit in a try except clause
# since some int() funcs may not work on all string reps.
valid_passports = 0
for batch in batches.keys():
    fields = {item.split(':')[0]: item.split(':')[1] for item in ' '.join(
                batches[batch]).split(' ')}
    
    # byr condition
    byr = fields.get('byr')
    try:
        c1 = all([
            bool(byr),
            len(byr) == 4,
            byr.isdigit(),
            1920 <= int(byr) <= 2002
        ])
    except:
        c1 = False
    
    # iyr condition
    iyr = fields.get('iyr')
    try:
        c2 = all([
            bool(iyr),
            len(iyr) == 4,
            iyr.isdigit(),
            2010 <= int(iyr) <= 2020
        ])
    except:
        c2 = False

    # eyr condition
    eyr = fields.get('eyr')
    try:
        c3 = all([
            bool(eyr),
            len(eyr) == 4,
            eyr.isdigit(),
            2020 <= int(eyr) <= 2030
        ])
    except:
        c3 = False
    
    # hgt condition
    hgt = fields.get('hgt')
    try:
        c4 = all([
            bool(hgt),
            any([
                hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193,
                hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76,
            ])
        ])
    except:
        c4 = False

    # hcl condition
    hcl = fields.get('hcl')
    try:
        c5 = all([
            bool(hcl),
            hcl[0] == '#',
            hcl[1:].isalnum()
        ])
    except:
        c5 = False
    
    # ecl condition
    ecl = fields.get('ecl')
    try:
        c6 = all([
            bool(ecl),
            ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        ])
    except:
        c6 = False

    # pid condition
    pid = fields.get('pid')
    try:
        c7 = all([
            bool(pid),
            len(pid) == 9,
            pid.isdigit()
        ])
    except:
        c7 = False

    if all([c1, c2, c3, c4, c5, c6, c7]):
        valid_passports += 1


print(f"Valid Passports (Problem 2) = {valid_passports}")