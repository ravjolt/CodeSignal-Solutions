def solution(matrix):
    x = 0
    
    for i in range(len(matrix[0])):
        if matrix[0][i] != 0:
            x += matrix[0][i]
    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i-1][j] == 0:
                matrix[i][j] = 0
            x += matrix[i][j]

    return (x)