k = int(input())
sequence = []
element = int(input())
order = 0

while element != 0:  # continue reading elements until 0 is encountered
    sequence.append(element)
    element = int(input())

for i in range(len(sequence)):   # iterate over the indices of the list
    if sequence[i] > k:
        order = i + 1

print(order)
