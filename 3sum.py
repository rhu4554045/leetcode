import itertools


def threeSum(nums):
    nums.sort()
    n, p, z = [i for i in nums if i < 0], [i for i in nums if i > 0], [i for i in nums if i == 0]
    n_lst = set(n)
    p_lst = set(p)

    ret = set()

    # 1. at least 1 zero
    if z:
        for i in n:
            if -1 * i in p:
                ret.add((i, 0, - 1 * i))

    # 2. 3 zeros
    if len(z) >= 3:
        ret.add((0, 0, 0))

    # 3. 2n and 1p
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            tar = -1 * (n[i] + n[j])
            if tar in p_lst:
                ret.add(tuple(sorted([n[i], n[j], tar])))

    # 4. 1n and 2p
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            tar = -1 * (p[i] + p[j])
            if tar in n_lst:
                ret.add(tuple(sorted([tar, p[i], p[j]])))

    return ret


nums = [-1, 0, 1, 2, -1, -4]

print(threeSum(nums))
