def longest_increasing_subsequence(l):
    lengths = [1] * len(l)
    max_length, max_length_index = 1, 0
    for curr_index in range(1, len(l)):
        curr_length = 1
        for prev in range(curr_index):
            if l[curr_index] > l[prev]:
                curr_length = lengths[prev] + 1
        lengths[curr_index] = max(lengths[curr_index], curr_length)
        if lengths[curr_index] > max_length:
            max_length_index = curr_index
            max_length = lengths[curr_index]
    subsequence = [l[max_length_index]]
    curr_index = max_length_index
    for i in range(max_length_index - 1, -1, -1):
        if lengths[i] + 1 == lengths[curr_index]:
            subsequence.insert(0, l[i])
            curr_index = i
    return subsequence


def longest_common_subsequence(l1, l2):
    lengths = [[0 for _ in range(len(l2) + 1)] for _ in range(len(l1) + 1)]
    for i in range(1, len(l1) + 1):
        for j in range(1, len(l2) + 1):
            if l1[i - 1] == l2[j - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j],
                                    lengths[i][j - 1])
    subsequence = []
    i, j = len(l1), len(l2)
    while i > 0 and j > 0:
        if l1[i - 1] == l2[j - 1] and lengths[i][j] == lengths[i - 1][j - 1] + 1:
            subsequence.insert(0, l1[i - 1])
            i, j = i - 1, j - 1
        if lengths[i - 1][j] > lengths[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return subsequence


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
