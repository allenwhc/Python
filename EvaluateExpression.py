import operator
import math
class Solution(object):
	"""
		Evaluate expression
		Stack solution
		Time complextity: O(nk)
		Extra space: O(n)
	"""
	def evaluateExpression(self, expression):
		if not expression: return 0
		nums,ops=[],[]
		d={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.div}
		def isPrior(a,b):
			if a=='*' or a=='/': return True
			elif a=='+' or a=='-': return False if b=='*' or b=='/' else True
			else: return False
		for e in expression:
			if e.isdigit(): nums.append(int(e))
			elif e=='(': ops.append(e)
			elif e==')':
				while ops and ops[-1]!='(':
					num1,num2=nums.pop(),nums.pop()
					nums.append(d[ops.pop()](num2,num1))
				ops.pop()
			else:
				while ops and isPrior(ops[-1],e):
					num1,num2=nums.pop(),nums.pop()
					nums.append(d[ops.pop()](num2,num1))
				ops.append(e)
		while ops:
			num1,num2=nums.pop(),nums.pop()
			nums.append(d[ops.pop()](num2,num1))
		return nums.pop() if nums else 0

	"""
		Convert infix expression to postfix expression
		Stack solution
		Time complextity: O(nk)
		Extra space: O(n)
	"""
	def convertToRPN(self, expression):
		if not expression: return []
		symbols=['+','-',]
		RPN,ops=[],[]
		count=0
		def precedence(a, b):
			if b=='*' or b=='/': return True
			elif b=='-' or b=='+': return False if a=='*' or a=='/' else True
			return False
		for e in expression:
			if e.isdigit(): RPN.append(e)
			elif e=='+' or e=='-' or e=='*' or e=='/':
				while ops and precedence(e,ops[-1]):
					RPN.append(ops.pop())
				ops.append(e)
			elif e=='(':
				ops.append(e)
			else:
				while ops and ops[-1]!='(':
					RPN.append(ops.pop())
				ops.pop()

		while ops: RPN.append(ops.pop())
		return RPN

	"""
		Evaluate RPN expression
		Stack solution
		Time complextity: O(nk)
		Extra space: O(n)
	"""
	def evaluateRPN(self, expression):
		stack=[]
		for e in expression:
			stack.append(e if e not in '+-*/' else str(int(eval(stack.pop(-2)+e+stack.pop()+'.'))))
		return int(stack.pop())

def main():
	expression=["(","(","1","+","(","2",")",")","*","3","+","(","4","/","2",")","-","5",")"]
	print 'Infix expression:',expression
	print 'Evaluate infix expression: %d'%(Solution().evaluateExpression(expression))
	print 'Reverse Polish notation is:',Solution().convertToRPN(expression)
	print 'Evaluate postfix expression: %d'%(Solution().evaluateRPN(Solution().convertToRPN(expression)))

if __name__ == '__main__':
	main()