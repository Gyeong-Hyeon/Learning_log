#문제링크: https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    s_res = set(reserve) - set(lost)
    s_lost = set(lost) - set(reserve)

    for r in s_res:
        if r-1 in s_lost:
            s_lost.remove(r-1)
            continue
        elif r+1 in s_lost:
            s_lost.remove(r+1)
            continue
    return n - len(s_lost)

if __name__ == "__main__":
    test_sets = (
                    (
                        5,
                        [2,4],
                        [1,3,5]
                    ),
                    (
                        5,
                        [2,4],
                        [3]
                    ),
                    (
                        3,
                        [3],
                        [1]
                    )
                )
    answers = (5,4,2)

    for test_set, answer in zip(test_sets, answers):
        result = solution(*test_set)
        try:
            assert result == answer
            print('정답이 일치합니다.')
        except AssertionError:
            print('정답이 일치하지 않습니다')
            print(f'테스트 케이스:{test_set}',f'정답:{answer}',f'결과값:{result}')

