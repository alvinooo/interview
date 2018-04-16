[10, 9, 2, 5, 3, 7, 101, 18]
[1,  1, 1, 2, 2, ]
[2, 3, 7, 101]
def longest_increasing_length(l):
	lengths = [1] * len(l)
	for curr_index in xrange(1, len(l)):
		curr_length = 1
		for prev in xrange(curr_index):
			if l[curr_index] > l[prev]:
				curr_length = lengths[prev] + 1
		lengths[curr_index] = max(lengths[curr_index], curr_length)
	return lengths[-1]

def test_longest_increasing_length():
	print longest_increasing_length([10, 9, 2, 5, 3, 7, 101, 18])

# test_longest_increasing_length()

# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/