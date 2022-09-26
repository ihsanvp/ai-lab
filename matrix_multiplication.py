def display(matrix, m, n) :
	for i in range(m) :
		print("[", end="")
		for j in range(n) :
			print(f"\t{matrix[i][j]}", end="")
		print("\t]")

A = [[1,4,6],
	[2,5,8],
	[7,9,1]]
	
B = [[7,4,1],
	[9,1,4],
	[0,7,3]]

result = [[0,0,0],
		 [0,0,0],
		 [0,0,0]]
		 
m = len(A)
n = len(A[0])

for i in range(m) :
	for j in range(n) :
		for k in range(m) :
			result[i][j] += A[i][k] * B[k][j]
	
print("Matrix 1")
display(A, m, n)

print("\nMatrix 2")
display(B, m, n)

print("\nResult")
display(result, m, n)
