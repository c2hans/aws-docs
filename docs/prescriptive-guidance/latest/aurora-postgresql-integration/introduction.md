---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-postgresql-integration/introduction.html
---

# Integrating Amazon Aurora PostgreSQL-Compatible with heterogeneous databases and AWS services
<a name="introduction"></a>

*Rambabu Karnena, Amazon Web Services*

Amazon Aurora PostgreSQL-Compatible Edition offers integration with heterogeneous databases and various services on the Amazon Web Services (AWS) Cloud. You can use this integration to build scalable data architectures on AWS, unlocking new possibilities for your applications.

## Overview
<a name="overview"></a>

This guide provides a comprehensive overview of Aurora PostgreSQL-Compatible integration with AWS services and heterogeneous databases. If you currently run on Oracle Database or Microsoft SQL Server, explore Aurora PostgreSQL-Compatible features that are equivalent to linked servers, database links, and external tables. By using this guidance, you can also do the following:
+ Integrate with services such as Amazon Simple Storage Service (Amazon S3), AWS Lambda, Amazon CloudWatch Logs, and Amazon Redshift.
+ Avoid design mistakes that might lead to errors or performance issues.
+ Make informed decisions when integrating Aurora PostgreSQL-Compatible with other databases and AWS services.

### Connecting to remote and heterogeneous databases
<a name="connecting-to-remote-and-heterogeneous-databases.efe0abe6-39f7-5830-9670-8b3c1757a2b1"></a>

A key strength of Aurora PostgreSQL-Compatible is its ability to connect to remote [PostgreSQL](remote-postgresql-databases.md), [SQL Server](heterogeneous-databases.md#tds-fdw), Oracle, and MySQL databases by using foreign data wrappers (FDWs). These wrappers include `postgres_fdw`, `oracle_fdw`, `tds_fdw` (for SQL Server), and `mysql_fdw`. You can use these foreign data wrappers to query data from these multiple sources directly.

### Logging
<a name="logging.2e29b64b-8364-5629-98c5-7e477a0130e1"></a>

Aurora PostgreSQL-Compatible also integrates with [Amazon CloudWatch Logs](cloudwatch-logs.md) by using the `log_fdw` extension. You can use `log_fdw` to query and analyze PostgreSQL log files directly from the database. This integration streamlines log monitoring and analysis so that you can gain valuable insights into your database's performance, errors, and activities.

### Connecting to storage
<a name="connecting-to-storage.c1afc69a-26f7-5000-828a-42fc4819c003"></a>

The `aws_s3` extension integrates with [Amazon S3](amazon-s3.md) for data imports, exports, backups, and archiving. By supporting data movement between Aurora PostgreSQL-Compatible and Amazon S3, the `aws_s3` extension enables efficient data ingestion, backup, and archiving processes.

### Serverless compute
<a name="serverless-compute.74e451c5-abdc-5a5a-9994-060351fb6971"></a>

You can use the `aws_lambda` extension to improve performance and cost efficiency by offloading compute-intensive tasks to serverless [AWS Lambda](aws-lambda-integration.md) functions. Lambda supports complex computations, data transformations, and integrations with other AWS services directly from your Aurora PostgreSQL-Compatible database, without the need for dedicated compute resources.

### Integrations for analytics
<a name="integrations-for-analytics.8af66cd2-193c-555e-8fb9-500568a07b27"></a>

To facilitate data migration and ETL (extract, transform, and load) processes, Aurora PostgreSQL-Compatible can integrate with services such as [AWS Database Migration Service (AWS DMS)](migration.md) and [AWS Glue](analytics-aws-glue.md). AWS DMS supports the migration of databases to Aurora PostgreSQL-Compatible. AWS Glue helps you to build robust data-processing pipelines for transforming and loading data from various sources into Aurora PostgreSQL-Compatible or other AWS services.

For a data warehousing solution, Aurora PostgreSQL-Compatible can integrate with [Amazon Redshift](amazon-redshift.md). By acting as a data source or staging area for Amazon Redshift, Aurora PostgreSQL-Compatible supports advanced analytics and reporting capabilities. You can use these capabilities to derive valuable insights from your data.

Whether you're migrating existing workloads, building hybrid architectures, or developing new data-driven applications, the integration capabilities of Aurora PostgreSQL-Compatible help you to create scalable, high-performance, and cost-effective solutions.

### Additional extensions for integrating with AWS services
<a name="additional-extensions-for-integrating-with-9999999999999999aws-services-.26b6cd21-b750-5bc2-bb6f-c9e8079792fb"></a>

PostgreSQL lists various data wrappers for connecting to files, NoSQL databases, specific database systems. For more information, see the [PostgreSQL documentation](https://wiki.postgresql.org/wiki/Foreign_data_wrappers).

## Objectives
<a name="objectives"></a>

This guide helps new customers, especially those who are migrating from Oracle or Microsoft SQL Server, to achieve the following:
+ Find equivalent features on AWS. Aurora PostgreSQL-Compatible provides functional equivalents to linked servers, database links, and external tables.
+ Design systems and batch jobs that integrate with and connect to heterogeneous databases and AWS services.
+ Avoid common design pitfalls and optimize infrastructure implementations.
