def spiral_order(matrix):
    m = len(matrix)
    result = []
    if m == 1:
        result.append(matrix[0][0])
    else:
        for i in range(m // 2):
            for j in range(i, m - i - 1):
                result.append(matrix[j][i])
            for j in range(i, m - i - 1):
                result.append(matrix[m - i - 1][j])
            for j in range(m - i - 1, i, -1):
                result.append(matrix[j][m - i - 1])
            for j in range(m - i - 1, i, -1):
                result.append(matrix[i][j])
            if m % 2 == 1:
                result.append(matrix[m // 2][m // 2])
    return result


matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]
print(spiral_order(matrix))