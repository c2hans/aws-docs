---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.access-control.FullAccess-managed-policy.html
---

# Attaching the AmazonRDSPerformanceInsightsFullAccess policy to an IAM principal
<a name="USER_PerfInsights.access-control.FullAccess-managed-policy"></a>

`AmazonRDSPerformanceInsightsFullAccess` is an AWS managed policy that grants access to all operations of the Amazon RDS Database Insights API.

If you attach `AmazonRDSPerformanceInsightsFullAccess` to a permission set or role, you must also attach the following CloudWatch permissions:
+ `GetMetricStatistics`
+ `ListMetrics`
+ `GetMetricData`

With these permissions, the recipient can use Database Insights with other console features.

 For more information about CloudWatch permissions, see [Amazon CloudWatch permissions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html).

For more information about `AmazonRDSPerformanceInsightsFullAccess`, see [AWS managed policy: AmazonRDSPerformanceInsightsFullAccess](rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSPerformanceInsightsFullAccess).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
