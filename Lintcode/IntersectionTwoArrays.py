from collections import Counter
class Solution:
	def intersection(self, nums1, nums2):
		d={e:i for i,e in enumerate(nums1)}
		res=set([x for x in nums2 if x in d])
		return list(res)

	def intersect(self, nums1, nums2):
		count1=Counter(nums1)
		count2=Counter(nums2)
		inter=count1&count2
		res=[key*value for key,value in inter.items()]
		return res

def main():
	nums1=[1,2,2,1]
	nums2=[2,2]
	print Solution().intersection(nums1,nums2)
	print Solution().intersect(nums1,nums2)

if __name__ == '__main__':
	main()