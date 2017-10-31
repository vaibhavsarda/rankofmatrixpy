#Akhil Jarodia 2017130 B1
#Nakul Gupta 2017068 B1
def swapRows(A,row1,col,row2):
	i=0
	while i<col:
		a=A[row1][i]
		A[row1][i]=A[row2][i]
		A[row2][i]=a
		i+=1
		
	return A

def Row_Transformation(A,x,row1,row2):
	i=0
	while i<len(A[0]):
		A[row2][i]=A[row2][i]+(x*A[row1][i])		
		i+=1
		
	return A

def MatrixRank(a):
	rank=len(a[0])
	i=0
	while i<rank:
		if(a[i][i]!=0):
			j=0
			while j<len(a):
				if j!=i:
					a=Row_Transformation(a,-1*(a[j][i]/a[i][i]),i,j)
				j+=1
		else :
			f=100345
			j=i
			while j<len(a):
				if a[j][i] :
					swapRows(a,i,rank,j)
					f=20
					break
				j+=1
			if(f==100345):
				rank-=1
				r=0
				while r<len(a):
					a[r][i]=a[r][rank]
					r+=1
			i-=1		
		i+=1

	return rank



if __name__ == '__main__':
	

	row=int(input("Enter no of rows:"))

	print("Enter elements of matrix row wise:")
	az=[]
	for i in range(row):
		a=input().split()
		a=list(map(int,a))
		az.append(a)
	MatrixRank(az)
