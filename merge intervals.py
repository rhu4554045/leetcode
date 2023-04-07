def merge(intervals):
    intervals.sort()

    ret = []

    for start, end in intervals:
        if not ret or start > ret[-1][1]:
            ret.append([start,end])
        else:
            ret[-1][1] = max(ret[-1][1], end)


    return ret


intervals = [[1, 3],[1,2], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))