def calculate_structure_sum(*objects):
    summ = 0
    for i in objects:
        if isinstance(i, int) or isinstance(i, float):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
        elif isinstance(i, list) or isinstance(i, set) or isinstance(i, tuple):
            for il in i:
                summ += calculate_structure_sum(il)
        elif isinstance(i, dict):
            for iv in i.values():
                summ += calculate_structure_sum(iv)
            for ik in i.keys():
                summ += calculate_structure_sum(ik)
        else:
            print('чота не так')
    return summ


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)