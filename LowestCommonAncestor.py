class TreeNode:
	def __init__(self, x):
		self.val=x
		self.left,self.right=None,None

"""
	Normal Binary Tree
	Time complexity: O(n)
	Extra space: O(1)
"""
def lowestCommonAncestor(root, node1, node2):
	if not root: return None
	if root==node1 or root==node2: return root
	left=lowestCommonAncestor(root.left, node1, node2)
	right=lowestCommonAncestor(root.right, node1, node2)
	if left and right: return root
	if not left and not right: return None
	return left if left else right

"""
	Bianry search tree
	Time complexity: O(logn)
	Extra space: O(1)
"""
def lowestCommonAncestorBST(root, node1, node2):
	if root.val>max(node1.val, node2.val): return lowestCommonAncestorBST(root.left, node1, node2)
	elif root.val>min(node1.val, node2.val): return lowestCommonAncestorBST(root.right, node1, node2)
	else: return root

def printTree(root, indent):
	if not root: return
	printTree(root.right, indent+'   ')
	print (indent+str(root.val))
	printTree(root.left, indent+'   ')

def main():
	root=TreeNode(3)
	root.left=TreeNode(6)
	root.right=TreeNode(8)
	root.left.left=TreeNode(2)
	root.left.right=TreeNode(11)
	root.right.right=TreeNode(13)
	root.right.right.left=TreeNode(7)
	root.left.right.left=TreeNode(9)
	root.left.right.right=TreeNode(5)
	printTree(root, '')

	node1=root.left.left
	node2=root.left.right.right
	print ('Lowest common ancestor of %d and %d is: %d.'% (node1.val, node2.val, lowestCommonAncestor(root,node1,node2).val))


if __name__ == '__main__':
	main()