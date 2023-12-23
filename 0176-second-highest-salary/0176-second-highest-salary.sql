# Write your MySQL query statement below

select coalesce(
    (select salary from 
     (select id, salary, DENSE_RANK() over ( ORDER BY salary desc) as rn from Employee ) a      where rn=2 limit 1)
    , null) as SecondHighestSalary
    