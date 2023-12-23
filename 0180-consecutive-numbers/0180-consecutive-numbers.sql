# Write your MySQL query statement below

select distinct num as ConsecutiveNums from (
select id, num , lead(num,1) over(order by id) as nxt1 ,
lead(num,2) over(order by id) as nxt2
from Logs
    ) a where num=nxt1 and nxt1=nxt2