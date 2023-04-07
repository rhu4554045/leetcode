import math


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_p = math.inf
    profit = 0

    for p in prices:
        if p < min_p:
            min_p = p
        elif (p - min_p) > profit:
            profit = p - min_p

    return profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))


# buy and sell 2
def maxProfit2(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_p = math.inf
    profit = 0
    cul_profit = 0

    for p in prices:
        if p < min_p:
            min_p = p
            cul_profit += profit
            profit = 0
        elif (p - min_p) > profit:
            profit = p - min_p
        elif (p - min_p) < profit:
            cul_profit += profit
            min_p = p
            profit = 0

        # print("current price", p)
        # print("current min price",min_p)
        # print("current profit",profit)
        # print("current cumulative profit", cul_profit)
        # print("")

    if profit > 0:
        cul_profit += profit

    return cul_profit


prices = [7, 1, 5, 3, 6, 4]
prices2 = [1, 2, 3, 4, 5]
prices3 = [7, 6, 4, 3, 1]
prices4 = [2, 1, 2, 0, 1]

print(maxProfit2(prices))
print(maxProfit2(prices2))
print(maxProfit2(prices3))
print(maxProfit2(prices4))


# buy and sell 3
def maxProfit3(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_p = math.inf
    profit = 0
    profit_max = 0
    profit_max2 = 0

    count = 0
    p_len = len(prices)
    while count < p_len:
        p = prices[count]
        profit_sub = 0
        min_sub = math.inf
        if p < min_p:
            min_p = p
            for p_sub in prices[count:]:
                print("current price", p_sub)
                if p_sub < min_sub:
                    min_sub = p_sub
                elif (p_sub - min_sub) > profit_sub:
                    profit_sub = p_sub - min_sub

            if (profit_max + profit_max2) < (profit + profit_sub):
                profit_max = profit
                profit_max2 = profit_sub
                profit = 0
        elif (p - min_p) > profit:
            profit = p - min_p
        elif (p - min_p) < profit:
            for p_sub in prices[count:]:
                print("current price", p_sub)
                if p_sub < min_sub:
                    min_sub = p_sub
                elif (p_sub - min_sub) > profit_sub:
                    profit_sub = p_sub - min_sub

            if (profit_max + profit_max2) < (profit + profit_sub):
                profit_max = profit
                profit_max2 = profit_sub
                profit = 0

        count += 1

        print("current price", p)
        print("current min price", min_p)
        print("current profit", profit)
        print("current profit sub", profit_sub)
        print("current first max profit", profit_max)
        print("current second max profit", profit_max2)
        print("")

    if ((profit_max + profit_max2) == 0) & (prices[0] < prices[p_len - 1]):
        return (max(prices) - min(prices))
    elif ((profit_max + profit_max2) == 0) & (profit > 0):
        return profit
    else:
        return profit_max + profit_max2


### test
prices = [397, 6621, 4997, 7506, 8918, 1662, 9187, 3278, 3890, 514, 18, 9305, 93, 5508, 3031, 2692, 6019, 1134, 1691,
          3842, 3285, 8951, 1826, 7616, 2324, 648, 9252, 5476, 8556, 4445, 6784]
print(maxProfit3(prices))


# buy and sell 3
def maxProfit3_best(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    t1_cost, t2_cost = math.inf, math.inf
    t1_profit, t2_profit = 0, 0

    for p in prices:
        t1_cost = min(t1_cost, p)
        t1_profit = max(t1_profit, p - t1_cost)

        t2_cost = min(t2_cost, p - t1_profit)
        t2_profit = max(t2_profit, p - t2_cost)
    return t2_profit


prices = [397, 6621, 4997, 7506, 8918, 1662, 9187, 3278, 3890, 514, 18, 9305, 93, 5508, 3031, 2692, 6019, 1134, 1691,
          3842, 3285, 8951, 1826, 7616, 2324, 648, 9252, 5476, 8556, 4445, 6784]
print(maxProfit3_best(prices))
