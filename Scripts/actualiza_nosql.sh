cd /home/wbarraza/Trabajo/SmartDB/Scripts

mariadb -h Ares -u monitor  --password='Emilita01' < actualiza_carga_tbl_nosql.sql  >> ../logs/actualiza_nosql.log
