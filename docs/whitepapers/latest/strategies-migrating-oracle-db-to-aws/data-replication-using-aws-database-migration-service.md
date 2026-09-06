---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/data-replication-using-aws-database-migration-service.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data replication using AWS Database Migration Service
<a name="data-replication-using-aws-database-migration-service"></a>

 [AWS Database Migration Service](https://aws.amazon.com/dms/) (AWS DMS) can support a number of migration and replication strategies including a bulk upload at a point in time, a minimal downtime migration leveraging Change Data Capture (CDC), or migration of only a subset of the data. AWS DMS supports sources and targets in EC2, RDS, and on-premises. Because no client install is required, the following steps are the same for any combination of the above. AWS DMS also offers the ability to migrate data between databases as easily as from Oracle to Oracle.

 The following steps show how to migrate data between Oracle databases using AWS DMS and with minimal downtime:

1.  Ensure supplemental logging is enabled on the source database.

1.  Create the target database and ensure database backups and Multi-AZ are turned off if the target is on RDS.

1.  Perform a no-data export of the schema using Oracle SQL Developer or the tool of your choice, then apply the schema to the target database.

1.  Disable triggers, foreign keys, and secondary indexes (optional) on the target.

1.  Create a DMS replication instance.

1.  Specify the source and target endpoints.

1.  Create a “Migrate existing data and replicate ongoing changes” task, mapping your source tables to your target tables. (The default task includes all tables.)

1.  Start the task.

1.  After the full load portion of the tasks is complete and the transactions reach a steady state, enable triggers, foreign keys, and secondary indexes.

1.  Turn on backups and Multi-AZ.

1.  Turn off any applications using the original source database.

1.  Let the final transactions flow through.

1.  Point any applications at the new database in AWS and start.

 An alternative method is to use Oracle Data Pump for the initial load and DMS to replicate changes from the Oracle System Change Number (SCN) point where data dump stopped. More details on using AWS DMS can be found in the [documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html). To improve the performance of DMS replication, the schemas and tables can be grouped into multiple DMS tasks. DMS tasks support wildcard entries for the names of the schemas and tables.
