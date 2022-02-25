import psycopg2

host = 'learnde.cduaw970ssvt.ap-northeast-2.redshift.amazonaws.com'
port = '5439'
user = 'kyunghyun7843'
password = 'Kyunghyun7843!1'
dbname = 'dev'

conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    dbname=dbname
)

cur = conn.cursor()

#사용자별로 처음과 마지막 채널 알아내기
ass_2 = """
    with fc as (
        select
        usc.userid, usc.channel, row_number() over(partition by usc.userid order by st.ts asc) num
        from raw_data.user_session_channel usc
        join raw_data.session_timestamp st 
        on usc.sessionid = st.sessionid
    ), lc as (
        select
        usc.userid, usc.channel, row_number() over(partition by usc.userid order by st.ts desc) num
        from raw_data.user_session_channel usc
        join raw_data.session_timestamp st 
        on usc.sessionid = st.sessionid
    )
    select fc.userid userid, fc.channel first_channel, lc.channel last_channel
    from fc
    join lc on fc.userid = lc.userid and fc.num = 1
    where lc.num = 1;
    """

#Gross Revenue가 가장 큰 UserID 10개 찾기
ass_3 = """
    select usc.userid, sum(st.amount) gross_revenue
    from raw_data.session_transaction st
    left join raw_data.user_session_channel usc 
    on st.sessionid = usc.sessionid
    group by usc.userid
    order by sum(st.amount) desc
    limit 10;
    """

#채널별 월 매출액 테이블 만들기
ass_4_drop = "drop table if exists kyunghyun7843.monthly_channel_transaction;"
ass_4_create = """
    create table kyunghyun7843.monthly_channel_transaction as
    select left(ts, 7) "year-month",
        usc.channel,
        count(distinct usc.userid) "uniqueUsers",
        count(case when st.amount > 0 then usc.userid end) "paidUsers",
        round(paidUsers*100/nullif(uniqueUsers,0),0) || '%' "conversionRate",
        sum(st.amount) "grossRevenue",
        sum(case when st.refunded is false then st.amount else 0 end) "netRevenue"
    from raw_data.user_session_channel usc
    left join raw_data.session_timestamp ts
    on usc.sessionid = ts.sessionid
    left join raw_data.session_transaction st
    on usc.sessionid = st.sessionid
    group by 1, 2;
    """

ass_4 = "select * from kyunghyun7843.monthly_channel_transaction;"

answer_list = [ass_2, ass_3, ass_4]

if __name__ == "__main__":
    for sql in answer_list:
        answer = cur.execute(sql).fetchall()
        #print(answer)