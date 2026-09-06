---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_monitor_instances_post_launch_record_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF07-BP01 Record performance-related metrics
<a name="perf_monitor_instances_post_launch_record_metrics"></a>

 Use a monitoring and observability service to record performance-related metrics. Examples of metrics include record database transactions, slow queries, I/O latency, HTTP request throughput, service latency, or other key data.

 Identify the performance metrics that matter for your workload and record them. This data is an important part of being able to identify which components are impacting overall performance or efficiency of the workload.

 Working back from the customer experience, identify metrics that matter. For each metric, identify the target, measurement approach, and priority. Use these to build alarms and notifications to proactively address performance-related issues.

 **Common anti-patterns:**
+  You only monitor operating system level metrics to gain insight into your workload.
+  You architect your compute needs for peak workload requirements.

 **Benefits of establishing this best practice:** To optimize performance and resource utilization, you need a unified operational view of your key performance indicators. You can create dashboards and perform metric math on your data to derive operational and utilization insights.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Identify the relevant performance metrics for your workload and record them. This data helps identify which components are impacting overall performance or efficiency of your workload.

 Identify performance metrics: Use the customer experience to identify the most important metrics. For each metric, identify the target, measurement approach, and priority. Use these data points to build alarms and notifications to proactively address performance-related issues.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [CloudWatch Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
+  [Collect metrics and logs from Amazon EC2 Instances and on-premises servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html?ref=wellarchitected)
+  [Publish custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html?ref=wellarchitected)
+  [Monitoring, Logging, and Performance APN Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance)
+  [X-Ray Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
+  [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)

 **Related videos:**
+  [Cut through the chaos: Gain operational visibility and insight (MGT301-R1)](https://www.youtube.com/watch?v=nLYGbotqHd0)
+  [Application Performance Management on AWS](https://www.youtube.com/watch?v=5T4stR-HFas&ref=wellarchitected)
+  [Build a Monitoring Plan](https://www.youtube.com/watch?v=OMmiGETJpfU&ref=wellarchitected)

 **Related examples:**
+  [Level 100: Monitoring with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_with_cloudwatch_dashboards/)
+  [Level 100: Monitoring Windows EC2 instance with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_windows_ec2_cloudwatch/)
+  [Level 100: Monitoring an Amazon Linux EC2 instance with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_linux_ec2_cloudwatch/)
