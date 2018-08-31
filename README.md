# IATI
TolaData to CSV (for IATI)
The main script "export_to_csv.py" can export data of an organisation from TolaData to a CSV File that can report against required IATI fields. This file can then be used to publish on IATI using a platform like [Aidstream](https://www.aidstream.org) to generate an IATI XML File needed for publishing.

In this version, the database connection is made to a localhost.

You need to install Postgres:
```bash
sudo apt-get install postgresql postgresql-contrib
service postgresql start
```
To connect to postgres:

```bash
sudo -u postgres psql
```

You are now connected to the Database Management System
You need to create your database and give all the access to the user you want:
```bash
CREATE DATABASE demo;
ALTER ROLE postgres WITH PASSWORD 'postgres'
GRANT ALL PRIVILEGES ON DATABASE demo TO 'postgres'
```
Now you need to go back to your session to dump the data:
```bash
pg_restore -c -U postgres -d demo -v SQL_Dump.tar -W
```
If you are getting an error, try to restart the postgres service : /etc/init.d/postgresql restart


To execute the file you just need to go to your terminal in the right repository and execute the main file and put an organisation name as parameter, example:
```bash
python3 export_to_csv TolaData
```

For production use, the main script needs to be pointed to a production database.

In a future version, the IATI Identifier also needs to be entered as a parameter.
A functionnality can be added where the user will specify one or many WFL1 to get all the WFL2 activities.
