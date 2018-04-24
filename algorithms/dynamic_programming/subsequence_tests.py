from subsequence import *

def test_longest_increasing_subsequence():
	assert [2, 3, 7, 101] == longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])

def test_longest_common_length():
	assert "ADH" == ''.join(longest_common_subsequence("ABCDGH", "AEDFHR"))
	assert "GTAB" == ''.join(longest_common_subsequence("AGGTAB", "GXTXAYB"))