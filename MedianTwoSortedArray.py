import time
class Solution:
	"""
		Merge sort solution
		Time complexity: O(log(m+n))
		Extra space: O(1)
	"""
	def findMedian1(self, A, B):
		A,B=sorted((A,B),key=len)
		m,n=len(A),len(B)
		mid_after=(m+n-1)/2
		l,r=0,m
		while l<r:
			mid=(l+r)/2
			if mid_after-mid<1 or A[mid]>=B[mid_after-mid-1]: r=mid
			else: l=mid+1
		roc=sorted(A[l:l+2]+B[mid_after-l:mid_after-l+2])
		return (roc[0]+roc[1-(m+n)%2])/2.0

	"""
		Divide conquer solution
		Time complexity: O(log(m+n))
		Extra space: O(n)
	"""
	def findMedian2(self, A, B):
		m,n=len(A),len(B)
		if (m+n)%2: return float(self.divideConquer(A, B, 0, m-1, 0, n-1, (m+n)/2))
		else: return (self.divideConquer(A, B, 0, m-1, 0, n-1, (m+n)/2) + self.divideConquer(A, B, 0, m-1, 0, n-1, (m+n)/2-1))/2.0

	def divideConquer(self, A, B, s1, e1, s2, e2, pos):
		len_A,len_B=e1-s1+1, e2-s2+1
		if not len_A: return A[s1+pos]
		if not len_B: return B[s2+pos]
		if not pos: return min(A[s1],B[s2])

		mid_1=pos*len_A/(len_A+len_B)
		mid_2=pos-mid_1-1
		mid_1+=s1
		mid_2+=s2

		if A[mid_1]<=B[mid_2]:
			return self.divideConquer(A, B, mid_1+1, e1, s2, mid_2, pos-(mid_1-s1+1))
		else:
			return self.divideConquer(A, B, s1, mid_1, mid_2+1, e2, pos-(mid_2-s2+1))


def main():
	A=[1,2,3,4,5,6]
	B=[2,3,4,5]
	start_time=time.time()
	print 'Median is: %f'%(Solution().findMedian1(A,B))
	print 'Run time: %s ms'%round((time.time()-start_time)*1000,5)
	start_time=time.time()
	print 'Median is: %f'%(Solution().findMedian2(A,B))
	print 'Run time: %s ms'%round((time.time()-start_time)*1000,5)

if __name__ == '__main__':
	main()