matrix = [[0 for i in range(100)]for i in range(100)]
row = [0 for i in range(100)]
forwardDiagonal = [0 for i in range(199)]
backwardDiagonal = [0 for i in range(199)]

def checkRow(row,n):
	for i in range(1,n+1):
		if matrix[row][i]==1:
			return True
	return False

def checkDiagonal(row,col,n):
	i=1
	while row+i<n+1 or row-i>0 or col+i<n+1 or col-i>0:
		if row+i<n+1 and col+i<n+1 and matrix[row+i][col+i]==1:
			return True
		if row+i<n+1 and col-i>0 and matrix[row+i][col-i]==1:
			return True
		if row-i>0 and col+i<n+1 and matrix[row-i][col+i]==1:
			return True
		if row-i>0 and col-i>0 and matrix[row-i][col-i]==1:
			return True
		i+=1
	return False

def nqueens(n,col):
	for row in range(1,n+1):
		if checkRow(row,n)==False and checkDiagonal(row,col,n)==False:
			matrix[row][col] = 1
			if col==n:
				return True
			flag = nqueens(n,col+1)
			if flag==False:
				matrix[row][col]=0
			else:
				return True
	return False

def Check(row1,col1,n):
	return row[row1]==True or forwardDiagonal[row1+col1]==True or backwardDiagonal[2*n-1+row1-col1]==True

def Mark(row1,col1,n,arg):
	row[row1] = arg
	forwardDiagonal[row1+col1]=arg
	backwardDiagonal[2*n-1+row1-col1]=arg

def nqueens_branc_bound(n,col):
	for row in range(1,n+1):
		if Check(row,col,n)==False:
			matrix[row][col] = 1
			Mark(row,col,n,True)
			if col==n:
				return True
			flag = nqueens_branc_bound(n,col+1)
			if flag==False:
				matrix[row][col]=0
				Mark(row,col,n,False)
			else:
				return True
	return False

if __name__ == "__main__":
	n = int(input("Enter n(greater than 3) : "))
	nqueens_branc_bound(n,1)
	for i in range(1,n+1):
		print(matrix[i][1:n+1])
