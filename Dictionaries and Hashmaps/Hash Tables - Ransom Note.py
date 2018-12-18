# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def checkMagazine(magazine, note):
    hMaps1 = {}
    hMaps2 = {}
    answer = 'Yes'
    for i in magazine:
        if i in hMaps1:
            hMaps1[i] += 1
        else:
            hMaps1[i] = 1
    for i in note:
        if i in hMaps2:
            hMaps2[i] += 1
        else:
            hMaps2[i] = 1
    for i in hMaps2:
        if i in hMaps1 and hMaps1[i] >= hMaps2[i]:
            continue
        else:
            answer = 'No'
            break
    print(answer)