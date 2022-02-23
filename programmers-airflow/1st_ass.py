import sqlite3

conn = sqlite3.connect(':memory:')
cur = conn.cursor()

user_data = [
    (1, 779, 7, 'Instagram'),
    (2, 230, 9, 'Naver'),
    (3, 369, 10, 'Youtube'),
    (4, 248, 1, 'Naver'),
    (5, 676, 272, 'Instagram'),
    (6, 40, 8, 'Youtube'),
    (7, 468, 44, 'Instagram'),
    (8, 69, 35, 'Facebook'),
    (9, 38, 22, 'Facebook')
]
time_data = [
    (1, 7, '2019-05-01 0:36:00'),
    (2, 9, '2019-05-01 2:53:49'),
    (3, 10, '2019-05-01 12:18:27'),
    (4, 1, '2019-05-01 13:41:29'),
    (5, 272, '2019-05-01 14:17:54'),
    (6, 8, '2019-05-01 14:42:50'),
    (7, 44, '2019-05-01 15:08:16'),
    (8, 35, '2019-05-01 15:20:27'),
    (9, 22, '2019-06-01 15:20:27')
]


def insert_data(table_name, data):
    for row in data:
        cur.execute(f"INSERT INTO {table_name} VALUES {row};")
    
    conn.commit()
    return None

if __name__ == "__main__":
    cur.execute("""CREATE TABLE user_session_channel (
                    record INT PRIMARY KEY,
                    userId INT,
                    sessionId INT,
                    channel text
                    );""")

    cur.execute("""CREATE TABLE session_timestamp (
                    record INT PRIMARY KEY,
                    sessionId INT,
                    timestamp DATETIME
                    );""")
    
    insert_data('user_session_channel', user_data)
    insert_data('session_timestamp', time_data)

    #월별 사용자를 카운트하는 쿼리입니다.
    answer = cur.execute("""SELECT STRFTIME('%Y-%m',substr(s."timestamp",0,instr(s."timestamp",' '))) as month,
	                        COUNT(DISTINCT(u.userId)) as MAU
                            FROM user_session_channel u, session_timestamp s
                            WHERE u.sessionId  == s.sessionId
                            GROUP BY STRFTIME('%Y-%m',substr(s."timestamp",0,instr(s."timestamp",' ')));
                        """).fetchall()
    print(answer)
    
    # #그룹을 맞게 뽑았는지 확인합니다.
    # session_hist = dict()
    # for time in time_data:
    #     group = time[2][:7]
    #     if session_hist.get(group):
    #         session_hist[group] = session_hist[group].append(time[1])
    #         continue
    #     session_hist[group] = [time[1]]

    # join_table = dict()
    # for user in user_data:
    #     for date in session_hist.keys():
    #         if user[2] not in session_hist[date]:
    #             continue
    #         try:
    #             join_table[date].append(user[2])
    #         except KeyError:
    #             join_table[date] = [user[2]]
    
    # correct_ans = list()
    # for group in join_table.keys():
    #     correct_ans.append((group, len(set(join_table[group]))))

    # assert answer == correct_ans
