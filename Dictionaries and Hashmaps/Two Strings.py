# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def twoStrings(s1, s2):
    hMaps1 = {}
    for i in s1:
        hMaps1[i] = 1
    for i in s2:
        if i in hMaps1:
            return 'YES'
    return 'NO'