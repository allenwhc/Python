import re
class Solution:
	def numberOfPatterns(self, m, n):
		if not m or not n: return 0
		def backTracking(m,n,patterns):
			while len(patterns)<=n:
				invalid_move='[^2]*(13|31)|[^4]*(17|71)|[^8]*(79|97)|[^6]*(39|93)|[^5]*(19|28|37|46|64|73|82|91)'
				invalid_move=re.compile(invalid_move).match
				patterns+=[p+d for p in patterns[-1] for d in '123456789'
							if d not in p and not invalid_move(p+d)],

			return sum(map(len, patterns[m:n+1]))
		return backTracking(m,n,[['']])

		

def main():
	m=3
	n=4
	print 'Number of unlock patterns: %d'%(Solution().numberOfPatterns(m,n))

if __name__ == '__main__':
	main()