# Write your MySQL query statement below

delete from Person where id in (
select id from (
select 
id, email, RANK() over ( partition by email order by id asc) as r 
from Person ) a
where r!=1
    )
