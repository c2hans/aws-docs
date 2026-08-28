---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/strategies.html
---

# SQL Server database migration strategies
<a name="strategies"></a>

At a high level, there are two options for migrating a SQL Server database from on premises to the AWS Cloud: either stay on SQL Server ([homogeneous migration](homogeneous-migration.md)) or move off SQL Server ([heterogeneous migration](heterogeneous-migration.md)). In a homogeneous migration, you don't change the database engine. That is, your target database is also a SQL Server database. In a heterogeneous migration, you switch your SQL Server databases either to an open-source database engine such as MySQL, PostgreSQL, or MariaDB, or to an AWS cloud-native database, such as Amazon Aurora, Amazon DynamoDB, or Amazon Redshift.

There are three common strategies for migrating your SQL Server databases to AWS: rehost, replatform, and re-architect (refactor). These are part of the 7 Rs of application migration strategies and described in the following table.

|
|
| **Strategy** | **Type** | **When to choose** | **Example** |
| --- |--- |--- |--- |
| **Rehost** | Homogeneous | You want to migrate your SQL Server database as is, with or without changing the operating system, database software, or configuration. | SQL Server to Amazon EC2 |
| **Replatform** | Homogeneous | You want to reduce the time you spend managing database instances by using a fully managed database offering. | SQL Server to Amazon RDS for SQL Server |
| **Re-architect  (refactor)** | Heterogeneous | You want to restructure, rewrite, and re-architect your database and application to take advantage of open-source and cloud-native database features. | SQL Server to Amazon Aurora PostgreSQL, MySQL, or MariaDB |

If you're trying to decide between rehosting or replatforming your SQL Server databases, see [Choosing between Amazon EC2 and Amazon RDS](comparison.md) later in this guide for a side-by-side comparison of supported features.

## Choosing the right migration strategy
<a name="choose-strategy"></a>

Choosing the correct strategy depends on your business requirements, resource constraints, migration timeframe, and cost considerations. The following diagram shows the effort and complexity involved in migrations, including all seven strategies.

![Comparison of SQL Server migration strategies.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/38d62954-e016-4185-b9f6-d19d207b6552.png)

Refactoring your SQL Server database and migrating to an open-source or AWS cloud-native database such as Aurora PostgreSQL or Aurora MySQL can help you modernize and optimize your database. By moving to an open-source database, you can avoid expensive licenses (resulting in lower costs), vendor lock-in periods, and audits. However, depending on the complexity of your workload, refactoring your SQL Server database can be a complicated, time-consuming, and resource-intensive effort.

To reduce complexity, instead of migrating your database in a single step, you might consider a phased approach. In the first phase, you can focus on core database functionality. In the next phase, you can integrate additional AWS services into your cloud environment, to reduce costs, and to optimize performance, productivity, and compliance. For example, if your goal is to replace your on-premises SQL Server database with Aurora MySQL, you might consider rehosting your database on Amazon EC2 or replatforming your database on Amazon RDS for SQL Server in the first phase, and then refactor to Aurora MySQL in a subsequent phase. This approach helps reduce costs, resources, and risks during the migration phase and focuses on optimization and modernization in the second phase.

## Online and offline migration
<a name="online-offline"></a>

You can use two methods to migrate your SQL Server database from an on-premises or another cloud environment to the AWS Cloud, based on your migration timeline and how much downtime you can allow: offline migration or online migration.
+ **Offline migration: **This method is used when your application can afford a planned downtime. In offline migration, the source database is offline during the migration period. While the source database is offline, it is migrated over to the target database on AWS. After the migration is complete, validation and verification checks are performed to ensure data consistency with the source database. When the database passes all validation checks, you perform a cutover to AWS by connecting your application to the target database on AWS.
+ **Online migration**: This method is used when your application requires near zero to minimal downtime. In online migration, the source database is migrated in multiple steps to AWS. In the initial steps, the data in the source database is copied to the target database while the source database is still running. In subsequent steps, all changes from the source database are propagated to the target database. When the source and target databases are in sync, they are ready for cutover. During the cutover, the application switches its connections over to the target database on AWS, leaving no connections to the source database. You can use AWS Database Migration Service (AWS DMS), or tools available from [AWS Marketplace](https://aws.amazon.com/marketplace/) (such as Attunity) to synchronize the source and target databases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
