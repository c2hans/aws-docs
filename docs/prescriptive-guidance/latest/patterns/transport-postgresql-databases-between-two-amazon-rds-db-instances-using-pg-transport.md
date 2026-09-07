---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/transport-postgresql-databases-between-two-amazon-rds-db-instances-using-pg-transport.html
---

# Transport PostgreSQL databases between two Amazon RDS DB instances using pg\_transport
<a name="transport-postgresql-databases-between-two-amazon-rds-db-instances-using-pg-transport"></a>

*Raunak Rishabh and Jitender Kumar, Amazon Web Services*

## Summary
<a name="transport-postgresql-databases-between-two-amazon-rds-db-instances-using-pg-transport-summary"></a>

This pattern describes the steps for migrating extremely large databases between two Amazon Relational Database Service (Amazon RDS) for PostgreSQL DB instances by using the **pg\_transport** extension. This extension provides a physical transport mechanism to move each database. By streaming the database files with minimal processing, it provides an extremely fast method for migrating large databases between DB instances with minimal downtime. This extension uses a pull model where the target DB instance imports the database from the source DB instance.

## Prerequisites and limitations
<a name="transport-postgresql-databases-between-two-amazon-rds-db-instances-using-pg-transport-prereqs"></a>

**Prerequisites **
+ Both DB instances must run the same major version of PostgreSQL.
+ The database must not exist on the target. Otherwise, the transport fails.
+ No extension other than **pg\_transport** must be enabled in the source database.
+ All source database objects must be in the default **pg\_default** tablespace.
+ The security group of the source DB instance should allow traffic from the target DB instance.
+ Install a PostgreSQL client like [psql](https://www.postgresql.org/docs/11/app-psql.html) or [PgAdmin](https://www.pgadmin.org/) to work with the Amazon RDS PostgreSQL DB instance. You can install the client either in your local system or use an Amazon Elastic Compute Cloud (Amazon EC2) instance. In this pattern, we use psql on an EC2 instance.

**Limitations **
+ You can't transport databases between different major versions of Amazon RDS for PostgreSQL.
+ The access privileges and ownership from the source database are not transferred to the target database.
+ You can't transport databases on read replicas or on parent instances of read replicas.
+ You can't use **reg** data types in any database tables that you plan to transport with this method.
+ You can run up to 32 total transports (including both imports and exports) at the same time on a DB instance.
+ You cannot rename or include/exclude tables. Everything is migrated as is.

**Caution**
+ Make backups before removing the extension, because removing the extension also removes dependent objects and some data that's critical to the operation of the database.
+ Consider the instance class and processes running on other databases on the source instance when you determine the number of workers and `work_mem` values for **pg\_transport**.
+ When the transport starts, all connections on the source database are ended and the database is put into read-only mode.

**Note**
When the transport is running on one database, it doesn’t affect other databases on the same server.** **

**Product versions**
+ Amazon RDS for PostgreSQL 10.10 and later, and Amazon RDS for PostgreSQL 11.5 and later. For the latest version information, see [Transporting PostgreSQL Databases Between DB Instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.TransportableDB.html) in the Amazon RDS documentation.

## Architecture
<a name="transport-postgresql-databases-between-two-amazon-rds-db-instances-using-pg-transport-architecture"></a>

![Transporting PostgreSQL databases between Amazon RDS DB instances](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d5fb7ea3-32b7-4602-b382-3cf5c075c7c9/images/aec4d8d2-37a8-4136-9042-f9667ac4aebb.png)

## Tools
<a name="transport-postgresql-databases-between-two-amazon-rds-db-instances-using-pg-transport-tools"></a>
+ **pg\_transport** provides a physical transport mechanism to move each database. By streaming the database files with minimal processing, physical transport moves data much faster than traditional dump and load processes and requires minimal downtime. PostgreSQL transportable databases use a pull model where the destination DB instance imports the database from the source DB instance. You install this extension on your DB instances when you prepare the source and target environments, as explained in this pattern.
+ [psql](https://www.postgresql.org/docs/11/app-psql.html) enables you to connect to, and work with, your PostgreSQL DB instances. To install **psql** on your system, see the [PostgreSQL Downloads](https://www.postgresql.org/download/) page.

## Epics
<a name="transport-postgresql-databases-between-two-amazon-rds-db-instances-using-pg-transport-epics"></a>

### Create the target parameter group
<a name="create-the-target-parameter-group"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a parameter group for the target system. | Specify a group name that identifies it as a target parameter group; for example, `pgtarget-param-group`. For instructions, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithDBInstanceParamGroups.html#USER_WorkingWithParamGroups.Creating). | DBA |
| Modify the parameters for the parameter group. | Set the following parameters:1. Add `pg_transport` to the `shared_preload_libraries` parameter.<pre>shared_preload_libraries = pg_stat_statements, pg_transport</pre><br />2. Set the `pg_transport.num_workers` parameter. Choose the number of workers you want to run the transport with. The value you set determines the number of `transport.send_file` workers that will be created in the source.<br />3. Increase the the value of `max_worker_processes` to more than three times the value of `pg_transport.num_workers`. For example, if you set the value of `pg_transport.num_workers` to 4, the `max_worker_processes` value should be at least 13. If this fails, **pg\_transport** recommends a minimum value. <br />4. Set `pg_transport.timing` to 1. This setting enables the reporting of timing information during the transport.<br />5. Set the `pg_transport.work_mem` parameter. This parameter specifies the maximum memory to allocate to each worker. The default value is 128 MB.<br />For more information about these parameters, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.TransportableDB.html). | DBA |

### Create the source parameter group
<a name="create-the-source-parameter-group"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a parameter group for the source system. | Specify a group name that identifies it as a source parameter group; for example, `pgsource-param-group`. For instructions, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithDBInstanceParamGroups.html#USER_WorkingWithParamGroups.Creating). | DBA |
| Modify the parameters for the parameter group. | Set the following parameters:1. Add `pg_transport` to the `shared_preload_libraries` parameter.<pre>shared_preload_libraries = pg_stat_statements, pg_transport</pre><br />2. Set the `pg_transport.num_workers` parameter. The value of this parameter defined in the target determines the number of `transport.send_file` workers to be used. If you have an import running on this instance, increase this value, but consider the number of workers that are already running.<br />3. Increase the the value of `max_worker_processes` to more than three times the value of `pg_transport.num_workers` on the target. For example, if you set the value of `pg_transport.num_workers` to 4 on the target, the `max_worker_processes` value on the source should be at least 13. If this fails, **pg\_transport** recommends a minimum value. <br />4. Set the `pg_transport.work_mem` parameter. This parameter specifies the maximum memory to allocate to each worker. The default value is 128 MB.<br />For more information about these parameters, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.TransportableDB.html). | DBA |

### Prepare the target environment
<a name="prepare-the-target-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a new Amazon RDS for PostgreSQL DB instance to transport your source database to. | Determine the instance class and PostgreSQL version based on your business requirements. | DBA, Systems administrator, Database architect |
| Modify the security group of the target to allow connections on the DB instance port from the EC2 instance. | By default, the port for the PostgreSQL instance is 5432. If you're using another port, connections to that port must be open for the EC2 instance. | DBA, Systems administrator |
| Modify the instance, and assign the new target parameter group. | For example, `pgtarget-param-group`. | DBA |
| Restart the target Amazon RDS DB instance.  | The parameters `shared_preload_libraries` and `max_worker_processes` are static parameters and require a reboot of the instance. | DBA, Systems administrator |
| Connect to the database from the EC2 instance using psql. | Use the command: <pre>psql -h <rds_end_point> -p PORT -U username -d database -W</pre> | DBA |
| Create the pg\_transport extension. | Run the following query as a user with the `rds_superuser` role:<pre>create extension pg_transport;</pre> | DBA |

### Prepare the source environment
<a name="prepare-the-source-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify the security group of the source to allow connections on the DB instance port from the Amazon EC2 instance and target DB instance | By default, the port for PostgreSQL instance is 5432. If you're using another port, connections to that port must be open for the EC2 instance. | DBA, Systems administrator |
| Modify the instance and assign the new source parameter group. | For example, `pgsource-param-group`. | DBA |
| Restart the source Amazon RDS DB instance.  | The parameters `shared_preload_libraries` and `max_worker_processes` are static parameters and require a reboot of the instance. | DBA |
| Connect to the database from the EC2 instance using psql. | Use the command: <pre>psql -h <rds_end_point> -p PORT -U username -d database -W</pre> | DBA |
| Create the pg\_transport extension and remove all other extensions from the databases to be transported. | The transport will fail if there are any extensions other than **pg\_transport** installed on the source database. This command must by run by a user with the `rds_superuser` role. | DBA |

### Perform the transport
<a name="perform-the-transport"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Perform a dry run. | Use the `transport.import_from_server` function to perform a dry run first:<pre>SELECT transport.import_from_server( 'source-db-instance-endpoint', source-db-instance-port, 'source-db-instance-user', 'source-user-password', 'source-database-name', 'destination-user-password', 'true');</pre><br />The last parameter of this function (set to `true`) defines the dry run. <br />This function displays any errors that you would see when you run the main transport. Resolve the errors before you run the main transport.  | DBA |
| If the dry run is successful, initiate the database transport. | Run the `transport.import_from_server` function to perform the transport. It connects to the source and imports the data. <pre>SELECT transport.import_from_server( 'source-db-instance-endpoint', source-db-instance-port, 'source-db-instance-user', 'source-user-password', 'source-database-name', 'destination-user-password', false);</pre><br />The last parameter of this function (set to `false`) indicates that this isn’t a dry run. | DBA |
| Perform post-transport steps. | After the database transport is complete:+ Validate the data in the target environment.<br />+ Add all the roles and permissions to the target.<br />+ Enable all required extensions in the target and source, if required.<br />+ Revert the value of the `max_worker_processes` parameter. | DBA |

## Related resources
<a name="transport-postgresql-databases-between-two-amazon-rds-db-instances-using-pg-transport-resources"></a>
+ [Amazon RDS documentation](https://docs.aws.amazon.com/rds/)
+ [pg\_transport documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Procedural.Importing.html#PostgreSQL.TransportableDB.Setup)
+ [Migrating databases using RDS PostgreSQL Transportable Databases](https://aws.amazon.com/blogs/database/migrating-databases-using-rds-postgresql-transportable-databases/) (blog post)
+ [PostgreSQL downloads](https://www.postgresql.org/download/linux/redhat/)
+ [psql utility](https://www.postgresql.org/docs/11/app-psql.html)
+ [Creating a DB Parameter Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html#USER_WorkingWithParamGroups.Creating)
+ [Modify Parameters in a DB Parameter Group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html#USER_WorkingWithParamGroups.Modifying)
+ [PostgreSQL downloads](https://www.postgresql.org/download/)
