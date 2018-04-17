def longest_increasing_length(l, length=True):
	lengths = [1] * len(l)
	for curr_index in range(1, len(l)):
		curr_length = 1
		for prev in range(curr_index):
			if l[curr_index] > l[prev]:
				curr_length = lengths[prev] + 1
		lengths[curr_index] = max(lengths[curr_index], curr_length)
	return lengths[-1]

def longest_common_length(l1, l2, length=True):
	lengths = [[0 for _ in range(len(l2) + 1)] for _ in range(len(l1) + 1)]
	for i in range(1, len(l1) + 1):
		for j in range(1, len(l2) + 1):
			if l1[i - 1] == l2[j - 1]:
				lengths[i][j] = lengths[i - 1][j - 1] + 1
			else:
				lengths[i][j] = max(lengths[i - 1][j],
					lengths[i][j - 1])
	return lengths[len(l1)][len(l2)]

"ADH"
"GTAB"

# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

[0, 8]

[0, 4]

[0, 4, 12]
[0, 2]

[0, 4, 12]
[0, 2, 10]

[0, 2, 6, 9, 11, 15]