dictionary = {"Test1": [5, 7, 5, 4, 5], "Test2": [6, 7, 4, 3, 3], "Test3": [9, 9, 6, 5, 5]}
repeats = []
for t in dictionary:
    repeat = 0
    for i in dictionary[t]:
        for j in dictionary[t]:
            if i == j:
                repeat += 1
    repeats.append(repeat)
# min index
tmp = min(repeats)
index = repeats.index(tmp)

tests = list(dictionary.keys())
print(tests[index])

