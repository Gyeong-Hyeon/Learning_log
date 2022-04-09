"""
Q.Length of the longest substring
(문제 링크: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/)

- 문자열 s가 주어질 때 중복되지 않은 문자를 포함하는 가장 긴 substring의 길이를 구하세요.
- 문자열 s의 길이는 0이상 50000이하입니다.
- 문자열은 영문자, 숫자, 기호, 띄어쓰기를 포함합니다.

[예시 1]
s = "abcabcbb"
return = 3
(abc)

[예시 2]
s = "bbbbb"
return = 1
(b)

[예시 3]
s = "pwwkew"
return = 3
(wke) *pwke는 연속되지 않으므로 취급하지 않음
"""

def lengthOfLongestSubstring(s:str) -> int:
    if not s:
        return 0
    elif len(s) == 1:
        return 1

    sub_str = ''
    max_len = 0
    for c in s:
        if c in sub_str:
            if max_len < len(sub_str):
                max_len = len(sub_str)
            idx = sub_str.find(c)
            substr = substr[idx+1:]
        sub_str+=c
    return max(max_len, len(sub_str))

#Runtime: 57 ms, faster than 94.02% of Python3 online submissions
#Memory Usage: 14.1 MB, less than 54.04% of Python3 online submissions
