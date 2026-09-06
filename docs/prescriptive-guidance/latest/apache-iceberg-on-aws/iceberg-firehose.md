---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/iceberg-firehose.html
---

# Working with Iceberg tables by using Amazon Data Firehose
<a name="iceberg-firehose"></a>

Amazon Data Firehose is a serverless, no-code service for delivering data streams from over 20 sources such as AWS WAF logs, Amazon CloudWatch Logs, AWS IoT, Amazon Kinesis Data Streams, and Amazon Managed Streaming for Apache Kafka (Amazon MSK) into destinations such as Amazon S3, Amazon Redshift, Snowflake, and Splunk.

You can use Firehose to directly deliver streaming data to Apache Iceberg tables in Amazon S3. Using Firehose, you can route records from a single stream into different Apache Iceberg tables, and automatically apply insert, update, and delete operations to records in the tables. Firehose guarantees exactly-once delivery to Iceberg tables. This feature requires using the AWS Glue Data Catalog.

Firehose can also directly deliver streaming data to Amazon S3 tables. These tables provide storage that is optimized for large-scale analytics workloads, and include features that continuously improve query performance and reduce storage costs for tabular data.

For information about how to set up a Firehose stream to deliver data to Apache Iceberg tables, see [Set up the Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/apache-iceberg-stream.html) in the Firehose documentation or the blog post [Stream real-time data into Apache Iceberg tables in Amazon S3 using Amazon Data Firehose](https://aws.amazon.com/blogs/big-data/stream-real-time-data-into-apache-iceberg-tables-in-amazon-s3-using-amazon-data-firehose/).
