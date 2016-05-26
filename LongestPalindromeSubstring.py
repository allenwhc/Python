
"""
	Center expansion algorithm
	Time complexity: O(n^2)
	Extra space: O(n)
"""
def longestPalindrome1(s):
	s='|'.join(list(s))
	length=[0]*len(s)
	for i in range(len(s)):
		l,r=i-1,i+1
		while True:
			if l<0 or r>len(s)-1: break
			if s[l]!=s[r]: break
			l-=1
			r+=1
		length[i]=(r-l,l,r) if l>=0 and r<=len(s)-1 else (0,0,0)
	(max_length,start,end)=max(length, key=lambda x:x[0])
	res=list(s[start+1:end])
	return ''.join([e for e in res if e!='|'])
"""
	Manacher's algorithm
	Time complexity: O(n)
	Extra space: O(n)
"""
def longestPalindrome2(s):
	if not s: return ''
	s='$|'+'|'.join(list(s))+'|@'
	print (s)
	P=[0]*len(s)
	C,R=0,0
	for i in range(1,len(s)-1):
		mirror=2*C-i
		if i<R:
			P[i]=min(P[mirror],R-i)
		while s[i+(1+P[i])]==s[i-(1+P[i])]: P[i]+=1
		if i+P[i]>R:
			C=i
			R=i+P[i]
	max_length=max(P)
	center=P.index(max_length)
	return ''.join([e for e in s[center-max_length:center+max_length] if e!='|'])

def main():
	s='bb'
	#s='abaxabaxabybaxabyb'
	print ('Longest palindrome of %s is: %s'%(s,longestPalindrome2(s)))

if __name__ == '__main__':
	main()