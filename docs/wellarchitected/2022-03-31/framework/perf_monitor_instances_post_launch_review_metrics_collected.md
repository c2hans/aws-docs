---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_monitor_instances_post_launch_review_metrics_collected.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF07-BP05 Review metrics at regular intervals
<a name="perf_monitor_instances_post_launch_review_metrics_collected"></a>

 As routine maintenance, or in response to events or incidents, review which metrics are collected. Use these reviews to identify which metrics were essential in addressing issues and which additional metrics, if they were being tracked, would help to identify, address, or prevent issues.

 As part of responding to incidents or events, evaluate which metrics were helpful in addressing the issue and which metrics could have helped that are not currently being tracked. Use this to improve the quality of metrics you collect so that you can prevent or more quickly resolve future incidents.

 **Common anti-patterns:**
+  You allow metrics to stay in an alarm state for an extended period of time.
+  You create alarms that are not actionable by an automation system.

 **Benefits of establishing this best practice:** Continually review metrics that are being collected to ensure that they properly identify, address, or prevent issues. Metrics can also become stale if you let them stay in an alarm state for an extended period of time.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Constantly improve metric collection and monitoring: As part of responding to incidents or events, evaluate which metrics were helpful in addressing the issue and which metrics could have helped that are not currently being tracked. Use this method to improve the quality of metrics you collect so that you can prevent or more quickly resolve future incidents.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [Collect metrics and logs from Amazon EC2 Instances and on-premises servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html?ref=wellarchitected)
+  [Monitoring, Logging, and Performance APN Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance)
+  [X-Ray Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

 **Related videos:**
+  [Cut through the chaos: Gain operational visibility and insight (MGT301-R1)](https://www.youtube.com/watch?v=nLYGbotqHd0)
+  [Application Performance Management on AWS](https://www.youtube.com/watch?v=5T4stR-HFas&ref=wellarchitected)
+  [Build a Monitoring Plan](https://www.youtube.com/watch?v=OMmiGETJpfU&ref=wellarchitected)

 **Related examples:**
+  [Creating a dashboard with Quick](https://github.com/aws-samples/amazon-quicksight-sdk-proserve)
+  [Level 100: Monitoring with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_with_cloudwatch_dashboards/)
