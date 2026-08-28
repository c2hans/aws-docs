---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.managed-policy.html
---

# Attaching the AmazonRDSPerformanceInsightsReadOnly policy to an IAM principal
<a name="USER_PerfInsights.access-control.managed-policy"></a>

`AmazonRDSPerformanceInsightsReadOnly` is an AWS managed policy that grants access to all read-only operations of the Amazon RDS Database Insights API.

If you attach `AmazonRDSPerformanceInsightsReadOnly` to a permission set or role, you must also attach the following CloudWatch permissions:
+ `GetMetricStatistics`
+ `ListMetrics`
+ `GetMetricData`

With these permissions, the recipient can use Database Insights with other console features.

 For more information about CloudWatch permissions, see [Amazon CloudWatch permissions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html).

For more information about `AmazonRDSPerformanceInsightsReadOnly`, see [AWS managed policy: AmazonRDSPerformanceInsightsReadOnly](rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSPerformanceInsightsReadOnly).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
