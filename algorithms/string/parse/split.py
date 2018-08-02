import string


# https://www.facebook.com/groups/405875789586377/permalink/888286181345333/
# https://leetcode.com/problems/decode-ways/description/
def recursive_decode(string, index=0):
    if index == len(string):
        return 0, True
    valid_one, valid_two = False, False
    if string[index] in letter_number_map:
        decode_one, valid_two = recursive_decode(string, index + 1)
    if string[index:index+1] in letter_number_map:
        decode_two, valid_two = recursive_decode(string, index + 2)
    ways = 0
    if valid_one:
        ways += decode_one
    if valid_two:
        ways += decode_two
    return ways

letter_number_map = dict(zip(range(1,27), string.ascii_uppercase))