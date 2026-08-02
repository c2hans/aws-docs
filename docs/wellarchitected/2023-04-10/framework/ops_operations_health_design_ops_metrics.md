---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_operations_health_design_ops_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS09-BP02 Define operations metrics
<a name="ops_operations_health_design_ops_metrics"></a>

 Define operations metrics to measure the achievement of KPIs (for example, successful deployments, and failed deployments). Define operations metrics to measure the health of operations activities (for example, mean time to detect an incident (MTTD), and mean time to recovery (MTTR) from an incident). Evaluate metrics to determine if operations are achieving desired outcomes, and to understand the health of your operations activities.

 **Common anti-patterns:**
+  Your operations metrics are based on what the team thinks is reasonable.
+  You have errors in your metrics calculations that will yield incorrect results.
+  You don't have any metrics defined for your operations activities.

 **Benefits of establishing this best practice:** By defining and evaluating operations metrics you can determine the health of your operations activities and measure the achievement of business outcomes.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Define operations metrics: Define operations metrics to measure the achievement of KPIs. Define operations metrics to measure the health of operations and its activities. Evaluate metrics to determine if operations are achieving desired outcomes, and to understand the health of the operations.
  +  [Publish custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
  +  [Searching and filtering log data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)
  +  [Amazon CloudWatch metrics and dimensions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Answers: Centralized Logging](https://aws.amazon.com/answers/logging/centralized-logging/)
+  [Amazon CloudWatch metrics and dimensions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html)
+  [Detect and React to Changes in Pipeline State with Amazon CloudWatch Events](https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html)
+  [Publish custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
+  [Searching and filtering log data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)

 **Related videos:**
+  Build a Monitoring Plan
