# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

def alternatingCharacters(s):
    listLen = len(s)
    if listLen == 1:
        return 0
    prev_char = s[0]
    count = 0
    for index in range(1,listLen):
        if prev_char == s[index]:
            count += 1
            continue
        else:
            prev_char = s[index]
            continue
    return count