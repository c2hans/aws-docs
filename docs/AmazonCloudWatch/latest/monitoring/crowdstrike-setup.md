---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/crowdstrike-setup.html
---

# CrowdStrike integration configuration
<a name="crowdstrike-setup"></a>

To integrate CrowdStrike Falcon Data Replicator with CloudWatch Logs, you must configure both the source and the pipeline. First, set up your CrowdStrike source by configuring Amazon S3 and Amazon SQS to receive FDR data. Then, configure the CloudWatch pipeline to ingest the data from your source into CloudWatch Logs.

**Topics**
+ [Source configuration for CrowdStrike](crowdstrike-source-setup.md)
+ [CloudWatch pipelines configuration for CrowdStrike](crowdstrike-pipeline-setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
