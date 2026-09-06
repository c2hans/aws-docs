---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_monitor_instances_post_launch_generate_alarms.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF07-BP04 Use monitoring to generate alarm-based notifications
<a name="perf_monitor_instances_post_launch_generate_alarms"></a>

 Using the performance-related key performance indicators (KPIs) that you defined, use a monitoring system that generates alarms automatically when these measurements are outside expected boundaries.

 Amazon CloudWatch can collect metrics across the resources in your architecture. You can also collect and publish custom metrics to surface business or derived metrics. Use CloudWatch or a third-party monitoring service to set alarms that indicate when thresholds are breached — alarms signal that a metric is outside of the expected boundaries.

 **Common anti-patterns:**
+  You rely on staff to watch metrics and react when they see an issue.
+  You rely solely on operational runbooks, when serverless workflows could be started to accomplish the same task.

 **Benefits of establishing this best practice:** You can set alarms and automate actions based on either predefined thresholds, or on machine learning algorithms that identify anomalous behavior in your metrics. These same alarms can also start serverless workflows, which can modify performance characteristics of your workload (for example, increasing compute capacity, altering database configuration).

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Monitor metrics: Amazon CloudWatch can collect metrics across the resources in your architecture. You can collect and publish custom metrics to surface business or derived metrics. Use CloudWatch or a third-party monitoring service to set alarms that indicate when thresholds are exceeded.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [Monitoring, Logging, and Performance APN Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance)
+  [X-Ray Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
+  [Using Alarms and Alarm Actions in CloudWatch](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cw-example-using-alarm-actions.html)

 **Related videos:**
+  [AWS re:Invent 2019: Scaling up to your first 10 million users (ARC211-R)](https://www.youtube.com/watch?v=kKjm4ehYiMs&ref=wellarchitected)
+  [Cut through the chaos: Gain operational visibility and insight (MGT301-R1)](https://www.youtube.com/watch?v=nLYGbotqHd0&ref=wellarchitected)
+  [Build a Monitoring Plan](https://www.youtube.com/watch?v=OMmiGETJpfU&ref=wellarchitected)
+  [Using AWS Lambda with Amazon CloudWatch Events](https://www.youtube.com/watch?v=WDBD3JmpLqs)

 **Related examples:**
+  [Cloudwatch Logs Customize Alarms](https://github.com/awslabs/cloudwatch-logs-customize-alarms)
