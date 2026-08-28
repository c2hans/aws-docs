---
source_url: https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-alarm-definition.html
---

# Alarm definition
<a name="idr-gs-alarm-definition"></a>

When onboarding your alarms to AWS Incident Detection and Response, you're responsible for defining the metrics and alarm configurations that provide visibility into the performance of your applications. As part of this process, you must also identify the teams within your organization who is responsible for responding to these alarms.

When preparing alarms, we recommend the following best practices:
+ Alarms only enter the "Alarm" state when there is ongoing critical impact to your monitored workload that requires immediate attention from your team and AWS. Alarms that trigger and don't automatically recover require your teams to join an incident bridge with AWS Incident Detection and Response.
+ Ensure the contact information you provide allows AWS Incident Detection and Response to reliably engage the appropriate teams within your organization to an incident bridge 24/7.

**Key outputs**
+ A list of alarms and contact details, which you provide to AWS Incident Detection and Response using the [IDR CLI](https://github.com/awslabs/CLI-for-AWS-Incident-Detection-and-Response).

For more information about defining and ingesting Amazon CloudWatch alarms see [Ingesting CloudWatch alarms](idr-gs-ingest-cw-alarms.md).

For more information about ingesting third party Application Performance Monitoring alarms see [Ingesting Third Party Application Performance Monitoring Alarms](idr-gs-ingest-apm-alarms.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Incident Detection Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IDR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
