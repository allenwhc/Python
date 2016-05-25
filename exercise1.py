#print script
def checkStack(stack):
	try:
		stack[0]
		print stack[-1]
	except:
		raise Exception('empty stack')
stack=[]
stack.append(0)
checkStack(stack)
stack.append(1)
checkStack(stack)
stack.pop()
stack.pop()
checkStack(stack)
