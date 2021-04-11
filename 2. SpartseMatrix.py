import numpy as np


class SparseMatrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.s = [[m, n, 0]]

    def append(self, i, j, value):
        if value != 0:
            self.s.append([i, j, value])
            self.s[0][2] += 1

    def shape(self):
        return self.m, self.n

    def getValue(self, i, j):
        for k in range(1, len(self.s)):
            if (self.s[k][0] == i) and (self.s[k][1] == j):
                return self.s[k][2]
        return 0

    def print(self):
        result = np.zeros((self.m, self.n))
        for i in range(1, len(self.s)):
            result[self.s[i][0] - 1, self.s[i][1] - 1] = self.s[i][2]
        print(result)

    @classmethod
    def mult(cls, a, b):
        if a.n != b.m:
            print("Null")
        else:
            c = SparseMatrix(a.m, b.n)
            for i in range(1, a.m + 1):
                for j in range(1, b.n + 1):
                    result = 0
                    for k in range(1, a.n + 1):
                        result += a.getValue(i, k) * b.getValue(k, j)
                    if result != 0:
                        c.append(i, j, result)
            return c


a = SparseMatrix(3, 3)
b = SparseMatrix(3, 2)

a.append(1, 1, 1)
a.append(2, 2, 2)
a.append(3, 3, 3)
b.append(1, 1, 1)
b.append(2, 2, 1)

a.print()
b.print()

c = SparseMatrix.mult(a, b)
c.print()
