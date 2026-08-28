---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_workload_health_workload_metric_baselines.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS08-BP04 Establish workload metrics baselines
<a name="ops_workload_health_workload_metric_baselines"></a>

 Establish baselines for metrics to provide expected values as the basis for comparison and identification of under- and over-performing components. Identify thresholds for improvement, investigation, and intervention.

 **Common anti-patterns:**
+  A server is running at 95% CPU utilization you are asked if that is good or bad. CPU utilization on that server has not been baselined so you have no idea if that is good or bad.

 **Benefits of establishing this best practice:** By defining baseline metric values you are able to evaluate current metric values, and metric trends, to determine if action is required.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Establish baselines for workload metrics: Establish baselines for workload metrics to provide expected values as the basis for comparison.
  +  [Creating Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Creating Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
