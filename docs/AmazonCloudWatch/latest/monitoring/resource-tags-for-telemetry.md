---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/resource-tags-for-telemetry.html
---

# Resource tags for telemetry
<a name="resource-tags-for-telemetry"></a>

Use Amazon CloudWatch to enrich your AWS infrastructure metrics and CloudWatch Logs with AWS resource tags. You can set up comprehensive monitoring with CloudWatch metrics and alarms using tags. This helps monitor cloud infrastructure at scale by adapting alarms and metrics analysis as resources change.

To begin discovering and visualizing your telemetry by tags, you must first enable the resource tags for telemetry feature for your AWS account. When you enable this feature, Resource Explorer creates an AWS index and managed view that indexes and discovers resources and tags in your account. For more information, see [Index](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Index.html) in the Resource Explorer API reference guide and [AWS managed views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html) in the Resource Explorer user guide. CloudWatch uses this information to enrich your AWS infrastructure metrics and log events with related AWS resource tags. You can enable **resource tags for telemetry** at no additional cost.

**Topics**
+ [Enable resource tags on telemetry](EnableResourceTagsOnTelemetry.md)
+ [Using resource tags for telemetry](UsingResourceTagsForTelemetry.md)
+ [Disable resource tags on telemetry](DisableResourceTagsOnTelemetry.md)
+ [Troubleshooting](ResourceTagsTelemetryTroubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
