class Solution:
	# @param m: An integer m denotes the size of a backpack
	# @param A & V: Given n items with size A[i] and value V[i]
	# @return: The maximum value
	def backPackII(self, m, A, V):
		# write your code here
		if not A or not V or not m or len(A)!=len(V): return 0
		n=len(A)
		D=[[0]*(m+1) for i in xrange(n+1)]
		for i in xrange(1, n+1):
			for j in xrange(m+1):
				if j<A[i-1]: D[i][j]=D[i-1][j]
				if j>=A[i-1]: D[i][j]=max(D[i-1][j], D[i-1][j-A[i-1]]+V[i-1])
		return D[-1][-1]

m,A,V=100, [77,22,29,50,99], [92,22,87,46,90]
print Solution().backPackII(m,A,V)