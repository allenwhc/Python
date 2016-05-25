class RangeSum:
	def __init__(self, A):
		self.A=A

	def rangeSum(self, start, end):
		pass

	def update(self, i, value):
		pass

class SegmentTree(RangeSum):
	def __init__(self, A):
		super(SegmentTree, self).__init__(A)
		self.A=A
		self.seg_tree=[0]*(4*len(self.A)-1)

	def rangeSum(self,start,end):
		pass

	def update(self, i, value):
		pass

	def printTree(self):
		print self.A
