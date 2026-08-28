---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/salesforce-elf-setup.html
---

# Salesforce ELF integration configuration
<a name="salesforce-elf-setup"></a>

Salesforce is a cloud-based Customer Relationship Management (CRM) platform that provides business applications for sales, service, marketing, and IT operations. It generates detailed operational logs through Event Log Files (ELF) including login activity, API usage, report execution, and administrative changes, with hourly or daily granularity, along with audit trail events. CloudWatch pipelines use the Salesforce REST API to poll these logs for ingestion into CloudWatch Logs.

**Topics**
+ [Source configuration for Salesforce ELF](salesforce-elf-source-config.md)
+ [CloudWatch pipelines configuration for Salesforce ELF](salesforce-elf-pipeline-setup.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
