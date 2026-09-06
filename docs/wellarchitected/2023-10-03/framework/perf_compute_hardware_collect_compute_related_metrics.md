---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_compute_hardware_collect_compute_related_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF02-BP03 Collect compute-related metrics
<a name="perf_compute_hardware_collect_compute_related_metrics"></a>

 Record and track compute-related metrics to better understand how your compute resources are performing and improve their performance and their utilization.

 **Common anti-patterns:**
+  You only use manual log file searching for metrics.
+  You only use the default metrics recorded by your monitoring software.
+  You only review metrics when there is an issue.

 **Benefits of establishing this best practice:** Collecting performance-related metrics will help you align application performance with business requirements to ensure that you are meeting your workload needs. It can also help you continually improve the resource performance and utilization in your workload.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Cloud workloads can generate large volumes of data such as metrics, logs, and events. In the AWS Cloud, collecting metrics is a crucial step to improve security, cost efficiency, performance, and sustainability. AWS provides a wide range of performance-related metrics using monitoring services such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to provide you with valuable insights. Metrics such as CPU utilization, memory utilization, disk I/O, and network inbound and outbound can provide insight into utilization levels or performance bottlenecks. Use these metrics as part of a data-driven approach to actively tune and optimize your workload's resources.  In an ideal case, you should collect all metrics related to your compute resources in a single platform with retention policies implemented to support cost and operational goals.

## Implementation steps
<a name="implementation-steps"></a>

1.  Identify which performance-related metrics are relevant to your workload. You should collect metrics around resource utilization and the way your cloud workload is operating (like response time and throughput).

   1.  [Amazon EC2 default metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)

   1.  [Amazon ECS default metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html)

   1.  [Amazon EKS default metrics](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/kubernetes-eks-metrics.html)

   1.  [Lambda default metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-access-metrics.html)

   1.  [Amazon EC2 memory and disk metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html)

1.  Choose and set up the right logging and monitoring solution for your workload.

   1.  [AWS native Observability](https://catalog.workshops.aws/observability/en-US/aws-native)

   1.  [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/)

   1.  [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/grafana/latest/userguide/prometheus-data-source.html)

1.  Define the required filter and aggregation for the metrics based on your workload requirements.

   1.  [Quantify custom application metrics with Amazon CloudWatch Logs and metric filters](https://aws.amazon.com/blogs/mt/quantify-custom-application-metrics-with-amazon-cloudwatch-logs-and-metric-filters/)

   1.  [Collect custom metrics with Amazon CloudWatch strategic tagging](https://aws.amazon.com/blogs/infrastructure-and-automation/collect-custom-metrics-with-amazon-cloudwatch-strategic-tagging/)

1.  Configure data retention policies for your metrics to match your security and operational goals.

   1.  [Default data retention for CloudWatch metrics](https://aws.amazon.com/cloudwatch/faqs/#AWS_resource_.26_custom_metrics_monitoring)

   1.  [Default data retention for CloudWatch Logs](https://aws.amazon.com/cloudwatch/faqs/#Log_management)

1.  If required, create alarms and notifications for your metrics to help you proactively respond to performance-related issues.

   1.  [Create alarms for custom metrics using Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-alarms-for-custom-metrics-using-amazon-cloudwatch-anomaly-detection.html)

   1.  [Create metrics and alarms for specific web pages with Amazon CloudWatch RUM](https://aws.amazon.com/blogs/mt/create-metrics-and-alarms-for-specific-web-pages-amazon-cloudwatch-rum/)

1.  Use automation to deploy your metric and log aggregation agents.

   1.  [AWS Systems Manager automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html?ref=wellarchitected)

   1.  [OpenTelemetry Collector](https://aws-otel.github.io/docs/getting-started/collector)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon CloudWatch documentation](https://docs.aws.amazon.com/cloudwatch/index.html?ref=wellarchitected)
+  [Collect metrics and logs from Amazon EC2 instances and on-premises servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html?ref=wellarchitected)
+  [Accessing Amazon CloudWatch Logs for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-logs.html?ref=wellarchitected)
+  [Using CloudWatch Logs with container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_cloudwatch_logs.html?ref=wellarchitected)
+  [Publish custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html?ref=wellarchitected)
+  [AWS Answers: Centralized Logging](https://aws.amazon.com/answers/logging/centralized-logging/?ref=wellarchitected)
+  [AWS Services That Publish CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html?ref=wellarchitected)
+  [Monitoring Amazon EKS on AWS Fargate](https://aws.amazon.com/blogs/containers/monitoring-amazon-eks-on-aws-fargate-using-prometheus-and-grafana/)

 **Related videos:**
+  [Application Performance Management on AWS](https://www.youtube.com/watch?v=5T4stR-HFas&ref=wellarchitected)

 **Related examples:**
+  [Level 100: Monitoring with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_with_cloudwatch_dashboards/)
+  [Level 100: Monitoring Windows EC2 instance with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_windows_ec2_cloudwatch/)
+  [Level 100: Monitoring an Amazon Linux EC2 instance with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_linux_ec2_cloudwatch/)
