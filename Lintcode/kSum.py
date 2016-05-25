import time
class Solution:
	"""
		Divide-conquer solution
		Time complexity: O(n^k)
		Extra space: O(n)
	"""
	def __init__(self):
		self.cnt=0

	def kSum1(self, A, k, target):
		# @param A: List[int]
		# @param k: int
		# @param target: int
		# @return: int
		if len(A)<k or A==0: return 0

		if k==1:
			
		self.divide(A,k,target,0,len(A)-1)
		return self.cnt

	def kSum2(self, A, k, target):
		list.sort(A)


def main():
	A=[1,3,4,5,8,10,11,12,14,17,20,22,24,25,28,30,31,34,35,37,38,40,42,44,45,48,51,54,56,59,60,61,63,66]
	k=24
	target=842
	start_time=time.time()
	print 'Divide-conquer solution: %d'%(Solution().kSum2(A,k,target))
	print 'Run time: %s ms'% `round(float(time.time()-start_time)*1000.0,5)`

if __name__ == '__main__':
	main()