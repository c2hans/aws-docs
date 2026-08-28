---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/export-unload-limits.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Limits for UNLOAD from Timestream for LiveAnalytics
<a name="export-unload-limits"></a>

Following are limits related to the `UNLOAD` command.
+ Concurrency for queries using the `UNLOAD` statement is 1 query per second (QPS). Exceeding the query rate might result in throttling.
+ Queries containing `UNLOAD` statement can export at most 100 partitions per query. We recommend to check the distinct count of the selected column before using it to partition the exported data.
+ Queries containing `UNLOAD` statement time out after 60 minutes.
+ The maximum size of the files that the `UNLOAD` statement creates in Amazon S3 is 78 GB.

For other limits for Timestream for LiveAnalytics, see [Quotas](ts-limits.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
