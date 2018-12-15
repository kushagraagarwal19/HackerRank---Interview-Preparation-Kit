# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def makeAnagram(a, b):
    count = 0
    for char in a:
        if char not in b:
            count += 1
    print(count)
    for char in b:
        if char not in a:
            count += 1
    print(count)
    return count