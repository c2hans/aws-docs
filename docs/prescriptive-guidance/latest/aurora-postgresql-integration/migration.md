---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-postgresql-integration/migration.html
---

# Aurora PostgreSQL-Compatible integration with AWS DMS
<a name="migration"></a>

AWS Database Migration Service (AWS DMS) helps you to migrate relational databases, data warehouses, NoSQL databases, and other data stores between different engines. AWS DMS supports homogeneous migrations (for example, PostgreSQL to PostgreSQL) and heterogeneous migrations (for example, Oracle, SQL Server, or MySQL to Amazon Aurora PostgreSQL-Compatible Edition).

By integrating Aurora PostgreSQL-Compatible with AWS DMS, you minimize downtime. AWS DMS also helps to ensure data consistency during when migrating from on premises or other cloud environments to Aurora PostgreSQL-Compatible. Additionally, AWS DMS supports various source and target database engines, providing flexibility in migrating workloads to Aurora PostgreSQL-Compatible.

## AWS DMS use cases and high-level steps
<a name="aws-dms"></a>

AWS DMS integration with Aurora PostgreSQL-Compatible supports the following use cases:
+ **Migrating from on-premises databases** ‒ Use AWS DMS to migrate existing on-premises databases (for example, Oracle, SQL Server, MySQL, or PostgreSQL) to Aurora PostgreSQL-Compatible.
+ **Migrating from other cloud databases** ‒ Use AWS DMS to facilitate migration of databases hosted on other engines or cloud platforms (for example, Amazon RDS, Azure SQL Database, or Google Cloud SQL) to Aurora PostgreSQL-Compatible.
+ **Migrating between Aurora PostgreSQL-Compatible clusters** ‒ Use AWS DMS to migrate data between Aurora PostgreSQL-Compatible clusters, either within the same AWS Region or across different Regions.
+ **Continuous data replication and CDC** ‒ Use AWS DMS for continuous data replication and change data capture (CDC) from a source database to an Aurora PostgreSQL-Compatible. This is useful for maintaining a live replica or data warehouse for analytics purposes.

To configure AWS DMS, use the following high-level steps:

1. Set up the AWS DMS replication instance in the AWS Region that you want to use.

1. Create a source endpoint in AWS DMS, specifying the details of the database from which you want to migrate data.

1. Create a target endpoint in AWS DMS, specifying the details of your Aurora PostgreSQL-Compatible cluster.

1. Configure the migration task in AWS DMS, specifying the source and target endpoints and migration type. The type can be full load, change data capture (CDC), or both. Specify any necessary mapping rules or transformations.

1. Start the migration task.

AWS DMS will handle the data transfer and replication from the source database to the target Aurora PostgreSQL-Compatible cluster.

For detailed instructions, see the [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
