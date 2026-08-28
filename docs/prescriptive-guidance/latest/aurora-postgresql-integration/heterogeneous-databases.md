---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-postgresql-integration/heterogeneous-databases.html
---

# Aurora PostgreSQL-Compatible integration with heterogeneous databases
<a name="heterogeneous-databases"></a>

To integrate Aurora PostgreSQL-Compatible with remote SQL Server databases, use the Tabular Data Stream foreign data wrapper (`tds_fdw`) extension. By using the `tds_fdw` extension, you can implement federated query capability to interact with any remote SQL Server based database, both on premises and managed or self-managed on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html). The `tds_fdw` extension is available in all currently supported versions of Amazon RDS for PostgreSQL and Aurora PostgreSQL-Compatible.

## tds\_fdw use cases and high-level steps
<a name="tds-fdw"></a>

Integrating Aurora PostgreSQL-Compatible with heterogeneous databases such as SQL Server supports the following use cases:
+ **Hybrid architectures** ‒ Your organization might have existing SQL Server databases that must coexist and integrate with Aurora PostgreSQL-Compatible. In such cases, Aurora PostgreSQL-Compatible can be part of a hybrid architecture, where it interacts with the heterogeneous databases to exchange data or perform specific operations. With this integration, your organization can use the strengths of different database platforms while maintaining your existing investments.
+ **Reporting and analytics** ‒ You can use Aurora PostgreSQL-Compatible as a reporting or analytics database. You can consolidate data from multiple sources, including Oracle and SQL Server databases. This use case is common in scenarios where organizations want to create specialized reporting databases or data marts tailored to specific business units or use cases.

To configure the `tds_fwd` extension in Aurora PostgreSQL-Compatible, use the following high-level steps:

1. Connect to your Aurora PostgreSQL-Compatible cluster by using a PostgreSQL client, and create the `tds_fdw` extension:

   ```
   CREATE EXTENSION tds_fdw;
   ```

   This extension provides the functionality to access and query data from remote SQL Server databases as if they were local tables.

1. Create a server object that represents the remote SQL Server or TDS-compatible database that you want to connect to.

1. Ensure that the necessary security groups and network configurations are in place to allow Aurora PostgreSQL-Compatible to connect to the remote SQL Server database.

   If the remote database is hosted on premises, you might need to configure a VPN or AWS Direct Connect connection.

   Run the following command:

   ```
   CREATE SERVER my_remote_sql_server
       FOREIGN DATA WRAPPER tds_fdw
       OPTIONS (
           servername 'your_server_name',
           port '1433',
           instance 'your_instance_name'
       );
   ```

1. Define a user mapping that maps an Aurora PostgreSQL-Compatible user to a user on the remote SQL Server or TDS-compatible database:

   ```
   CREATE USER MAPPING FOR postgres
       SERVER my_remote_sql_server
       OPTIONS (
           username 'your_sql_server_username',
           password 'your_sql_server_password'
       );
   ```

1. Create a foreign table that represents a table or view in the remote SQL Server or TDS-compatible database:

   ```
   CREATE FOREIGN TABLE sql_server_table (
       column1 INTEGER,
       column2 VARCHAR(50)
   ) SERVER my_remote_sql_server
       OPTIONS (
           schema_name 'your_schema_name',
           table_name 'your_table_name'
       );
   ```

1. Create a foreign table based on the SQL query:

   ```
   CREATE FOREIGN TABLE mssql_people ( empno INT NOT NULL , ename VARCHAR(10) NULL, dept INT) SERVER my_remote_sql_server OPTIONS (  query 'SELECT empno, ename, dept FROM dbo.emp');
   ```

1. Query the foreign table as you would query any other table in Aurora PostgreSQL-Compatible:

   ```
   SELECT * FROM sql_server_table;
   SELECT * FROM mssql_people; -- Query based on table
   ```

1. Import the table from SQL Server to PostgreSQL:

   ```
   IMPORT FOREIGN SCHEMA dbo LIMIT TO (emp) FROM SERVER my_remote_sql_server INTO public_fdw;
   ```

1. To validate the query plan, run `EXPLAIN SELECT`:

   ```
   EXPLAIN SELECT * FROM mssql_people;
   ```

**Note**
Data Manipulation Language (DML) operations are not available through the `tds_fdw` extension. The system doesn't support performing DML operations across different database engines. `INSERT`, `DELETE`, `UPDATE`, and `TRUNCATE TABLE` will not be successful on the remote SQL server.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
