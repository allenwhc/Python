
class Interval(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end


class Solution:	
	"""
	@param A, queries: Given an integer array and an Interval list
					   The ith query is [queries[i-1].start, queries[i-1].end]
	@return: The result list
	"""
	def intervalSum(self, A, queries):
		# write your code here
		seg_tree=[0]*(4*len(A)-1)
		self.constructTree(A, seg_tree, 0, len(A)-1, 0)
		res=[]
		for q in queries:
			res.append(self.searchSegmentTree(seg_tree, q.start, q.end, 0, len(A)-1, 0))
		return res
	
	def constructTree(self, A, seg, l, r, pos):
		if l==r:
			seg[pos]=A[l]
			return
		mid=(l+r)/2
		self.constructTree(A, seg, l, mid, 2*pos+1)
		self.constructTree(A, seg, mid+1, r, 2*pos+2)
		seg[pos]=seg[2*pos+1]+seg[2*pos+2]
	
	def searchSegmentTree(self, A, start, end, l, r, pos):
		if end<l or start>r: return 0
		if start<=l<=r<=end: return A[pos]
		mid=(l+r)/2
		return self.searchSegmentTree(A, start, end, l, mid, 2*pos+1) + self.searchSegmentTree(A, start, end, mid+1, r, 2*pos+2)
		
A=[100,99,98,97,96,95,94,93,92,91,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,90,89,88,87,86,85,84,83,82,81,71,72,73,74,75,76,77,78,79,80,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]
queries=[Interval(0,99),Interval(0,49),Interval(0,99),Interval(0,59),Interval(0,39),Interval(29,59)]

print Solution().intervalSum(A,queries)