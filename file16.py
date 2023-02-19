def filereader(filename):
    with open(filename+'.txt', "r") as f:
        filelist = f.read().split(",")
    equals = 0
    for i in filelist:
        temp = 0
        for j in filelist:
            if i == j:
                temp += 1
        if temp > equals:
            equals = temp
    return equals


file_name = input("Enter file name: ")
print(filereader(file_name))
