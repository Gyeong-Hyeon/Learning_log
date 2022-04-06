def solution(n, computers):
    visited = [False]*n
    answer = 0
    def dfs(start):
        visited[start] = True
        for neighbor in range(n):
            if visited[neighbor] or neighbor == start:
                continue
            elif computers[start][neighbor] == 1:
                dfs(neighbor)
    
    for c in range(n):
        if visited[c]:
            continue
        dfs(c)
        answer+=1
    return answer

if __name__ == "__main__":
    from numpy import random

    def graph2coms(graph):
        return [[int(k in j) for k in graph.keys()] for i, j in graph.items()]
    
    for trial in range(5):
        nets = random.randint(1,50)
        coms = random.randint(51,100)
        computers = graph2coms({i:{i, i - nets, i + nets} for i in range(coms)})
        result = solution(coms, computers)
        try:
            assert result == nets
            print('정답이 일치합니다')
        except:
            print('네트워크 수:',nets,'컴퓨터 수:',coms,'오답:',result)
