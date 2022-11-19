use SmartDB
;
CREATE TEMPORARY TABLE IF NOT EXISTS tbl_mdb_p001_temporary AS (SELECT * FROM tbl_mdb_p001 a where a.fecha = (select max(b.fecha) from tbl_mdb_p001 b) );

insert into tbl_mdb_p001H()
select * from tbl_mdb_p001
;
truncate table tbl_mdb_p001;
insert into tbl_mdb_p001 () 
select * from tbl_mdb_p001_temporary;
commit;

CREATE TEMPORARY TABLE IF NOT EXISTS tbl_mdb_p002_temporary AS (SELECT * FROM tbl_mdb_p002 a where a.fecha = (select max(b.fecha) from tbl_mdb_p002 b) );

insert into tbl_mdb_p002H()
select * from tbl_mdb_p002
;
truncate table tbl_mdb_p002;
insert into tbl_mdb_p002 
select * from tbl_mdb_p002_temporary;
commit;

CREATE TEMPORARY TABLE IF NOT EXISTS tbl_mdb_p003_temporary AS (SELECT * FROM tbl_mdb_p003 a where a.fecha = (select max(b.fecha) from tbl_mdb_p003 b) )
;
insert into tbl_mdb_p003H()
select * from tbl_mdb_p003
;
truncate table tbl_mdb_p003;
insert into tbl_mdb_p003 
select * from tbl_mdb_p003_temporary;
commit;

CREATE TEMPORARY TABLE IF NOT EXISTS tbl_mdb_p004_temporary AS (SELECT * FROM tbl_mdb_p004 a where a.fecha = (select max(b.fecha) from tbl_mdb_p004 b) )
;
insert into tbl_mdb_p004H()
select * from tbl_mdb_p004
;
truncate table tbl_mdb_p004;
insert into tbl_mdb_p004 
select * from tbl_mdb_p004_temporary;
commit;
