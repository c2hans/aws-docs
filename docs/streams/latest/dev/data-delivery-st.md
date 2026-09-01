---
source_url: https://docs.aws.amazon.com/streams/latest/dev/data-delivery-st.html
---

# Streaming tables
<a name="data-delivery-st"></a>

 Streaming tables continuously delivers records from a Amazon Kinesis Data Streams stream into streaming tables on Apache Iceberg backed by Amazon S3 Tables. As data arrives, it is automatically converted to optimized Apache Parquet format with inline compaction, and becomes queryable through engines such as Amazon Athena, Amazon EMR, and Amazon Managed Service for Apache Flink. This capability requires a schema in AWS Glue Schema Registry and a dead-letter queue.

**Topics**
+ [How streaming table delivery works](data-delivery-st-about.md)
+ [Getting started with streaming tables](data-delivery-st-getting-started.md)
+ [Manage streaming table deliveries](data-delivery-st-manage.md)
+ [Iceberg behaviors for streaming table](data-delivery-st-iceberg.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query streams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
