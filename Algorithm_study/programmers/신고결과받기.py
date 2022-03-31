#문제 링크 https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    dic_rpt = dict()
    #s_report = list(map(lambda x : x.split(' '), report))
    s_rpt = set(report)

    for users in s_rpt:
        reporter, reportee = users.split(' ')
        
        try:
            dic_rpt[reportee].append(reporter)
        except:
            dic_rpt[reportee] = [reporter]
    
    for v in dic_rpt.values():
        if len(v) < k:
            continue
        
        for user in v:
            idx = id_list.index(user)
            answer[idx]+=1
    
    return answer

if __name__ == "__main__":
    test_sets = (
                    (
                        ["muzi","frodo","apeach","neo"],
                        ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
                        2
                    ),
                    (
                        ["con", "ryan"],
                        ["ryan con", "ryan con", "ryan con", "ryan con"],
                        3
                    )
                )
    answers = ([2,1,1,0],[0,0])

    for test_set, answer in zip(test_sets, answers):
        result = solution(*test_set)
        try:
            assert result == answer
            print('정답이 일치합니다.')
        except AssertionError:
            print('정답이 일치하지 않습니다')
            print(f'테스트 케이스:{test_set}',f'정답:{answer}',f'결과값:{result}')
