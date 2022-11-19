use SmartDB
;
CREATE TEMPORARY TABLE IF NOT EXISTS tbl_redis_p001_temporary AS (SELECT * FROM tbl_redis_p001 a where a.fecha = (select max(b.fecha) from tbl_redis_p001 b) );

insert into tbl_redis_p001H()
select * from tbl_redis_p001
;
truncate table tbl_redis_p001;
insert into tbl_redis_p001 ()
select * from tbl_redis_p001_temporary;
commit;
