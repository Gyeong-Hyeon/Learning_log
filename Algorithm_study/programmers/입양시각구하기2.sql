--문제링크: https://programmers.co.kr/learn/courses/30/lessons/59413

WITH RECURSIVE HOURS AS (
   select 0 as hour union all select hour + 1 from HOURS where hour < 23 )

SELECT h.hour AS HOUR, IFNULL(seq.COUNT, 0) AS COUNT
FROM HOURS AS h
LEFT OUTER JOIN (
    SELECT CAST(SUBSTR(datetime, 11, 3) AS UNSIGNED) AS hour, COUNT(animal_id) AS "COUNT"
    FROM Animal_outs
    GROUP BY HOUR) AS seq
ON h.hour = seq.hour
ORDER BY h.hour;