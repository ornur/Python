n = int(input())      # read the integer N
sequence = list(map(int, input().split()))   # read the sequence of N integers
min_element = min(sequence)   # find the minimal element
index = sequence.index(min_element)   # find the index of the first occurrence of the minimal element
count = index   # count the number of elements before the first minimal element

print(count)   # print the number of elements before the first minimal element
