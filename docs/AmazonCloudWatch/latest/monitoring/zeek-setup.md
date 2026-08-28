---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/zeek-setup.html
---

# Zeek integration configuration
<a name="zeek-setup"></a>

Zeek is an open-source network security monitoring platform widely used for analyzing network traffic and generating detailed logs about network activities across an organization's infrastructure. It passively monitors network traffic and provides deep visibility into communications by producing structured logs for multiple network protocols and security-relevant events. CloudWatch pipelines allow ingestion of Zeek log data into CloudWatch Logs, providing scalable collection, processing, normalization, and integration with downstream AWS security and monitoring services.

**Topics**
+ [Source configuration for Zeek](zeek-source-setup.md)
+ [CloudWatch pipelines configuration for Zeek](zeek-pipeline-setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
