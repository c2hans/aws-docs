---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_operations_health_ops_anomaly_alerts.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS09-BP07 Alert when operations anomalies are detected
<a name="ops_operations_health_ops_anomaly_alerts"></a>

 Raise an alert when operations anomalies are detected so that you can respond appropriately if necessary.

 Your analysis of your operations metrics over time may established patterns of behavior that you can quantify sufficiently to define an event or raise an alarm in response.

 Once trained, the [CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) feature can be used to [alarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html) on detected anomalies or can provide overlaid expected values onto a [graph](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph_a_metric.html#create-metric-graph) of metric data for ongoing comparison.

 [Amazon DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html) can be used to identify anomalous behavior through event correlation, log analysis, and applying machine learning to analyze your workload telemetry. The [insights](https://docs.aws.amazon.com/devops-guru/latest/userguide/understanding-insights-console.html) gained are presented with the relevant data and recommendations.

 **Common anti-patterns:**
+  You are applying a patch to your fleet of instances. You tested the patch successfully in the test environment. The patch is failing for a large percentage of instances in your fleet. You do nothing.
+  You note that there are deployments starting Friday end of day. Your organization has predefined maintenance windows on Tuesdays and Thursdays. You do nothing.

 **Benefits of establishing this best practice:** By understanding patterns of operations behavior you can identify unexpected behavior and take action if necessary.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Alert when operations anomalies are detected: Raise an alert when operations anomalies are detected so that you can respond appropriately if required.
  +  [What is Amazon CloudWatch Events?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)
  +  [Creating Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
  +  [Invoking Lambda functions using Amazon SNS notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-lambda.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/welcome.html)
+  [CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
+  [Creating Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
+  [Detect and React to Changes in Pipeline State with Amazon CloudWatch Events](https://docs.aws.amazon.com/codepipeline/latest/userguide/detect-state-changes-cloudwatch-events.html)
+  [Invoking Lambda functions using Amazon SNS notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-lambda.html)
+  [What is Amazon CloudWatch Events?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)
