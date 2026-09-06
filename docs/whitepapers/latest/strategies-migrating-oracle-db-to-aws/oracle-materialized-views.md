---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/oracle-materialized-views.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Oracle materialized views
<a name="oracle-materialized-views"></a>

 You can use [Oracle Database materialized views](https://docs.oracle.com/cd/E11882_01/server.112/e25554/basicmv.htm#DWHSG008) to migrate data to Oracle databases on AWS, for either Amazon RDS or Amazon EC2. This method is well suited for databases under 500 MB.

 Because materialized views are available only in Oracle Database Enterprise Edition, this method works only if Oracle Database Enterprise Edition is used for both the source database and the destination database. With materialized view replication, you can do a one-time migration of data to AWS while keeping the destination tables continuously in sync with the source. The result is a minimal downtime cut over. Replication occurs over a database link between the source and destination databases. For the initial load, you must do a full refresh so that all the data in the source tables gets moved to the destination tables.

**Important**
 Because the data is transferred over a database link, the source and destination databases must be able to connect to each other over SQL\*Net. If your network security design doesn’t allow such a connection, then you cannot use this method.

 Unlike the preceding method (the Oracle SQL Developer **Database Copy** function) in which you copy an entire database, for this method you must create a materialized view for each table that you want to migrate. This gives you the flexibility of selectively moving tables to the database in AWS. However, it also makes the process more cumbersome if you need to migrate a large number of tables. For this reason, this method is better suited for migrating a limited number of tables.

 For best results with this method, complete the following steps. Assume the source database user ID is `SourceUser` with password `PASS: `

1.  Create a new user in the Amazon RDS or Amazon EC2 database with sufficient privileges.

   ```
    Create user MV_DBLink_AWSUser identified by password
   ```

1.  Create a database link to the source database.

   ```
   CREATE DATABASE LINK SourceDB_lnk CONNECT TO SourceUser
   IDENTIFIED BY PASS USING
   '(description=(address=(protocol=tcp)	(host= crmdb.acmecorp.com)
   (port=1521)) (connect_data=(sid=ORCLCRM)))’
   ```

1.  Test the database link to make sure you can access the tables in the source database from the database in AWS through the database link.

   ```
    Select * from tab@ SourceDB_lnk
   ```

1.  Log in to the source database and create a materialized view log for each table that you want to migrate.

   ```
    CREATE MATERIALIZED VIEW LOG ON customers
   ```

1.  In the destination database in AWS, create materialized views for each table for which you set up a materialized view log in the source database.

   ```
   CREATE MATERIALIZED VIEW customer BUILD IMMEDIATE REFRESH
   FAST AS SELECT * FROM customer@ SourceDB_lnk
   ```
