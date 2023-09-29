def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

input = 'input.txt'
with open(input, 'r') as f:
    matrices = []
    matrix = []
    for line in f:
        if line.strip():
            matrix.append(list(map(int, line.split())))
        else:
            matrices.append(matrix)
            matrix = []

symmetric_filename = 'file2.txt'
nonsymmetric_filename = 'file3.txt'

symmetric_count = 0
nonsymmetric_count = 0

with open(symmetric_filename, 'w') as symmetric_file, open(nonsymmetric_filename, 'w') as nonsymmetric_file:
    for matrix in matrices:
        if is_symmetric(matrix):
            symmetric_count += 1

            for row in matrix:
                symmetric_file.write(' '.join(map(str, row)) + '\n')
            symmetric_file.write('\n')
        else:
            nonsymmetric_count += 1

            for row in matrix:
                nonsymmetric_file.write(' '.join(map(str, row)) + '\n')
            nonsymmetric_file.write('\n')

print("Количество симметричных матриц:", symmetric_count)
print("Количество несимметричных матриц:", nonsymmetric_count)