---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html
---

# Setting up binary log replication for Aurora MySQL
<a name="AuroraMySQL.Replication.MySQL.SettingUp"></a>

Setting up MySQL replication with Aurora MySQL involves the following steps, which are discussed in detail:

**Contents**
+ [1. Turn on binary logging on the replication source](#AuroraMySQL.Replication.MySQL.EnableBinlog)
+ [2. Retain binary logs on the replication source until no longer needed](#AuroraMySQL.Replication.MySQL.RetainBinlogs)
+ [3. Create a copy or dump of your replication source](#AuroraMySQL.Replication.MySQL.CreateSnapshot)
+ [4. Load the dump into your replica target (if needed)](#AuroraMySQL.Replication.MySQL.LoadSnapshot)
+ [5. Create a replication user on your replication source](#AuroraMySQL.Replication.MySQL.CreateReplUser)
+ [6. Turn on replication on your replica target](#AuroraMySQL.Replication.MySQL.EnableReplication)
  + [Setting a location to stop replication to a read replica](#AuroraMySQL.Replication.StartReplicationUntil)
+ [7. Monitor your replica](#AuroraMySQL.Replication.MySQL.Monitor)
+ [Synchronizing passwords between replication source and target](#AuroraMySQL.Replication.passwords)

## 1. Turn on binary logging on the replication source
<a name="AuroraMySQL.Replication.MySQL.EnableBinlog"></a>

 Find instructions on how to turn on binary logging on the replication source for your database engine following.

|  Database engine  |  Instructions  |
| --- | --- |
|  Aurora MySQL  |  **To turn on binary logging on an Aurora MySQL DB cluster** <br />Set the `binlog_format` DB cluster parameter to `ROW`, `STATEMENT`, or `MIXED`. `MIXED` is recommended unless you have a need for a specific binlog format. (The default value is `OFF`.)<br />To change the `binlog_format` parameter, create a custom DB cluster parameter group and associate that custom parameter group with your DB cluster. You can't change parameters in the default DB cluster parameter group.<br />If you're changing the `binlog_format` parameter from `OFF` to another value, reboot your Aurora DB cluster for the change to take effect.<br /> For more information, see [Amazon Aurora DB cluster and DB instance parameters](USER_WorkingWithDBClusterParamGroups.md#Aurora.Managing.ParameterGroups) and [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md).  |
|  RDS for MySQL  |  **To turn on binary logging on an Amazon RDS DB instance** <br /> You can't turn on binary logging directly for an Amazon RDS DB instance, but you can turn it on by doing one of the following: [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html) |
|  MySQL (external) | **To set up encrypted replication**<br />To replicate data securely with Aurora MySQL version 2, you can use encrypted replication.  If you don't need to use encrypted replication, you can skip these steps.  <br /> The following are prerequisites for using encrypted replication: [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html)<br /> During encrypted replication, the Aurora MySQL DB cluster acts a client to the MySQL database server. The certificates and keys for the Aurora MySQL client are in files in .pem format. [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html)<br /> **To turn on binary logging on an external MySQL database** [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html) |

## 2. Retain binary logs on the replication source until no longer needed
<a name="AuroraMySQL.Replication.MySQL.RetainBinlogs"></a>

When you use MySQL binary log replication, Amazon RDS doesn't manage the replication process. As a result, you need to ensure that the binlog files on your replication source are retained until after the changes have been applied to the replica. This maintenance helps you to restore your source database in the event of a failure.

Use the following instructions to retain binary logs for your database engine.

|  Database engine  |  Instructions  |
| --- | --- |
|  Aurora MySQL | **To retain binary logs on an Aurora MySQL DB cluster**<br />You don't have access to the binlog files for an Aurora MySQL DB cluster. As a result, you must choose a time frame to retain the binlog files on your replication source long enough to ensure that the changes have been applied to your replica before the binlog file is deleted by Amazon RDS. You can retain binlog files on an Aurora MySQL DB cluster for up to 90 days.<br />If you're setting up replication with a MySQL database or RDS for MySQL DB instance as the replica, and the database that you are creating a replica for is very large, choose a large time frame to retain binlog files until the initial copy of the database to the replica is complete and the replica lag has reached 0.<br />To set the binary log retention time frame, use the [mysql.rds\_set\_configuration](mysql-stored-proc-configuring.md#mysql_rds_set_configuration) procedure and specify a configuration parameter of `'binlog retention hours'` along with the number of hours to retain binlog files on the DB cluster. The maximum value for Aurora MySQL version 2.11.0 and higher and version 3 is 2160 (90 days).<br />The following example sets the retention period for binlog files to 6 days:<pre>CALL mysql.rds_set_configuration('binlog retention hours', 144);</pre><br />After replication has been started, you can verify that changes have been applied to your replica by running the `SHOW SLAVE STATUS` (Aurora MySQL version 2) or `SHOW REPLICA STATUS` (Aurora MySQL version 3) command on your replica and checking the `Seconds behind master` field. If the `Seconds behind master` field is 0, then there is no replica lag. When there is no replica lag, reduce the length of time that binlog files are retained by setting the `binlog retention hours` configuration parameter to a smaller time frame.<br />If this setting isn't specified, the default for Aurora MySQL is 24 (1 day).<br />If you specify a value for `'binlog retention hours'` that is higher than the maximum value, then Aurora MySQL uses the maximum. |
|  RDS for MySQL  |  **To retain binary logs on an Amazon RDS DB instance** <br /> You can retain binary log files on an Amazon RDS DB instance by setting the binlog retention hours just as with an Aurora MySQL DB cluster, described in the previous row.<br />You can also retain binlog files on an Amazon RDS DB instance by creating a read replica for the DB instance. This read replica is temporary and solely for the purpose of retaining binlog files. After the read replica has been created, call the [mysql.rds\_stop\_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication) procedure on the read replica. While replication is stopped, Amazon RDS doesn't delete any of the binlog files on the replication source. After you have set up replication with your permanent replica, you can delete the read replica when the replica lag (`Seconds behind master` field) between your replication source and your permanent replica reaches 0. |
|  MySQL (external)  | **To retain binary logs on an external MySQL database**<br />Because binlog files on an external MySQL database are not managed by Amazon RDS, they are retained until you delete them.<br />After replication has been started, you can verify that changes have been applied to your replica by running the `SHOW SLAVE STATUS` (Aurora MySQL version 2) or `SHOW REPLICA STATUS` (Aurora MySQL version 3) command on your replica and checking the `Seconds behind master` field. If the `Seconds behind master` field is 0, then there is no replica lag. When there is no replica lag, you can delete old binlog files. |

## 3. Create a copy or dump of your replication source
<a name="AuroraMySQL.Replication.MySQL.CreateSnapshot"></a>

You use a snapshot, clone, or dump of your replication source to load a baseline copy of your data onto your replica. Then you start replicating from that point.

Use the following instructions to create a copy or dump of the replication source for your database engine.

| Database engine | Instructions |
| --- | --- |
|  Aurora MySQL  | **To create a copy of an Aurora MySQL DB cluster**<br />Use one of the following methods:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html)<br />**To determine the binlog file name and position**<br />Use one of the following methods:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html)<br />**To create a dump of an Aurora MySQL DB cluster**<br />If your replica target is an external MySQL database or an RDS for MySQL DB instance, then you must create a dump file from your Aurora DB cluster.<br />Be sure to run the `mysqldump` command against the copy of your source DB cluster that you created. This is to avoid locking considerations when taking the dump. If the dump were taken on the source DB cluster directly, it would be necessary to lock the source tables to prevent concurrent writes to them while the dump is in progress.[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html) |
| RDS for MySQL | **To create a snapshot of an Amazon RDS DB instance**<br />Create a read replica of your Amazon RDS DB instance. For more information, see [Creating a read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Create) in the *Amazon Relational Database Service User Guide*. [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html) |
| MySQL (external) | **To create a dump of an external MySQL database**[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html) |

## 4. Load the dump into your replica target (if needed)
<a name="AuroraMySQL.Replication.MySQL.LoadSnapshot"></a>

If you plan to load data from a dump of a MySQL database that is external to Amazon RDS, you might want to create an EC2 instance to copy the dump files to. Then you can load the data into your DB cluster or DB instance from that EC2 instance. Using this approach, you can compress the dump file(s) before copying them to the EC2 instance in order to reduce the network costs associated with copying data to Amazon RDS. You can also encrypt the dump file or files to secure the data as it is being transferred across the network.

**Note**
If you create a new Aurora MySQL DB cluster as your replica target, then you don't need to load a dump file:
You can restore from a DB cluster snapshot to create a new DB cluster. For more information, see [Restoring from a DB cluster snapshot](aurora-restore-snapshot.md).
You can clone your source DB cluster to create a new DB cluster. For more information, see [Cloning a volume for an Amazon Aurora DB cluster](Aurora.Managing.Clone.md).
You can migrate the data from a DB instance snapshot into a new DB cluster. For more information, see [Migrating data to an Amazon Aurora MySQL DB cluster](AuroraMySQL.Migrating.md).

Use the following instructions to load the dump of your replication source into your replica target for your database engine.

| Database engine | Instructions |
| --- | --- |
| Aurora MySQL  |  **To load a dump into an Aurora MySQL DB cluster** [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html) |
|  RDS for MySQL  | **To load a dump into an Amazon RDS DB instance**[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html) |
| MySQL (external) | **To load a dump into an external MySQL database**<br />You can't load a DB snapshot or a DB cluster snapshot into an external MySQL database. Instead, you must use the output from the `mysqldump` command.[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html) |

## 5. Create a replication user on your replication source
<a name="AuroraMySQL.Replication.MySQL.CreateReplUser"></a>

Create a user ID on the source that is used solely for replication. The following example is for RDS for MySQL or external MySQL source databases.

```
mysql> CREATE USER '{{repl_user}}'@'{{domain_name}}' IDENTIFIED BY '{{password}}';
```

For Aurora MySQL source databases, the `skip_name_resolve` DB cluster parameter is set to `1` (`ON`) and can't be modified, so you must use an IP address for the host instead of a domain name. For more information, see [skip\_name\_resolve](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_skip_name_resolve) in the MySQL documentation.

```
mysql> CREATE USER '{{repl_user}}'@'{{IP_address}}' IDENTIFIED BY '{{password}}';
```

The user requires the `REPLICATION CLIENT` and `REPLICATION SLAVE` privileges. Grant these privileges to the user.

If you need to use encrypted replication, require SSL connections for the replication user. For example, you can use one of the following statements to require SSL connections on the user account `repl_user`.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO '{{repl_user}}'@'{{IP_address}}';
```

```
GRANT USAGE ON *.* TO '{{repl_user}}'@'{{IP_address}}' REQUIRE SSL;
```

**Note**
If `REQUIRE SSL` isn't included, the replication connection might silently fall back to an unencrypted connection.

## 6. Turn on replication on your replica target
<a name="AuroraMySQL.Replication.MySQL.EnableReplication"></a>

Before you turn on replication, we recommend that you take a manual snapshot of the Aurora MySQL DB cluster or RDS for MySQL DB instance replica target. If a problem arises and you need to re-establish replication with the DB cluster or DB instance replica target, you can restore the DB cluster or DB instance from this snapshot instead of having to import the data into your replica target again.

Use the following instructions to turn on replication for your database engine.

|  Database engine  |  Instructions  |
| --- | --- |
|  Aurora MySQL  | **To turn on replication from an Aurora MySQL DB cluster** [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html)<br />To use SSL encryption, set the final value to `1` instead of `0`. |
|  RDS for MySQL  |  **To turn on replication from an Amazon RDS DB instance** [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html)<br />To use SSL encryption, set the final value to `1` instead of `0`. |
|  MySQL (external)  |  **To turn on replication from an external MySQL database** [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html) |

If replication fails, it can result in a large increase in unintentional I/O on the replica, which can degrade performance. If replication fails or is no longer needed, you can run the [mysql.rds\_reset\_external\_master (Aurora MySQL version 2)](mysql-stored-proc-replicating.md#mysql_rds_reset_external_master) or [mysql.rds\_reset\_external\_source (Aurora MySQL version 3)](mysql-stored-proc-replicating.md#mysql_rds_reset_external_source) stored procedure to remove the replication configuration.

### Setting a location to stop replication to a read replica
<a name="AuroraMySQL.Replication.StartReplicationUntil"></a>

In Aurora MySQL version 3.04 and higher, you can start replication and then stop it at a specified binary log file location using the [mysql.rds\_start\_replication\_until(Aurora MySQL version 3)](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until) stored procedure.

**To start replication to a read replica and stop replication at a specific location**

1. Using a MySQL client, connect to the replica Aurora MySQL DB cluster as the master user.

1. Run the [mysql.rds\_start\_replication\_until(Aurora MySQL version 3)](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until) stored procedure.

   The following example initiates replication and replicates changes until it reaches location `120` in the `mysql-bin-changelog.000777` binary log file. In a disaster recovery scenario, assume that location `120` is just before the disaster.

   ```
   call mysql.rds_start_replication_until(
     'mysql-bin-changelog.000777',
     120);
   ```

Replication stops automatically when the stop point is reached. The following RDS event is generated: `Replication has been stopped since the replica reached the stop point specified by the rds_start_replication_until stored procedure`.

If you use GTID-based replication, use the [mysql.rds\_start\_replication\_until\_gtid(Aurora MySQL version 3)](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid) stored procedure instead of the [mysql.rds\_start\_replication\_until(Aurora MySQL version 3)](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until) stored procedure. For more information about GTID-based replication, see [Using GTID-based replication](mysql-replication-gtid.md).

## 7. Monitor your replica
<a name="AuroraMySQL.Replication.MySQL.Monitor"></a>

 When you set up MySQL replication with an Aurora MySQL DB cluster, you must monitor failover events for the Aurora MySQL DB cluster when it is the replica target. If a failover occurs, then the DB cluster that is your replica target might be recreated on a new host with a different network address. For information on how to monitor failover events, see [Working with Amazon RDS event notification](USER_Events.md).

 You can also monitor how far the replica target is behind the replication source by connecting to the replica target and running the `SHOW SLAVE STATUS` (Aurora MySQL version 2) or `SHOW REPLICA STATUS` (Aurora MySQL version 3) command. In the command output, the `Seconds Behind Master` field tells you how far the replica target is behind the source.

**Important**
If you upgrade your DB cluster and specify a custom parameter group, make sure to manually reboot the cluster after the upgrade finishes. Doing so makes the cluster use your new custom parameter settings, and restarts binlog replication.

## Synchronizing passwords between replication source and target
<a name="AuroraMySQL.Replication.passwords"></a>

 When you change user accounts and passwords on the replication source using SQL statements, those changes are replicated to the replication target automatically.

 If you use the AWS Management Console, the AWS CLI, or the RDS API to change the master password on the replication source, those changes are not automatically replicated to the replication target. If you want to synchronize the master user and master password between the source and target systems, you must make the same change on the replication target yourself.
