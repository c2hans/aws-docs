---
source_url: https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-monitoring.html
---

# Monitoring Lambda Managed Instances
<a name="lambda-managed-instances-monitoring"></a>

Lambda provides two types of monitoring data for your capacity providers: metrics and system logs. Together, these give you visibility into resource utilization, instance lifecycle events, and operational issues.
+ **Metrics** – Lambda automatically publishes CloudWatch metrics for your capacity providers to help you monitor resource utilization, track costs, and optimize performance. For more information, see [CloudWatch metrics for Lambda Managed Instances](lambda-managed-instances-monitoring-metrics.md).
+ **System logs** – Lambda automatically sends system logs to CloudWatch Logs that record instance lifecycle events and errors for your capacity provider. For more information, see [Capacity provider system logs for Lambda Managed Instances](lambda-managed-instances-monitoring-system-logs.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
