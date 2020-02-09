class Matrix:
    def __init__(self, matrix_string):
        self.matrix = {}
        rows = matrix_string.split("\n")
        for i, row in enumerate(rows):
            self.matrix[i] = list(map(int, row.split(" ")))

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        result = [x[index - 1] for x in self.matrix.values()]
        return result

