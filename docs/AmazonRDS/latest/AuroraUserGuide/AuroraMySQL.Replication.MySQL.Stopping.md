---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.Stopping.html
---

# Stopping binary log replication for Aurora MySQL
<a name="AuroraMySQL.Replication.MySQL.Stopping"></a>

To stop binary log replication with a MySQL DB instance, external MySQL database, or another Aurora DB cluster, follow these steps, discussed in detail following in this topic.

[1. Stop binary log replication on the replica target](#AuroraMySQL.Replication.MySQL.Stopping.StopReplication)

[2. Turn off binary logging on the replication source](#AuroraMySQL.Replication.MySQL.Stopping.DisableBinaryLogging)

## 1. Stop binary log replication on the replica target
<a name="AuroraMySQL.Replication.MySQL.Stopping.StopReplication"></a>

Use the following instructions to stop binary log replication for your database engine.

|  Database engine  |  Instructions  |
| --- | --- |
|  Aurora MySQL  | **To stop binary log replication on an Aurora MySQL DB cluster replica target**<br />Connect to the Aurora DB cluster that is the replica target, and call the [mysql.rds\_stop\_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication) procedure. |
|  RDS for MySQL  | **To stop binary log replication on an Amazon RDS DB instance**<br />Connect to the RDS DB instance that is the replica target and call the [mysql.rds\_stop\_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication) procedure. |
|  MySQL (external)  | **To stop binary log replication on an external MySQL database**<br />Connect to the MySQL database and run the `STOP SLAVE` (version 5.7) or `STOP REPLICA` (version 8.0) command. |

## 2. Turn off binary logging on the replication source
<a name="AuroraMySQL.Replication.MySQL.Stopping.DisableBinaryLogging"></a>

Use the instructions in the following table to turn off binary logging on the replication source for your database engine.

| Database engine | Instructions |
| --- | --- |
|  Aurora MySQL  | **To turn off binary logging on an Amazon Aurora DB cluster**[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.Stopping.html) |
|  RDS for MySQL  | **To turn off binary logging on an Amazon RDS DB instance**<br />You can't turn off binary logging directly for an Amazon RDS DB instance, but you can turn it off by doing the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.Stopping.html) |
|  MySQL (external)  | **To turn off binary logging on an external MySQL database**<br />Connect to the MySQL database and call the `STOP REPLICATION` command.[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.Stopping.html) |
