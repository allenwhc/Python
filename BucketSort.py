from itertools import chain
import Queue
import heapq
def bucketSort(A):
	min_element=min(A)
	max_element=max(A)
	num_buckets=(max_element-min_element)/(len(A)-1)+1
	bucket_size=(max_element-min_element)/num_buckets+1
	bucket=[[] for i in xrange(bucket_size)]
	for e in A:
		index=(e-min_element)/num_buckets
		heapq.heappush(bucket[index],e)
	print bucket
	return list(chain(*bucket))

def main():
	A=[10,2,-3,1,-5,0]
	print bucketSort(A)

if __name__ == '__main__':
	main()