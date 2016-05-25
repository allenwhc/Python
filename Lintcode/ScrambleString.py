class Solution:
	def isScramble(self, s1, s2):
		# @param s1: str
		# @param s2: str
		# @return: bool
		if len(s2)!=len(s1): return False
		if not cmp(s1,s2): return True

		ascii_sum_s1,ascii_sum_s2=0,0
		ascii_sum_s1=sum(ord(c)-ord('a') for c in s1)
		ascii_sum_s2=sum(ord(c)-ord('a') for c in s2)
		if cmp(ascii_sum_s1,ascii_sum_s2): return False

		for i in xrange(1,len(s1)):
			if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]): return True
			elif self.isScramble(s1[:i],s2[len(s1)-i:]) and self.isScramble(s1[i:],s2[:len(s1)-i]): return True
		return False


def main():
	s1='great'
	s2='rgtae'
	if Solution().isScramble(s1,s2):
		print '%s is a scrambled string of %s.'%(s2,s1)
	else:
		print '%s is not a scrambled string of %s.'%(s2,s1)

if __name__ == '__main__':
	main()