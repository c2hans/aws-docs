---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/sentinelone-setup.html
---

# SentinelOne Singularity Endpoint integration configuration
<a name="sentinelone-setup"></a>

To integrate SentinelOne Singularity Endpoint with CloudWatch Logs, you must configure both the source and the pipeline. First, set up your SentinelOne source by configuring Amazon S3 and Amazon SQS to receive endpoint logs. Then, configure the CloudWatch pipeline to ingest the data from your source into CloudWatch Logs.

**Topics**
+ [Source configuration for SentinelOne](sentinelone-source-setup.md)
+ [CloudWatch pipelines configuration for SentinelOne](sentinelone-pipeline-setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
