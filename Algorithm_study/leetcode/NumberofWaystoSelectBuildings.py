"""
Q.Number of ways to select buildings
(문제 링크: https://leetcode.com/problems/number-of-ways-to-select-buildings/)

- 주어지는 파라미터 s는 이진 문자열입니다.
    - s[i] = 0은 거리의 i번째 빌딩이 사무실임을 뜻합니다.
    - s[i] = 1은 거리의 i번째 빌딩이 식당임을 뜻합니다.

- 세 개의 빌딩을 랜덤으로 선택하여 검사할 때 두 개의 연속적인 빌딩이 같은 타입일 수 없습니다.
- 문자열 s의 길이는 3이상 100000이하입니다.
- 세 개의 빌딩을 선택할 수 있는 경우의 수를 리턴하세요.

[예시 1]
S = "001101"
return = 6
([0,2,4],[0,3,4],[1,2,4],[1,3,4],[2,4,5],[3,4,5])

[예시 2]
S = "11100"
return = 0
"""

def numberOfWays(s:str) -> int:
    c0, c1, c10, c01, ans = 0, 0, 0, 0, 0
    for i in range(len(s)):
        if s[i] == '0': 
            ans += c01
            c0 += 1
            c10 += c1                
        else: 
            ans += c10
            c1 += 1
            c01 += c0  
    return ans