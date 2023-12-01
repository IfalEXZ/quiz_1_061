class MatrixOperations:
    def __init__(self, matrix):
        self.matrix = matrix

    def find_min_max(self):
        min_value = min(min(row) for row in self.matrix)
        max_value = max(max(row) for row in self.matrix)
        return min_value, max_value

    def transpose_matrix(self):
        transposed_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return transposed_matrix

    def multiply_matrices(self):
        transposed_matrix = self.transpose_matrix()
        result_matrix = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*transposed_matrix)] for row_a in self.matrix]
        return result_matrix

    def add_matrices(self):
        transposed_matrix = self.transpose_matrix()
        result_matrix = [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self.matrix, transposed_matrix)]
        return result_matrix


if __name__ == "__main__":
    A = [
        [34, 100, 12],
        [72, 24, 55],
        [61, 20, 19]
    ]

    matrix_ops = MatrixOperations(A)

    min_value, max_value = matrix_ops.find_min_max()
    print("Min value:", min_value)
    print("Max value:", max_value)

    transposed_matrix = matrix_ops.transpose_matrix()
    print("Transposed matrix:")
    for row in transposed_matrix:
        print(row)

    multiplied_matrix = matrix_ops.multiply_matrices()
    print("Multiplied matrix:")
    for row in multiplied_matrix:
        print(row)

    added_matrix = matrix_ops.add_matrices()
    print("Added matrix:")
    for row in added_matrix:
        print(row)