---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/doc-history.html
---

# Document history

The following table describes significant changes to this guide.

|
|
| Change | Description | Date |
| --- |--- |--- |
| Major update | Updates throughout to reflect the latest versions of Apache Iceberg and AWS integrations. Added Amazon S3 Tables coverage across the guide — see [Hosting Iceberg tables on AWS: self-managed vs. Amazon S3 Tables](apache-iceberg-on-aws-self-managed-vs-s3-tables.md) and [Getting started with Amazon S3 Tables](getting-started-with-amazon-s3-tables.md). Added Iceberg format version 3 coverage in [Working with Iceberg table format specification version 3](table-spec-v3.md). Added Iceberg V3 feature-support matrices and Amazon S3 Tables integration to every pre-existing engine and service chapter. Added new engine and integration chapters: [Working with Iceberg tables by using Amazon Redshift](working-with-iceberg-tables-by-using-amazon-redshift.md), [Streaming directly to Iceberg from Amazon Kinesis Data Streams and Amazon MSK](streaming-directly-to-iceberg-from-kinesis-and-msk.md), [Apache Iceberg materialized views in AWS Glue Data Catalog](apache-iceberg-materialized-views-in-aws-glue-data-catalog.md), and [Catalog federation for Apache Iceberg tables in the AWS Glue Data Catalog](catalog-federation-for-apache-iceberg-tables.md). Enhanced [Migrating existing tables to Iceberg](table-migration.md) with coverage of Apache Hudi and Delta Lake tables as sources, plus the new [Managed migration to Amazon S3 Tables](managed-migration-to-amazon-s3-tables.md) path. Restructured and expanded [Best practices for optimizing Iceberg workloads](best-practices.md), including dedicated coverage of the three execution options for table maintenance on AWS in [Maintaining Iceberg tables](maintaining-iceberg-tables.md): [Self-managed maintenance](self-managed-maintenance.md), [Maintenance with the AWS Glue Data Catalog table optimizer](maintenance-with-the-aws-glue-data-catalog-table-optimizer.md), and [Maintenance in Amazon S3 Tables](maintenance-in-amazon-s3-tables.md). Added [Measuring data quality for Iceberg tables](measuring-data-quality-for-iceberg-tables.md). Enhanced [Reference architectures](reference-architectures.md). | November, 2026 |
| New section | Added information about [working with Iceberg table format specification version 3](table-spec-v3.md). | November 26, 2025 |
| Correction | Corrected information about `gc.enabled` settings in the [snapshot procedure](hive-tables-parquet-orc-or-avro.md) section. | October 24, 2025 |
| Additions | Added new sections on working with Iceberg tables by using [Trino](working-with-iceberg-tables-by-using-trino-amazon-emr.md) and [PyIceberg](iceberg-pyiceberg.md), and expanded the section on [migrating tables to Iceberg](table-migration.md). | August 12, 2025 |
| Updates | Enhanced and clarified information throughout the guide to reflect the latest versions of AWS Glue, Amazon EMR, and Apache Iceberg. | July 14, 2025 |
| Additions | Added a [new section](iceberg-firehose.md) on working with Iceberg tables by using Amazon Data Firehose. | February 20, 2025 |
| Initial publication | — | April 30, 2024 |
