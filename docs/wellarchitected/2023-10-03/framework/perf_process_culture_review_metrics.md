---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_process_culture_review_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP07 Review metrics at regular intervals
<a name="perf_process_culture_review_metrics"></a>

 As part of routine maintenance or in response to events or incidents, review which metrics are collected. Use these reviews to identify which metrics were essential in addressing issues and which additional metrics, if they were being tracked, could help identify, address, or prevent issues.

 **Common anti-patterns:**
+  You allow metrics to stay in an alarm state for an extended period of time.
+  You create alarms that are not actionable by an automation system.

 **Benefits of establishing this best practice:** Continually review metrics that are being collected to verify that they properly identify, address, or prevent issues. Metrics can also become stale if you let them stay in an alarm state for an extended period of time.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Constantly improve metric collection and monitoring. As part of responding to incidents or events, evaluate which metrics were helpful in addressing the issue and which metrics could have helped that are not currently being tracked. Use this method to improve the quality of metrics you collect so that you can prevent, or more quickly resolve future incidents.

 As part of responding to incidents or events, evaluate which metrics were helpful in addressing the issue and which metrics could have helped that are not currently being tracked. Use this to improve the quality of metrics you collect so that you can prevent or more quickly resolve future incidents.

### Implementation steps
<a name="implementation-steps"></a>

1. Define critical performance metrics to monitor that are aligned to your workload objective.

1. Set a baseline and desirable value for each metric.

1. Set a cadence (like weekly or monthly) to review critical metrics.

1. During each review, assess trends and deviation from the baseline values. Look for any performance bottlenecks or anomalies.

1. For identified issues, conduct in-depth root cause analysis to understand the main reason behind the issue.

1. Document your findings and use strategies to deal with identified issues and bottlenecks.

1. Continually assess and improve the metrics review process.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [Collect metrics and logs from Amazon EC2 Instances and on-premises servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html?ref=wellarchitected)
+  [Monitoring, Logging, and Performance AWS Partner Network Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance)
+  [X-Ray Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

 **Related videos:**
+  [Setting up controls at scale in your AWS environment](https://www.youtube.com/watch?v=NkE9_okfPG8)
+  [How Amazon uses better metrics for improved website performance](https://www.youtube.com/watch?v=_uaaCiyJCFA&ab_channel=AWSEvents)

 **Related examples:**
+  [Creating a dashboard with Quick](https://github.com/aws-samples/amazon-quicksight-sdk-proserve)
+  [Level 100: Monitoring with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_with_cloudwatch_dashboards/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
