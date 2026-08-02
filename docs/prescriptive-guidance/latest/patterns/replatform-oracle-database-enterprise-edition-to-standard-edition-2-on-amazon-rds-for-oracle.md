---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replatform-oracle-database-enterprise-edition-to-standard-edition-2-on-amazon-rds-for-oracle.html
---

# Replatform Oracle Database Enterprise Edition to Standard Edition 2 on Amazon RDS for Oracle
<a name="replatform-oracle-database-enterprise-edition-to-standard-edition-2-on-amazon-rds-for-oracle"></a>

*Lanre (Lan-Ray) showunmi and Tarun Chawla, Amazon Web Services*

## Summary
<a name="replatform-oracle-database-enterprise-edition-to-standard-edition-2-on-amazon-rds-for-oracle-summary"></a>

Oracle Database Enterprise Edition (EE) is a popular choice for running applications in many enterprises. In some cases, however, applications use few or no Oracle Database EE features, so there is a lack of justification for incurring huge licensing costs. You can achieve cost savings by downgrading such databases to Oracle Database Standard Edition 2 (SE2) when you migrate to Amazon RDS.

This pattern describes how to downgrade from Oracle Database EE to Oracle Database SE2 when migrating from on premises to [Amazon RDS for Oracle](https://aws.amazon.com/rds/oracle/). The steps presented in this pattern also apply if your EE Oracle database is already running on Amazon RDS or on an [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) (Amazon EC2) instance.

For more information, see the AWS Prescriptive Guidance guide on how to [Evaluate downgrading Oracle databases to Standard Edition 2 on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/welcome.html).

## Prerequisites and limitations
<a name="replatform-oracle-database-enterprise-edition-to-standard-edition-2-on-amazon-rds-for-oracle-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Oracle Database Enterprise Edition
+ A client tool, such as [Oracle SQL Developer](https://www.oracle.com/database/sqldeveloper/) or SQL\*Plus, for connecting to and running SQL commands on Oracle database
+ Database user for performing the assessment; for example, one of the following:
  + User with sufficient [privileges](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Permissions) for running [AWS Schema Conversion Tool (AWS SCT)](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) assessment
  + User with sufficient privileges to run SQL queries on Oracle database dictionary tables
+ Database user for performing database migration; for example, one of the following:
  + User with sufficient [privileges](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Self-Managed) for running [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
  + User with sufficient [privileges for performing Oracle Data Pump export and import](https://docs.oracle.com/database/121/SUTIL/GUID-8B6975D3-3BEC-4584-B416-280125EEC57E.htm#SUTIL807)
  + User with sufficient [privileges for running Oracle GoldenGate](https://docs.oracle.com/goldengate/1212/gg-winux/GIORA/user_assignment.htm#GIORA546)

**Limitations **
+ Amazon RDS for Oracle has a maximum database size. For more information, see [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html).

**Product versions**

The general logic described in this document applies to Oracle versions from 9i and later. For supported versions of self-managed and Amazon RDS for Oracle databases, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html).

To identify feature usage in cases where AWS SCT is not supported, run SQL queries on the source database. To migrate from earlier versions of Oracle where AWS DMS and Oracle Data Pump are not supported, use [Oracle Export and Import utilities](https://docs.oracle.com/cd/B19306_01/server.102/b14215/exp_imp.htm).

For a current list of supported versions and editions, see [Oracle on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) in the AWS documentation. For details on pricing and supported instance classes, see [Amazon RDS for Oracle pricing](https://aws.amazon.com/rds/oracle/pricing/).

## Architecture
<a name="replatform-oracle-database-enterprise-edition-to-standard-edition-2-on-amazon-rds-for-oracle-architecture"></a>

**Source technology stack  **
+ Oracle Database Enterprise Edition running on premises or on Amazon EC2

**Target technology stack using native Oracle tools **
+ Amazon RDS for Oracle running Oracle Database SE2

![Three-step process for migrating from on-premises Oracle DB to Amazon RDS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a1b28050-9bab-4de6-b2a9-b97b3e5070bd/images/bf765c5b-4b12-4a8c-b27c-c5e0bd605dd1.png)

1. Export data by using Oracle Data Pump.

1. Copy dump files to Amazon RDS through a database link.

1. Import dump files to Amazon RDS by using Oracle Data Pump.

**Target technology stack using AWS DMS **
+ Amazon RDS for Oracle running Oracle Database SE2
+ AWS DMS

![Four-step process for migrating from on-premises Oracle DB to Amazon RDS using AWS DMS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a1b28050-9bab-4de6-b2a9-b97b3e5070bd/images/fef4eced-1acb-4303-baaa-5c1c29650935.png)

1. Export data by using Oracle Data Pump with FLASHBACK\_SCN.

1. Copy dump files to Amazon RDS through a database link.

1. Import dump files to Amazon RDS by using Oracle Data Pump.

1. Use AWS DMS [change data capture (CDC)](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html).

## Tools
<a name="replatform-oracle-database-enterprise-edition-to-standard-edition-2-on-amazon-rds-for-oracle-tools"></a>

**AWS services**
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud. This pattern uses Amazon RDS for Oracle.
+ [AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)** **provides a project-based user interface to automatically assess, convert, and copy the database schema of your source Oracle database into a format compatible with Amazon RDS for Oracle. AWS SCT enables you to analyze potential cost savings that can be achieved by changing your license type from Enterprise to Standard Edition of Oracle. The **License Evaluation and Cloud Support** section of the AWS SCT report provides detailed information about Oracle features in use so you can make an informed decision while migrating to Amazon RDS for Oracle.

**Other tools**
+ Native Oracle import and export utilities support moving Oracle data in and out of Oracle databases. Oracle offers two types of database import and export utilities: [Original Export and Import](https://docs.oracle.com/cd/B19306_01/server.102/b14215/exp_imp.htm) (for earlier releases) and [Oracle Data Pump Export and Import](https://docs.oracle.com/cd/B19306_01/server.102/b14215/part_dp.htm#CEGJCCHC) (available in Oracle Database 10g release 1 and later).
+ [Oracle GoldenGate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.html) offers real-time replication capabilities so that you can synchronize your target database after an initial load. This option can help reduce application downtime during go-live.

## Epics
<a name="replatform-oracle-database-enterprise-edition-to-standard-edition-2-on-amazon-rds-for-oracle-epics"></a>

### Make a pre-migration assessment
<a name="make-a-pre-migration-assessment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate database requirements for your applications. | Ensure that your applications are certified to run on Oracle Database SE2. Check directly with the software vendor, developer, or application documentation. | App developer, DBA, App owner |
| Investigate use of EE features directly in the database. | To determine EE feature use, do one of the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replatform-oracle-database-enterprise-edition-to-standard-edition-2-on-amazon-rds-for-oracle.html) | App owner, DBA, App developer |
| Identify use of EE features for operational activities. | Database or application administrators sometimes rely on EE-only features for operational activities. Common examples include online maintenance activities (index rebuild, table move) and use of parallelism by batch jobs.<br />These dependencies can be mitigated by modifying your operations where possible. Identify the use of these features and make a decision based on cost compared with benefits.<br />Use the [Comparing Oracle Database EE and SE2 features ](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/compare-features.html)table as a guide to identify features that are available in Oracle Database SE2. | App developer, DBA, App owner |
| Review workload patterns of the EE Oracle database. | Oracle Database SE2 automatically restricts usage to a maximum of 16 CPU threads at any time.<br />If your Oracle EE database is licensed to use the Oracle Diagnostic Pack, use the Automatic Workload Repository (AWR) tool, or DBA\_HIST\_\* views, to analyze database workload patterns to determine whether the maximum limit of 16 CPU threads will negatively impact service levels when you downgrade to SE2.<br />Ensure that your assessment covers periods of peak activity, such as end of day, month, or year processing. | App owner, DBA, App developer |

### Prepare the target infrastructure on AWS
<a name="prepare-the-target-infrastructure-on-aws"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy and configure networking infrastructure. | Create a [virtual private cloud (VPC) and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html), [security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html), and [network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html). | AWS administrator, Cloud architect, Network administrator, DevOps engineer |
| Provision the Amazon RDS for Oracle SE2 database. | Provision the target [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.Oracle.html) SE2 database to meet your applications’ performance, availability, and security requirements. We recommend Multi-AZ configuration for production workloads. However, to improve migration performance, you can defer [enabling Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-multi-az-db-cluster.html) until after data migration. | Cloud administrator, Cloud architect, DBA, DevOps engineer, AWS administrator |
| Customize the Amazon RDS environment. | Configure custom [parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html) and [options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html), and enable additional [monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MonitoringOverview.html). For more information, see [Best practices for migrating to Amazon RDS for Oracle](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/best-practices.html). | AWS administrator, AWS systems administrator, Cloud administrator, DBA, Cloud architect |

### Perform the migration dry run and application testing
<a name="perform-the-migration-dry-run-and-application-testing"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate the data (dry run). | Migrate data from the source Oracle EE database to the Amazon RDS for Oracle SE2 database instance using the approach best suited to your specific environment. Select a migration strategy based on factors such as size, complexity, and the available downtime window. Use one or a combination of the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/replatform-oracle-database-enterprise-edition-to-standard-edition-2-on-amazon-rds-for-oracle.html) | DBA |
| Validate the target database. | Perform post-migration validation of database storage and code objects. Review migration logs, and fix any identified issues. For more information, see the guide [Migrating Oracle databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/best-practices.html#post-import). | DBA |
| Test the applications. | Application and database administrators should conduct functional, performance, and operational tests as appropriate. For more information, see [Best practices for migrating to Amazon RDS for Oracle](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/best-practices.html#test-migration).<br />Lastly, obtain sign-offs on test-results from stakeholders. | App developer, App owner, DBA, Migration engineer, Migration lead |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Refresh data from Oracle Database EE. | Select a data refresh approach based on the application availability requirement. For more information, see the migration methods in [Strategies for Migrating Oracle Databases to AWS](https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/data-migration-methods.html).<br />For example, you can achieve near-zero downtime by using tools such as Oracle GoldenGate or AWS DMS with ongoing replication. If the downtime window permits, you can perform the final data cutover using offline methods such as Oracle Data Pump or Original Export-Import utilities. | App owner, Cutover lead, DBA, Migration engineer, Migration lead |
| Point applications to the target database instance. | Update connection parameters in applications and other clients to point to the Amazon RDS for Oracle SE2 database. | App developer, App owner, Migration engineer, Migration lead, Cutover lead |
| Perform post-migration activities. | Perform post data migration tasks such as enabling Multi-AZ, data validation, and other checks. | DBA, Migration engineer |
| Perform post-cutover monitoring. | Use tools such as [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-cloudwatch.html) and Amazon [RDS Performance Insights](https://aws.amazon.com/rds/performance-insights/) to monitor the Amazon RDS for Oracle SE2 database. | App developer, App owner, AWS administrator, DBA, Migration engineer |

## Related resources
<a name="replatform-oracle-database-enterprise-edition-to-standard-edition-2-on-amazon-rds-for-oracle-resources"></a>

**AWS Prescriptive Guidance**
+ [Migrating Oracle databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/welcome.html) (guide)
+ [Evaluate downgrading Oracle databases to Standard Edition 2 on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-oracle-edition/welcome.html) (guide)
+ [Migrate an on-premises Oracle database to Amazon RDS for Oracle](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle.html?did=pg_card&trk=pg_card) (pattern)
+ [Migrate an on-premises Oracle database to Amazon RDS for Oracle using Oracle Data Pump](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-oracle-database-to-amazon-rds-for-oracle-using-oracle-data-pump.html?did=pg_card&trk=pg_card) (pattern)

**Blog posts**
+ [Migrating Oracle databases with near-zero downtime using AWS DMS](https://aws.amazon.com/blogs/database/migrating-oracle-databases-with-near-zero-downtime-using-aws-dms/)
+ [Analyzing performance management in Oracle SE using Amazon RDS for Oracle](https://aws.amazon.com/blogs/database/analyzing-performance-management-in-oracle-se-using-amazon-rds-for-oracle/)
+ [Managing your SQL plan in Oracle SE with Amazon RDS for Oracle](https://aws.amazon.com/blogs/database/managing-your-sql-plan-in-oracle-se-with-amazon-rds-for-oracle/)
+ [Implementing table partitioning in Oracle Standard Edition: Part 1](https://aws.amazon.com/blogs/database/implementing-table-partitioning-in-oracle-standard-edition-part-1/)
