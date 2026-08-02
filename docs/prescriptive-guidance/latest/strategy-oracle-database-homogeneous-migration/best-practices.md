---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-oracle-database-homogeneous-migration/best-practices.html
---

# Best practices
<a name="best-practices"></a>

## Offline migration
<a name="offline"></a>

For offline migration, we recommend the following best practices:
+ Make sure that the target EC2 instance has sufficient resources to handle the migration workload. During migration, you can disable archive logging, or you can provision a larger EC2 instance or [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/) volumes with higher IOPS.
+ Monitor network bandwidth carefully. If possible, provision a dedicated network such as [AWS Direct Connect](https://aws.amazon.com/directconnect/) for the migration.
+ Make sure to follow best practices for migration tools such as Oracle Data Pump ([configuring the number of parallel threads](https://docs.oracle.com/database/121/SUTIL/GUID-1E134053-692A-4386-BB77-153CB4A6071A.htm#SUTIL887)) or AWS DMS ([loading tables by using multiple threads](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Tablesettings.html#CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Tablesettings.ParallelLoad)).
+ For best practices to migrate from on premises to Amazon RDS for Oracle, see the AWS blog post [Achieve a high-performance migration to Amazon RDS for Oracle from on-premises Oracle with AWS DMS](https://aws.amazon.com/blogs/database/achieve-a-high-performance-migration-to-amazon-rds-for-oracle-from-on-premises-oracle-with-aws-dms/).

## Online migration
<a name="online"></a>

Best practices for online migrations include the guidelines for offline migration provided in the previous list, and the following additional considerations:
+ Use best practices for online tools. For example, when you use AWS DMS, choose the [right method of reading the redo logs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC) from Oracle LogMiner or AWS DMS Binary Reader.
+ Make sure that tables with a high number of data manipulation languages (DMLs) are separated logically from tables that have fewer DMLs.
+ Follow the best practices for using Oracle native tools, such as Oracle GoldenGate or Oracle Data Guard.
