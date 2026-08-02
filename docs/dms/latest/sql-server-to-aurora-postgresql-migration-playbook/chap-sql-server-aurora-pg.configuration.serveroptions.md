---
source_url: https://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/chap-sql-server-aurora-pg.configuration.serveroptions.html
---

# Configuring server options
<a name="chap-sql-server-aurora-pg.configuration.serveroptions"></a>

This topic provides reference information about parameter configuration in SQL Server and PostgreSQL, specifically in the context of migrating from SQL Server 2019 to Amazon Aurora PostgreSQL. You can understand the differences in how server-level settings and parameters are managed between these two database systems.

| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences |
| --- | --- | --- | --- |
|  ![One star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-1.png)  | N/A | N/A | Use Cluster and Database/Cluster Parameter. |

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.configuration.serveroptions.sqlserver"></a>

SQL Server provides server-level settings that affect all databases and all sessions. You can modify these settings using the `sp_configure` system stored procedure.

You can use server options to perform the following configuration tasks:
+ Define hardware utilization such as memory management, affinity mask, priority boost, network packet size, and soft Non-Uniform Memory Access (NUMA).
+ Alter run time global values such as recovery interval, remote login timeout, optimization for ad-hoc workloads, and cost threshold for parallelism.
+ Enable and disable global features such as C2 Audit, OLE, procedures, CLR procedures, and allow trigger recursion.
+ Configure global security settings such as server authentication mode, remote access, shell access with `xp_cmdshell`, CLR access level, and database chaining.
+ Set default values for sessions such as user options, default language, backup compression, and fill factor.

Some settings require an explicit `RECONFIGURE` command to apply the changes to the server. High risk settings require `RECONFIGURE WITH OVERRIDE` for the changes to be applied. Some advanced options are hidden by default. To view and modify these settings, set `show advanced options` to 1 and run `sp_configure`.

**Note**
Server audits are managed with the T-SQL commands `CREATE` and `ALTER SERVER AUDIT`.

### Syntax
<a name="chap-sql-server-aurora-pg.configuration.serveroptions.sqlserver.syntax"></a>

```
EXECUTE sp_configure <option>, <value>;
```

### Examples
<a name="chap-sql-server-aurora-pg.configuration.serveroptions.sqlserver.examples"></a>

Limit server memory usage to 4 GB.

```
EXECUTE sp_configure 'show advanced options', 1;
```

```
RECONFIGURE;
```

```
sp_configure 'max server memory', 4096;
```

```
RECONFIGURE;
```

Allow command shell access from T-SQL.

```
EXEC sp_configure 'show advanced options', 1;
```

```
RECONFIGURE;
```

```
EXEC sp_configure 'xp_cmdshell', 1;
```

```
RECONFIGURE;
```

View the current values.

```
EXECUTE sp_configure
```

For more information, see [Server Configuration Options (SQL Server)](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/server-configuration-options-sql-server?view=sql-server-ver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.configuration.serveroptions.pg"></a>

When running PostgreSQL databases as Amazon Aurora Clusters, Parameter Groups are used to change to cluster-level and database-level parameters.

Most of the PostgreSQL parameters are configurable in an Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) cluster, but some are disabled and can’t be modified. Because Amazon Aurora clusters restrict access to the underlying operating system, modification to PostgreSQL parameters must be made using Parameter Groups.

 Amazon Aurora is a cluster of database instances and, as a direct result, some of the PostgreSQL parameters apply to the entire cluster while other parameters apply only to a particular database instance.

|  Aurora PostgreSQL parameter class | Controlled by |
| --- | --- |
|  **Cluster-level parameters** <br />Single cluster parameter group for each Amazon Aurora Cluster. | Managed by cluster parameter groups. For example,[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/chap-sql-server-aurora-pg.configuration.serveroptions.html) |
|  **Database instance-level parameters** <br />You can associate every instance in an Amazon Aurora cluster with a unique database parameter group. | Managed by database parameter groups. For example,[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/chap-sql-server-aurora-pg.configuration.serveroptions.html) |

New parameters in PostgreSQL 10:

1.  `enable_gathermerge` enables the gather merge run plan.

1.  `max_parallel_workers` stands for the maximum number of parallel workers process.

1.  `max_sync_workers_per_subscription` stands for the maximum number of synchronous workers for subscription.

1.  `wal_consistency_checking` checks consistency of WAL on the standby instance (can’t be set in Aurora PostgreSQL).

1.  `max_logical_replication_workers` stands for the maximum number of logical replication worker process.

1.  `max_pred_locks_per_relation` stands for the maximum number of records that you can predicate-lock before locking the entire relation.

1.  `max_pred_locks_per_page` stands for the maximum number of records that you can predicate-lock before locking the entire page.

1.  `min_parallel_table_scan_size` stands for the minimum table size to consider parallel table scan.

1.  `min_parallel_index_scan_size` stands for the minimum table size to consider parallel index scan.

### Examples
<a name="chap-sql-server-aurora-pg.configuration.serveroptions.pg.examples"></a>

 **To create and configure a new parameter group**

1. Sign in to the AWS Management Console and choose **RDS**.

1. Choose **Parameter groups**.
**Note**
You can’t edit the default parameter group. Create a custom parameter group to apply changes to your Amazon Aurora cluster and its database instances.

    ![Parameter groups](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-sql-server-aurora-pg-parameter-groups.png)

1. Select the DB family from the Parameter group family drop-down list.

1. For **Type**, select the DB parameter group.

1. Choose **Create**.

 **To modify an existing parameter group**

1. Sign in to the AWS Management Console and choose **RDS**.

1. Choose **Parameter groups**.

1. Choose the name of the parameter to edit.

1. Choose **Edit parameters**.

1. Change parameter values and choose **Save changes**.

For more information, see [Working with parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) in the *Amazon RDS User Guide*.
