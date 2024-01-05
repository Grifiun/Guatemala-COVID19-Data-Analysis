copy file to docker "sql_server_container" to "/home/"
```bash
    docker cp /home/denilson/Documents/Proyectos/SS2_Proyecto_Fase_1/scripts/ss2-sql-server-express-2019.sql sql_server_container:/home/ 
```
Then execute in docker "sql_server_container"
```bash
    /opt/mssql-tools/bin/sqlcmd -S host -U SA -P 'password' -d master -i /home/ss2-sql-server-express-2019.sql
```