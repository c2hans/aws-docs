---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/migration-tools.html
---

# Migration tools
<a name="migration-tools"></a>

The following tools are listed in order of logical migration to physical migration.

## Oracle Data Pump
<a name="data-pump"></a>

[Oracle Data Pump](https://docs.oracle.com/en/database/oracle/oracle-database/21/sutil/oracle-data-pump.html) is a native tool that comes with Oracle Database. It provides the ability to export and import data and metadata from or to Oracle databases. You can use Oracle Data Pump at the database, tablespace, schema, and object level. Oracle Data Pump supports flexible data extraction options, parallelism, compression, and encryption.

Oracle Data Pump is commonly used to migrate Oracle databases because it provides a high level of compatibility. Oracle Data Pump is an especially suitable option for migrations to different database editions, versions, and endian platforms. Oracle Data Pump is also often used along with other tools, such as AWS Database Migration Service (AWS DMS) and Oracle Recovery Manager (Oracle RMAN), to build comprehensive solutions for complex use cases.

## AWS DMS
<a name="aws-dms"></a>

[AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) is a managed service that helps move data to AWS securely. AWS DMS provides both one-time full database copy and change data capture (CDC) technology. The CDC feature can keep the source and target database in sync and minimize downtime during the migration. To migrate large databases, you can use AWS DMS together with other AWS services, such as Amazon S3, AWS Direct Connect, or AWS Snow Family devices.

## Oracle GoldenGate
<a name="goldengate"></a>

[Oracle GoldenGate](https://docs.oracle.com/en/middleware/goldengate/index.html) is a tool that Oracle offers to collect, replicate, and manage transactional data between databases. It provides CDC by interpreting Oracle database transaction logs. Similar to AWS DMS, Oracle GoldenGate is a common option for migrating Oracle Database. For more information, see [Using Oracle GoldenGate with Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.html).

Oracle GoldenGate is not part of Oracle Database and requires a separate license from Oracle.

## Oracle Recovery Manager
<a name="rman"></a>

[Oracle Recovery Manager (RMAN)](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/getting-started-rman.html) is a tool provided by Oracle to perform and manage Oracle database backups and restorations. You can use RMAN to back up an Oracle database from on premises and then restore it to an Oracle instance on AWS. RMAN is a physical-level tool that works on data files and log files instead of schemas and objects.

You can use Oracle RMAN with Amazon RDS Custom for Oracle. RMAN is usually combined with other AWS services, such as Direct Connect, AWS DataSync, and Amazon S3, to form an end-to-end migration solution.

## Oracle Data Guard
<a name="data-guard"></a>

[Oracle Data Guard](https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/introduction-to-oracle-data-guard-concepts.html) is a built-in feature of Oracle Database that maintains a physical copy of the database and keeps it in sync. It provides the capability to switch over the roles between primary and standby databases, which can minimize downtime during the migration.

Oracle Data Guard can't be directly used with Amazon RDS for Oracle or Amazon RDS Custom for Oracle for migration. Instead, Oracle Data Guard is usually used with AWS services such as Amazon EC2, Direct Connect, or AWS DMS to build a complete migration solution. For example, you can build a physical standby on an EC2 instance using Oracle Data Guard. Then you can use AWS DMS or Oracle Data Pump to migrate data to the target RDS for Oracle instance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
