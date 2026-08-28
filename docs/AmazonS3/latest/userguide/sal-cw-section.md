---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/sal-cw-section.html
---

# Delivering logs to Amazon CloudWatch Logs
<a name="sal-cw-section"></a>

When you deliver server access logs to Amazon CloudWatch Logs, you get structured JSON logs that you can query interactively with CloudWatch Logs Insights, aggregate across accounts and Regions, and optionally mirror to S3 Tables in Apache Iceberg format for SQL analytics. You can also deliver logs to Amazon S3 in JSON or Apache Parquet format or route them through Amazon Data Firehose.

**Topics**
+ [Delivering server access logs to CloudWatch Logs](sal-cw-enabling.md)
+ [Log format in CloudWatch Logs](sal-cw-log-format.md)
+ [Managing log retention](sal-cw-retention.md)
+ [Querying logs with CloudWatch Logs Insights](sal-cw-querying-insights.md)
+ [Querying access logs in S3 Tables](sal-cw-querying-s3tables.md)
+ [Troubleshooting CloudWatch Logs delivery](sal-cw-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
