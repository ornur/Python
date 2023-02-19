def longest_substring_without_repeating_characters(string):
    l = len(string)
    max = 0
    maxs = ""
    for i in range(l):
        for j in range(l, i, -1):
            f = True
            for k in range(i, j):
                for o in range(i, j):
                    if k != o and string[k] == string[o]:
                        f = False
                        break
            if f and j - i > max:
                max = j - i
                maxs = string[i:j]
    return maxs


print(longest_substring_without_repeating_characters("12345678912345"))
