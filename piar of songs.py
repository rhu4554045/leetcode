import collections
import itertools

def numParisDivisibleBy60(time):
    ret = 0
    songs = collections.defaultdict(int)

    for song in time:
        if song % 60 == 0:
            ret += songs[song % 60]
        else:
            ret += songs[60 - song % 60]

        songs[song % 60] += 1

    return ret


def numParisDivisibleBy60_comb(time):
    comb = itertools.combinations(range(len(time)),2)
    res = []
    ret = 0
    for song in time:
        res.append(song%60)

    for f, s in comb:
        if (res[f]+res[s])%60 == 0:
            ret += 1

    return  ret



time = [30,20,150,100,40]

print(numParisDivisibleBy60_comb(time))