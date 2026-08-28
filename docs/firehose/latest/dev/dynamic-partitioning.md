---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/dynamic-partitioning.html
---

# Partition streaming data in Amazon Data Firehose
<a name="dynamic-partitioning"></a>

Dynamic partitioning enables you to continuously partition streaming data in Firehose by using keys within data (for example, `customer_id` or `transaction_id`) and then deliver the data grouped by these keys into corresponding Amazon Simple Storage Service (Amazon S3) prefixes. This makes it easier to run high performance, cost-efficient analytics on streaming data in Amazon S3 using various services such as Amazon Athena, Amazon EMR, Amazon Redshift Spectrum, and Amazon QuickSight. In addition, AWS Glue can perform more sophisticated extract, transform, and load (ETL) jobs after the dynamically partitioned streaming data is delivered to Amazon S3, in use-cases where additional processing is required.

Partitioning your data minimizes the amount of data scanned, optimizes performance, and reduces costs of your analytics queries on Amazon S3. It also increases granular access to your data. Firehose streams are traditionally used in order to capture and load data into Amazon S3. To partition a streaming data set for Amazon S3-based analytics, you would need to run partitioning applications between Amazon S3 buckets prior to making the data available for analysis, which could become complicated or costly.

With dynamic partitioning, Firehose continuously groups in-transit data using dynamically or statically defined data keys, and delivers the data to individual Amazon S3 prefixes by key. This reduces time-to-insight by minutes or hours. It also reduces costs and simplifies architectures.

**Topics**
+ [Enable dynamic partitioning in Amazon Data Firehose](dynamic-partitioning-enable.md)
+ [Understand partitioning keys](dynamic-partitioning-partitioning-keys.md)
+ [Use Amazon S3 bucket prefix to deliver data](dynamic-partitioning-s3bucketprefix.md)
+ [Apply dynamic partitioning to aggregated data](dynamic-partitioning-multirecord-deaggergation.md)
+ [Troubleshoot dynamic partitioning errors](dynamic-partitioning-error-handling.md)
+ [Buffer data for dynamic partitioning](buffering.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
