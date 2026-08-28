---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/strategies.html
---

# Oracle database migration strategies
<a name="strategies"></a>

At a high level, there are two options for migrating an Oracle database from on premises to the AWS Cloud: either stay on Oracle (*homogeneous migration*) or move off Oracle (*heterogeneous migration*). In a homogeneous migration, you don't change the database engine (that is, your target database is also an Oracle database). In a heterogeneous migration, you switch either to an open-source database engine such as MySQL, PostgreSQL, or MariaDB, or to an AWS Cloud-native database such as Amazon Aurora, Amazon DynamoDB, or Amazon RedShift.

There are three common strategies for migrating your Oracle databases to AWS: rehost, replatform, and re-architect (refactor). These are part of the 7 Rs of application migration strategies and are described in the following table.

|
|
| Strategy | Type | When to choose | Example |
| --- |--- |--- |--- |
| **Rehost** | Homogeneous | You want to migrate your Oracle database as is, with or without changing the operating system, database software, or configuration. | Oracle Database to Amazon EC2 |
| **Replatform** | Homogeneous | You want to reduce the time you spend managing database instances by using a database-as-a-service (DBaaS) offering. | Oracle Database to Amazon RDS for Oracle |
| **Re-architect  (refactor)** | Heterogeneous | You want to restructure, rewrite, and re-architect your database and application to take advantage of open-source and cloud-native database features. | Oracle Database to Amazon Aurora PostgreSQL, MySQL, or MariaDB |

## Choosing the right migration strategy
<a name="choose-strategy"></a>

Choosing the correct strategy depends on your business requirements, your resource constraints, your migration timeframe, and cost considerations. The following diagram shows the effort and complexity involved in migrations, including six of the strategies.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/images/guide-img/b6e66b32-33d8-4097-909d-dcc9b3b4a45a/images/fee9eb5a-4f38-48b8-97b8-4ac66c04ac9d.png)

Refactoring your Oracle database and migrating to an open-source or AWS Cloud-native database such as Amazon Aurora PostgreSQL-Compatible Edition or Amazon Aurora MySQL-Compatible Edition can help you modernize and optimize your database. By moving to an open-source database, you can avoid expensive licenses (resulting in lower costs), vendor lock-in periods, and audits, and you won't have to pay additional fees for new features. However, depending on the complexity of your workload, refactoring your Oracle database can be a complicated, time-consuming, and resource-intensive effort.

To reduce complexity, instead of migrating your database in a single step, you might consider a phased approach. In the first phase, you can focus on core database functionality. In the next phase, you can integrate additional AWS services into your cloud environment, to reduce costs, and to optimize performance, productivity, and compliance. For example, if your goal is to replace your on-premises Oracle database with Aurora PostgreSQL-Compatible, you might consider rehosting your database on Amazon EC2 or replatforming your database on Amazon RDS for Oracle in the first phase, and then refactor to Aurora PostgreSQL-Compatible in a subsequent phase. This approach helps reduce costs, resources, and risks during the migration phase and focuses on optimization and modernization in the second phase.

## Online and offline migration
<a name="online-offline"></a>

You can use two methods to migrate Oracle Database from an on-premises environment to the AWS Cloud, based on your migration timeline and how much downtime you can allow: online migration or offline migration.
+ **Offline migration: **This method is used when your application can afford a planned downtime. In offline migration, the source database is offline during the migration period. While the source database is offline, it is migrated over to the target database on AWS. After the migration is complete, validation and verification checks are performed to ensure data consistency with the source database. When the database passes all validation checks, you perform a cutover to AWS by connecting your application to the target database on AWS.
+ **Online migration**: This method is used when your application requires near zero to minimal downtime. In online migration, the source database is migrated in multiple steps to AWS. In the initial steps, the data in the source database is copied to the target database while the source database is still running. In subsequent steps, all changes from the source database are propagated to the target database. When the source and target databases are in sync, they are ready for cutover. During the cutover, the application switches its connections over to the target database on AWS, leaving no connections to the source database. You can use AWS Database Migration Service (AWS DMS), Oracle GoldenGate, Quest SharePlex, or tools available from [AWS Marketplace](https://aws.amazon.com/marketplace/) (such as Attunity) to synchronize the source and target databases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
