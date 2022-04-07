--Table name: Employee
--id: int, PK
--salary: int
--두 번째로 높은 연봉 출력. 두 번째로 높은 연봉이 없으면 null 출력

SELECT
    (CASE WHEN (SELECT count(DISTINCT salary) FROM Employee) < 2 THEN null
     ELSE (SELECT DISTINCT salary FROM Employee ORDER BY salary DESC LIMIT 1,1)            
     END) AS SecondHighestSalary;