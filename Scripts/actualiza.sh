cd /home/wbarraza/Trabajo/SmartDB/Scripts

mariadb -h Ares -u monitor  --password='Emilita01' < actualiza_carga_tbl.sql  >> ../logs/actualiza.log
