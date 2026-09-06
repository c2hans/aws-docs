---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-postgresql-integration/remote-postgresql-databases.html
---

# Aurora PostgreSQL-Compatible integration with remote PostgreSQL databases
<a name="remote-postgresql-databases"></a>

This section discusses Amazon Aurora PostgreSQL-Compatible Edition integration with remote PostgreSQL databases using the `postgres_fdw` (foreign-data wrapper) extension or the `dblink` feature. The `postgres_fdw` module provides federated query capability for interacting with remote PostgreSQL-based databases. The remote databases can be managed or self-managed on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) or on premises. The `postgres_fdw` extension is available in all currently supported versions of Amazon Relational Database Service (Amazon RDS) for PostgreSQL and Aurora PostgreSQL-Compatible.

Using the `postgres_fdw` extension,  you can access and query data from remote PostgreSQL databases as if they were local tables. The `postgres_fdw` extension also supports the following:
+ Cross-version compatibility for accessing data from external PostgreSQL servers that are running different versions.
+ Transaction management, which helps to ensure data consistency and integrity when you perform operations across local and external PostgreSQL servers.
+ Distributed transactions, which provide atomicity (a property of ACID transactions) and isolation guarantees when you perform operations across multiple external PostgreSQL servers. This helps ensure that either all operations in a transaction are committed or none are committed, maintaining data consistency and integrity.

Although the `dblink` module provides a way to interact with remote PostgreSQL databases, it doesn't support distributed transactions or other advanced features. If you need more advanced functionality, consider using the `postgres_fdw` extension instead. The `postgres_fdw` extension provides more integration and optimization capabilities.

## postgres\_fdw use cases and high-level steps
<a name="postgres-fdw"></a>

The `postgres_fdw` extension usage with Aurora PostgreSQL-Compatible supports the following use cases and scenarios:
+ **Federated queries and data integration** ‒ Querying and combining data from multiple PostgreSQL databases within a single Aurora PostgreSQL-Compatible instance
+ **Offloading read workloads** ‒ Connecting to read replicas of external PostgreSQL servers, offloading read-heavy workloads, and improving query performance
+ **Cross-database operations** ‒ Performing `INSERT`, `UPDATE`, `DELETE`, and `COPY` operations across multiple PostgreSQL databases, enabling cross-database data manipulation and maintenance tasks

To configure `postgres_fdw`, use the following high-level steps:

1. Connect to your Aurora PostgreSQL-Compatible cluster by using a PostgreSQL client, and create the `postgres_fdw` extension:

   ```
   CREATE EXTENSION postgres_fdw;
   ```

   This extension provides the functionality to connect to remote PostgreSQL databases.

1. Create a foreign server named `my_fdw_target` by using the `CREATE SERVER` command. This server represents the remote PostgreSQL database that you want to connect to. Specify the database name, hostname, and SSL mode as options for this server.

1. Ensure that the necessary security groups and network configurations are in place to allow Aurora PostgreSQL-Compatible to connect to the remote PostgreSQL database.

   If the remote database is hosted on premises, you might need to configure a virtual private network (VPN) or AWS Direct Connect connection.

   Run the following command:

   ```
   CREATE SERVER my_fdw_target Foreign Data Wrapper postgres_fdw OPTIONS (DBNAME 'postgres', HOST 'SOURCE_HOSTNAME', SSLMODE 'require');
   ```

1. Create a user mapping for the `dbuser` user on the `my_fdw_target` server. This mapping associates the `dbuser` user and password on the local Aurora PostgreSQL-Compatible instance with the corresponding user on the remote database.

   ```
   CREATE USER MAPPING FOR dbuser SERVER my_fdw_target OPTIONS (user 'DBUSER', password 'PASSWORD');
   ```

   This step is necessary to authenticate and provide access to remote database.

1. Create a foreign table named `customer_fdw` with the `my_fdw_target` server and user mapping that you set up previously:

   ```
   CREATE FOREIGN TABLE customer_fdw( id int, name varchar, emailid varchar, projectname varchar, contactnumber bigint) server my_fdw_target OPTIONS( TABLE_NAME 'customers');
   ```

   The `customer_fdw` table maps to the `customers` table in the remote database specified by the `my_fdw_target` server. The foreign table has the same structure as the remote table so that you can interact with the remote data as if it were a local table.

1. You can perform various data manipulation operations on the `customer_fdw` foreign table, such as `INSERT`, `UPDATE`, and `SELECT` queries. The script demonstrates inserting a new row and updating an existing row, deleting a record, and truncating a table in the remote `customers` table through the `customer_fdw` foreign table:

   ```
   INSERT INTO customer_fdw values ( 1, 'Test1', 'Test1@email.com', 'LMS1', '888888888');
   INSERT INTO customer_fdw values ( 2, 'Test2', 'Test2@email.com', 'LMS2', '999999999');
   INSERT INTO customer_fdw values ( 3, 'Test3', 'Test3@email.com', 'LMS3', '111111111');
   UPDATE customer_fdw set contactnumber = '123456789' where id = 2;
   DELETE FROM customer_fdw where id = 1;
   TRUNCATE TABLE customer_fdw;
   ```

1. You can validate an SQL query plan by using the `EXPLAIN` statement to analyze the query plan for a `SELECT` query on the `customer_fdw` table:

   ```
   EXPLAIN select * from customer_fdw where id =1;
   ```

   This can help you understand how the query is being run and how to optimize it. For more information about using the `EXPLAIN` statement, see [Optimizing PostgreSQL query performance](https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-query-tuning/introduction.html) in AWS Prescriptive Guidance.

1. To import multiple tables from the remote database into a local schema, use the `IMPORT FOREIGN SCHEMA` command:

   ```
   CREATE SCHEMA public_fdw;
   IMPORT FOREIGN SCHEMA public LIMIT TO (employees, departments)
       FROM SERVER my_fdw_target INTO public_fdw;
   ```

   This creates local foreign tables for specified tables in the `public_fdw` schema. In this example, the specific tables are employees and departments.

1. To grant the necessary permissions to a specific database user so that they can access and use the FDW and the associated foreign server, run the following commands:

   ```
   GRANT USAGE ON FOREIGN SERVER my_fdw_target TO targetdbuser;
   GRANT USAGE ON FOREIGN DATA WRAPPER postgres_fdw TO targetdbuser;
   ```

   This step can be beneficial when multiple users require access to the foreign tables facilitated by the foreign data wrapper.

When using foreign tables, be aware of the following limitations:
+ Accessing data from a remote source can introduce data transfer costs and performance overhead caused by network latency. Performance issues can be noticeable for large data sets or queries that require significant data transfer between the Aurora PostgreSQL-Compatible instance and the remote data source.
+ In complex queries that involve features such as window functions, recursive queries might not work as expected or might not be supported.
+ Currently, password encryption is not supported. Implement controls to ensure that only authorized users can access the FDWs and retrieve data from remote databases.
+ Primary key constraints can't be defined on foreign tables, as demonstrated by the following table-creation script attempt:

  ```
  CREATE FOREIGN TABLE customer_fdw2( id int primary key, name varchar, emailid varchar, projectname varchar, contactnumber bigint) server my_fdw_target OPTIONS( TABLE_NAME 'customers');
  Primary keys cannot be defined on Foreign table
  ```
+ The `ON CONFLICT` clause for `INSERT` statements isn't supported on foreign tables, as shown in the following example:

  ```
  INSERT INTO customer_fdw (id, name, emailid, projectname, contactnumber) VALUES
  (1, 'test1', 'test@email.com', 'LMS', 11111111 ),
  (3, 'test3', 'test3@email.com', 'LMS', 22222222 )
  ON CONFLICT (id) DO UPDATE
  SET name = EXCLUDED.name;
  On Conflict option doesnot work.
  ```

### Cleanup
<a name="cleanup.047e1775-387f-5344-b0b6-a2f3c5830c14"></a>

To clean up the created objects, including dropping the `postgres_fdw` extension, the `my_fdw_target` server, user mappings, and foreign tables, run the following commands:

```
DROP FOREIGN TABLE customer_fdw;
DROP USER MAPPING for postgres;
DROP SERVER  my_fdw_target;
DROP EXTENSION postgres_fdw cascade;
```

## Using dblink to create connections
<a name="dblink"></a>

The `dblink` module functions provide an alternative way to create connections and run SQL statements on remote PostgreSQL databases. The `dblink` solution is a simpler and more flexible way to run one-time queries or operations on remote databases. For more complex scenarios that involve large-scale data integration, performance optimization, and data-integrity requirements, we recommend using `postgres_fdw`.

Using `dblink` involves the following high-level steps:

1. Create the `dblink` extension:

   ```
   CREATE EXTENSION dblink;
   ```

   This extension provides the functionality to connect to remote PostgreSQL databases.

1. To establish a connection to a remote PostgreSQL database, use the `dblink_connect` function:

   ```
   SELECT dblink_connect('myconn', 'dbname=postgres port=5432 host=SOURCE_HOSTNAME user=postgres password=postgres');
   ```

1. After you connect to the remote PostgreSQL database, run SQL statements on the remote database by using `dblink` functions:

   ```
   SELECT  FROM dblink('myconn', 'SELECT col1, col2 FROM remote_table') AS remote_data(col1 int, col2 text);
   ```

   This query runs the `SELECT * FROM remote_table` statement on the remote database by using the `myconn` connection. The query retrieves the results into a local temporary table with columns `col1` and `col2`.

1. You can also run non-query statements, such as `INSERT`, `UPDATE`, or `DELETE`, on the remote database by using the `dblink_exec` function:

   ```
   SELECT dblink_exec('myconn', 'INSERT INTO remote_table VALUES (1, ''value'')');
   ```
