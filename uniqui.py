list = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 4, 5]
numbers_dict = dict.fromkeys(list)
for i in numbers_dict:
    idx = []
    for j in range(len(list)):
        if i == list[j]:
            idx.append(j)
    numbers_dict.update({i:idx})
print(numbers_dict)