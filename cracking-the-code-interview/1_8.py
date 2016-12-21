# If an element in the MxN matrix is 0, its entire row and column are set to 0.

from copy import copy
def zero_matrix(matrix):
	clear_rows = [False]*len(matrix)
	clear_cols = [False]*len(matrix[0])
	new_matrix = copy(matrix)
	for r in range(len(matrix)):
		for c in range(len(matrix[r])):
			if matrix[r][c] == 0:
				clear_rows[r] = True
				clear_cols[c] = True

	for r in range(len(clear_rows)):
		if clear_rows[r]:
			for i in range(len(new_matrix[r])):
				new_matrix[r][i] = 0

	for c in range(len(clear_cols)):
		if clear_cols[c]:
			for i in range(len(new_matrix)):
				new_matrix[i][c] = 0
	return new_matrix

m = [
	[1, 2, 3, 4],
	[0, 1, 2, 3],
	[1, 0, 3, 4]
    ]

def print_matrix(m):
	for row in m:
		print(row)
print_matrix(m)
print("--- changed to ---")
print_matrix(zero_matrix(m))
