

def getSuffix(t):
	i,j=1,0
	res=[0]*len(t)
	while i<len(t):
		print (j,i)
		if t[i]==t[j]:
			res[i]=j+1
			i+=1
			j+=1
		else:
			j=res[j-1]
			i+=1

	print (res)

def KMP(s,t):
	if not s or not t or len(s)<len(t): return ''
	suffix=getSuffix(t)
	return ''

def main():
	s='sasfagfadga'
	t='aabaabaaa'
	print (KMP(s,t))

if __name__ == '__main__':
	main()