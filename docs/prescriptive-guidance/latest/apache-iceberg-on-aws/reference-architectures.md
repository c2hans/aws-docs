---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/reference-architectures.html
---

# Reference architectures
<a name="reference-architectures"></a>

This section provides examples of how to apply best practices in different use cases such as batch ingestion and a data lake that combines batch and streaming data ingestion.

## Nightly batch ingestion
<a name="batch-ingestion"></a>

For this hypothetical use case, let's say that your Iceberg table ingests credit card transactions on a nightly basis. Each batch contains only incremental updates, which must be merged into the target table. Several times per year, full historical data is received. For this scenario, we recommend the following architecture and configurations.

**Note**
This is just an example. The optimal configuration depends on your data and requirements.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/108be8b9-8667-4e45-a026-5ce532c8b621.png)

Recommendations:
+ File size: 128 MB, because Apache Spark tasks process data in 128 MB chunks.
+ Write type: copy-on-write. As detailed earlier in this guide, this approach helps ensure that data is written in a read-optimized fashion.
+ Partition variables: year/month/day. In our hypothetical use case, we query recent data most frequently, although we occasionally run full table scans for the past two years of data. The goal of partitioning is to drive fast read operations based on the requirements of the use case.
+ Sort order: timestamp
+ Data catalog: AWS Glue Data Catalog

## Data lake that combines batch and near real-time ingestion
<a name="batch-real-time-ingestion"></a>

You can provision a data lake on Amazon S3 that shares batch and streaming data across accounts and Regions. For an architecture diagram and details, see the AWS blog post [Build a transactional data lake using Apache Iceberg, AWS Glue, and cross-account data shares using AWS Lake Formation and Amazon Athena](https://aws.amazon.com/blogs/big-data/build-a-transactional-data-lake-using-apache-iceberg-aws-glue-and-cross-account-data-shares-using-aws-lake-formation-and-amazon-athena/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
