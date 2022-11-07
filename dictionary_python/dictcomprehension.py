# {KEY:VALUE FOR KEY IN ....}
d = {i: i * 2 for i in range(1, 6)}
print(d)  # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

d = {i: len(i) for i in ['name', 'name1', 'name11']}
print(d)  # {'name': 4, 'name1': 5, 'name11': 6}
