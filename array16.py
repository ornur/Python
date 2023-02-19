n = int(input())   # read the integer N
a = list(map(float, input().split()))   # read the sequence of N real numbers
result = []   # initialize an empty list to store the result

for i in range(n//2):   # iterate over the first half of the list
    result.append(a[i])   # add the ith element to the result
    result.append(a[n-i-1])   # add the (n-i-1)th element to the result

if n % 2 != 0:   # if N is odd
    result.append(a[n//2])   # add the middle element to the result

print(result)   # print the result
