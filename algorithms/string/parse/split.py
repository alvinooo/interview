import string


# https://www.facebook.com/groups/405875789586377/permalink/888286181345333/
# https://leetcode.com/problems/decode-ways/description/
def recursive_decode(s, index=0):
    if index >= len(s):
        return 1
    if s[index] == '0':
        return 0
    ways = recursive_decode(s, index + 1)
    if index + 1 < len(s) and int(s[index:index+1]) <= 26:
        ways += recursive_decode(s, index + 2)
    return ways


def dynamic_decode(s):
    ways = [0] * (len(s) + 1)
    ways[len(s) - 1] = 1 if s[len(s) - 1] != '0' else 0
    ways[-1] = 1
    for index in range(len(s) - 2, -1, -1):
        if s[index] == '0':
            continue
        ways[index] = ways[index + 1]
        if int(s[index:index+1]) <= 26:
            ways[index] += ways[index + 2]
    return ways[0]
