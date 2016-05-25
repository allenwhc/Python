class BinaryIndexTree:
	def __init__(self,A):
		self.A=A
		self.index_tree=[0]*(len(A)+1)
		self.constructTree()

	def constructTree(self):
		for i,x in enumerate(self.A):
			print i, 
			binary_rep=bin(i)[2:]
			print self.getNextNode(binary_rep)

	def getPrevNode(self, binary_rep):
		pass

	def getNextNode(self, binary_rep):
		twosComp=self.twosComplement(int(binary_rep,2), len(binary_rep))
		print twosComp
	
	def twosComplement(self, val, bits):
		mask=1
		for i in xrange(bits): mask <<= 1
		print mask

A=[3,2,-1,6,5,4,-3,3,7,2,3]
bit=BinaryIndexTree(A)
print bit.index_tree