---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-get-customize-monitoring.html
---

# Customize monitoring in Accelerate
<a name="acc-get-customize-monitoring"></a>

To customize monitoring of your cloud resources based on your application needs:

1. Create a custom monitoring policy. See [Modifying the Accelerate alarm default configuration](acc-mem-modify-default.md).

1. Apply a custom policy to resources using tags. See [Monitoring in Accelerate](acc-tag-req-mon.md)

1. Route alerts to the resource owner. See [Tag-based alert notification](how-monitoring-works.md#how-mon-works-alert-notes-tags).

 You can use the following CloudWatch dashboards to explore how many of your resources are targeted by AMS monitoring and tagging, and how many are not. In your account, navigate to the CloudWatch dashboards console, and select one of the following:
+ AMS-Alarm-Manager-Reporting-Dashboard
+ AMS-Resource-Tagger-Reporting-Dashboard

For a complete description of the dashboard metrics, see:
+ [Viewing the number of resources managed by Resource Tagger](acc-rt-using.md#acc-rt-number-of-resources)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
