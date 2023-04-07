

def lengthOfLongestSubstring(s):
    check_lst = {}
    left, right, output = 0, 0, 0

    for right in range(len(s)):
        if s[right] in check_lst:
            left = max(left, check_lst[s[right]] + 1)
        check_lst[s[right]] = right
        output = max(output, right - left +1)

    return output


s = "dvdf"
print(lengthOfLongestSubstring(s))

