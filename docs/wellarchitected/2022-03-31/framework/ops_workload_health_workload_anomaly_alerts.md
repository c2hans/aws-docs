---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_workload_health_workload_anomaly_alerts.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS08-BP07 Alert when workload anomalies are detected
<a name="ops_workload_health_workload_anomaly_alerts"></a>

 Raise an alert when workload anomalies are detected so that you can respond appropriately if necessary.

 Your analysis of your workload metrics over time may establish patterns of behavior that you can quantify sufficiently to define an event or raise an alarm in response.

 Once trained, the [CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) feature can be used to [alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html) on detected anomalies or can provide overlaid expected values onto a [graph](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph_a_metric.html#create-metric-graph) of metric data for ongoing comparison.

 **Common anti-patterns:**
+  Your retail website sales have increased suddenly and dramatically. No one is aware. No one is trying to identify what led to this surge. No one is taking action to ensure quality customer experiences under the additional load.
+  Following the application of a patch, your persistent servers are rebooting frequently, disrupting users. Your servers typically reboot up to three times but not more. No one is aware. No one is trying to identify why this is happening.

 **Benefits of establishing this best practice:** By understanding patterns of workload behavior, you can identify unexpected behavior and take action if necessary.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Alert when workload anomalies are detected: Raise an alert when workload anomalies are detected so that you can respond appropriately if required.
  +  [What is Amazon CloudWatch Events?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)
  +  [Creating Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
  +  [Invoking Lambda functions using Amazon SNS notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-lambda.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Creating Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
+  [CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
+  [Invoking Lambda functions using Amazon SNS notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-lambda.html)
+  [What is Amazon CloudWatch Events?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)
