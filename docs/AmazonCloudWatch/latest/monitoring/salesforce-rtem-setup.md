---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/salesforce-rtem-setup.html
---

# Salesforce RTEM integration configuration
<a name="salesforce-rtem-setup"></a>

Salesforce is a cloud-based Customer Relationship Management (CRM) platform that provides business applications for sales, service, marketing, and IT operations. It generates real-time security events through the [Pub/Sub API](https://developer.salesforce.com/docs/platform/pub-sub-api/overview) (gRPC) covering login activity, API usage, file events, and data access across 19\+ event channels with sub-second delivery. CloudWatch pipelines use the Salesforce Pub/Sub API to stream these events into CloudWatch Logs.

**Topics**
+ [Source configuration for Salesforce RTEM](salesforce-rtem-source-config.md)
+ [CloudWatch pipelines configuration for Salesforce RTEM](salesforce-rtem-pipeline-setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
