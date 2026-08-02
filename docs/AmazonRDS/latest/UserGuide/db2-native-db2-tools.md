---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools.html
---

# Using native Db2 tools to migrate data from Db2 to Amazon RDS for Db2
<a name="db2-native-db2-tools"></a>

You can use several native Db2 tools, utilities, and commands to move data directly from a Db2 database to an Amazon RDS for Db2 database. To use these native Db2 tools, you must be able to connect your client machine to an RDS for Db2 DB instance. For more information, see [Connecting a client machine to an Amazon RDS for Db2 DB instance](db2-connecting-client-rds.md).

**Note**
Another way to move your data is to first save it to an Amazon S3 bucket, and then use the `LOAD` command to transfer that data into a table in your RDS for Db2 database. This method provides the best performance when migrating a large amount of data because of good network connectivity between RDS for Db2 and S3. For more information, see [Migrating Db2 data through Amazon S3 to Amazon RDS for Db2](db2-migration-load-from-s3.md).

| Tool name | Use case | Limitations |
| --- | --- | --- |
| [db2look](db2-native-db2-tools-db2look.md)  | Copying metadata from a self-managed Db2 database to an RDS for Db2 database. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools.html)  |
| [IMPORT command](db2-native-db2-tools-import.md) | Migrating small tables and tables with large objects (LOBs) from a client machine to the RDS for Db2 DB instance. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools.html)  |
| [INGEST utility](db2-native-db2-tools-ingest.md)  | Continually streaming data from files and pipes *without* large objects (LOBs) on the client machine to the RDS for Db2 DB instance. Supports `INSERT` and `MERGE` operations.  |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools.html)  |
| [INSERT command](db2-native-db2-tools-insert.md) | Copying data in small tables from a self-managed Db2 database to an RDS for Db2 database. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools.html)  |
| [LOAD CLIENT command](db2-native-db2-tools-load.md) | Migrating small tables *without *large objects (LOBs) from a client machine to the RDS for Db2 DB instance. |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools.html)  |
