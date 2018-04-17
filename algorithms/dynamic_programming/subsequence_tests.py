from subsequence import *

def test_longest_increasing_length():
	assert 4 == longest_increasing_length([10, 9, 2, 5, 3, 7, 101, 18])

def test_longest_common_length():
	assert 3 == longest_common_length("ABCDGH", "AEDFHR")
	assert 4 == longest_common_length("AGGTAB", "GXTXAYB")