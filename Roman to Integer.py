def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    sum = 0
    roman_dict = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
    count = 0
    num_lst = [roman_dict[st] for st in s]

    while count < len(num_lst):
        crr = num_lst[count]
        count += 1
        nxt = num_lst[count] if count < len(num_lst) else crr
        if crr >= nxt:
            sum += crr
        else:
            sum += nxt - crr
            count += 1

    return sum


s = "MCMXCIV"
print(romanToInt(s))
