---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-application-users-and-roles-in-aurora-postgresql-compatible.html
---

# Create application users and roles in Aurora PostgreSQL-Compatible
<a name="create-application-users-and-roles-in-aurora-postgresql-compatible"></a>

*Abhishek Verma, Amazon Web Services*

## Summary
<a name="create-application-users-and-roles-in-aurora-postgresql-compatible-summary"></a>

When you migrate to Amazon Aurora PostgreSQL-Compatible Edition, the database users and roles that exist on the source database must be created in the Aurora PostgreSQL-Compatible database. You can create the users and roles in Aurora PostgreSQL-Compatible by using two different approaches:
+ Use similar users and roles in the target as in the source database. In this approach, the data definition languages (DDLs) are extracted for users and roles from the source database. Then they are transformed and applied to the target Aurora PostgreSQL-Compatible database. For example, the blog post [Use SQL to map users, roles, and grants from Oracle to PostgreSQL](https://aws.amazon.com/blogs/database/use-sql-to-map-users-roles-and-grants-from-oracle-to-postgresql) covers using extraction from an Oracle source database engine.
+ Use standardized users and roles that are commonly used during development, administration, and for performing other related operations in the database. This includes read-only, read/write, development, administration, and deployment operations performed by the respective users.

This pattern contains the grants required for users and roles creation in Aurora PostgreSQL-Compatible required for the standardized users and roles approach. The user and role creation steps are aligned to the security policy of granting least privilege to the database users. The following table lists the users, their corresponding roles, and their details on the database.

|
|
| Users | Roles | Purpose |
| --- |--- |--- |
| `APP_read` | `APP_RO` | Used for read-only access on the schema `APP` |
| `APP_WRITE` | `APP_RW` | Used for the write and read operations on the schema `APP` |
| `APP_dev_user` | `APP_DEV` | Used for the development purpose on the schema `APP_DEV`, with read-only access on the schema `APP` |
| `Admin_User` | `rds_superuser` | Used for performing administrator operations on the database |
| `APP` | `APP_DEP` | Used for creating the objects under the `APP` schema and for deployment of objects in the `APP` schema |

## Prerequisites and limitations
<a name="create-application-users-and-roles-in-aurora-postgresql-compatible-prereqs"></a>

**Prerequisites **
+ An active Amazon Web Services (AWS) account
+ A PostgreSQL database, Amazon Aurora PostgreSQL-Compatible Edition database, or Amazon Relational Database Service (Amazon RDS) for PostgreSQL database

**Product versions**
+ All versions of PostgreSQL

## Architecture
<a name="create-application-users-and-roles-in-aurora-postgresql-compatible-architecture"></a>

**Source technology stack  **
+ Any database

**Target technology stack  **
+ Amazon Aurora PostgreSQL-Compatible

**Target architecture**

The following diagram shows user roles and the schema architecture in the Aurora PostgreSQL-Compatible database.

![User roles and schema architecture for the Aurora PostgreSQL-Comaptible database.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/80105a81-e3d1-4258-b3c1-77f3a5e78592/images/b95cb9bc-8bf7-47d1-92e7-66cfb37d7ce7.png)

**Automation and scale**

This pattern contains the users, roles, and schema creation script, which you can run multiple times without any impact to existing users of the source or target database.

## Tools
<a name="create-application-users-and-roles-in-aurora-postgresql-compatible-tools"></a>

**AWS services**
+ [Amazon Aurora PostgreSQL-Compatible Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html) is a fully managed, ACID-compliant relational database engine that helps you set up, operate, and scale PostgreSQL deployments.

**Other services**
+ [psql](https://www.postgresql.org/docs/current/app-psql.html) is a terminal-based front-end tool that is installed with every PostgreSQL Database installation. It has a command line interface for running SQL, PL-PGSQL, and operating system commands.
+ [pgAdmin](https://www.pgadmin.org/) is an open-source management tool for PostgreSQL. It provides a graphical interface that helps you create, maintain, and use database objects.

## Epics
<a name="create-application-users-and-roles-in-aurora-postgresql-compatible-epics"></a>

### Create the users and roles
<a name="create-the-users-and-roles"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the deployment user. | The deployment user `APP` will be used to create and modify the database objects during deployments. Use the following scripts to create the deployment user role `APP_DEP` in the schema `APP`. Validate access rights to make sure this user has only the privilege to create objects in the required schema `APP`.1. Connect to the admin user, and create the schema.<pre>CREATE SCHEMA APP;</pre><br />2. Create the user.<pre>CREATE USER APP WITH PASSWORD  <password> ;</pre><br />3. Create the role.<pre>CREATE ROLE APP_DEP ;<br />GRANT all on  schema APP to APP_DEP ;<br />GRANT USAGE ON SCHEMA APP to APP_DEP ;<br />GRANT connect on database <db_name>  to APP_DEP ;<br />GRANT APP_DEP to APP;</pre><br />4. To test the privileges, connect to `APP` and create the tables.<pre>set search_path to APP;<br />SET<br />CREATE TABLE test(id integer ) ;<br />CREATE TABLE</pre><br />5. Check the privileges.<pre>select schemaname  , tablename , tableowner    from pg_tables where tablename like 'test' ;<br />schemaname   | tablename |  tableowner <br />APP                  | test            | APP</pre> | DBA |
| Create the read-only user. | The read-only user `APP_read` will be used for performing the read-only operation in the schema `APP`. Use the following scripts to create the read-only user. Validate access rights to make sure that this user has privilege only to read the objects in the schema `APP` and for automatically granting read access for any new objects created in the schema `APP`.1. Create the user `APP_read`.<pre>create user APP_read ;<br />alter user APP_read with password 'your_password' ;</pre><br />2. Create the role.<pre>CREATE ROLE APP_ro ;<br />GRANT SELECT ON ALL TABLES IN SCHEMA  APP  TO  APP_RO   ;<br />GRANT USAGE ON SCHEMA  APP   TO APP_RO<br />GRANT CONNECT ON DATABASE  testdb  TO APP_RO ;<br />GRANT APP_RO TO APP_read;</pre><br />3. To test the privileges, log in using the `APP_read` user.<pre>set search_path to APP ;<br />create table test1( id integer) ;<br />ERROR:  permission denied for schema APP<br />LINE 1: create table test1( id integer) ;<br />insert into test values (34) ;<br />ERROR: permission denied for table test SQL state: 42501<br />select from test<br />no rows selected</pre> | DBA |
| Create the read/write user. | The read/write user `APP_WRITE` will be used to perform read and write operations on the schema `APP`. Use the following scripts to create the read/write user and grant it the `APP_RW` role. Validate access rights to make sure that this user has read and write privileges only on the objects in the schema `APP` and for automatically granting read and write access for any new object created in schema `APP`.1. Create the user.<pre>CREATE USER APP_WRITE ;<br />alter user APP_WRITE  with password 'your_password' ;</pre><br />2. Create the role.<pre>CREATE ROLE APP_RW;<br />GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA APP   TO APP_RW ;<br />GRANT CONNECT ON DATABASE postgres to APP_RW ;<br />GRANT USAGE ON SCHEMA APP to APP_RW ;<br />ALTER DEFAULT PRIVILEGES IN SCHEMA APP<br />GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO APP_RW ;<br />GRANT APP_RW to APP_WRITE</pre><br />3. To test the privileges, log in using the `APP_WRITE` user.<pre>SET SEARCH_PATH to APP;<br />CREATE TABLE test1( id integer) ;<br />ERROR:   permission denied for schema APP<br />LINE 1: create table test1( id integer) ;<br />SELECT * FROM test ;<br />id <br />----<br />12<br />INSERT INTO test values (31) ;<br />INSERT 0 1</pre> |  |
| Create the admin user. | The admin user `Admin_User` will be used to perform admin operations on the database. Examples of these operations are `CREATE ROLE` and `CREATE DATABASE`. `Admin_User` uses the built-in role `rds_superuser` to perform admin operations on the database. Use the following scripts to create and test the privilege for the admin user `Admin_User` in the database.1. Create the user and grant the role.<pre>create user Admin_User WITH PASSWORD   ‘Your password’<br />ALTER user Admin_user CREATEDB;<br />ALTER user Admin_user CREATEROLE;</pre><br />2. To test the privilege, log in from the `Admin_User` user.<pre>SELECT * FROM APP.test ;<br />  id<br />  ----<br />   31<br />CREATE ROLE TEST ;<br />CREATE DATABASE test123 ;</pre> | DBA |
| Create the development user. | The development user `APP_dev_user` will have rights to create the objects in its local schema `APP_DEV` and read access in the schema `APP`. Use the following scripts to create and test the privileges of the user `APP_dev_user` in the database.1. Create the user.<pre>CREATE USER APP1_dev_user with password ‘your password’;</pre><br />2. Create the `APP_DEV` schema for the `App_dev_user`.<pre>CREATE SCHEMA APP1_DEV ;</pre><br />3. Create the `APP_DEV` role.<pre>CREATE ROLE APP1_DEV ;<br />GRANT   APP1_RO to APP1_DEV ;<br />GRANT SELECT ON ALL TABLES IN SCHEMA APP1_DEV to APP1_dev_user<br />GRANT USAGE, CREATE ON SCHEMA APP1_DEV to APP1_DEV_USER<br />GRANT APP1_DEV  to APP1_DEV_USER ;</pre><br />4. To test the privileges, log in from `APP_dev_user`.<pre>CREATE TABLE APP1_dev.test1( id integer ) ;<br />CREATE TABLE<br />INSERT into APP1_dev.test1 ( select * from APP1.test );<br />INSERT 0 1<br />CREATE TABLE APP1.test4 ( id int) ;<br />ERROR:   permission denied for schema APP1<br />LINE 1: create table APP1.test4 ( id int) ;</pre> | DBA |

## Related resources
<a name="create-application-users-and-roles-in-aurora-postgresql-compatible-resources"></a>

**PostgreSQL documentation**
+ [CREATE ROLE](https://www.postgresql.org/docs/9.1/sql-createrole.html)
+ [CREATE USER](https://www.postgresql.org/docs/8.0/sql-createuser.html)
+ [Predefined Roles](https://www.postgresql.org/docs/14/predefined-roles.html)

## Additional information
<a name="create-application-users-and-roles-in-aurora-postgresql-compatible-additional"></a>

**PostgreSQL 14 enhancement**

PostgreSQL 14 provides a set of predefined roles that give access to certain commonly needed, privileged capabilities and information. Administrators (including roles that have the `CREATE ROLE` privilege) can grant these roles or other roles in their environment to users, providing them with access to the specified capabilities and information.

Administrators can grant users access to these roles using the `GRANT` command. For example, to grant the `pg_signal_backend` role to `Admin_User`, you can run the following command.

```
GRANT pg_signal_backend TO Admin_User;
```

The `pg_signal_backend` role is intended to allow administrators to enable trusted, non-superuser roles to send signals to other backends. For more information, see [PostgreSQL 14 enhancement](https://www.postgresql.org/docs/14/predefined-roles.html).

**Fine-tuning access**

In some cases, it might be necessary to provide more granular access to the users (for example, table-based access or column-based access). In such cases, additional roles can be created to grant those privileges to the users. For more information, see [PostgreSQL Grants](https://www.postgresql.org/docs/8.4/sql-grant.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
