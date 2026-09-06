---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_select_compute_collect_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF02-BP03 Collect compute-related metrics
<a name="perf_select_compute_collect_metrics"></a>

To understand how your compute resources are performing, you must record and track the utilization of various systems. This data can be used to make more accurate determinations about resource requirements.

 Workloads can generate large volumes of data such as metrics, logs, and events. Determine if your existing storage, monitoring, and observability service can manage the data generated. Identify which metrics reflect resource utilization and can be collected, aggregated, and correlated on a single platform across. Those metrics should represent all your workload resources, applications, and services, so you can easily gain system-wide visibility and quickly identify performance improvement opportunities and issues.

 **Desired outcome:** All metrics related to the compute-related resources are identified, collected, aggregated, and correlated on a single platform with retention implemented to support cost and operational goals.

 **Common anti-patterns:**
+  You only use manual log file searching for metrics.
+  You only publish metrics to internal tools.
+  You only use the default metrics recorded by your selected monitoring software.
+  You only review metrics when there is an issue.

 **Benefits of establishing this best practice:** To monitor the performance of your workloads, you must record multiple performance metrics over a period of time. These metrics allow you to detect anomalies in performance. They will also help gauge performance against business metrics to ensure that you are meeting your workload needs.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Identify, collect, aggregate, and correlate compute-related metrics. Using a service such as Amazon CloudWatch, can make the implementation quicker and easier to maintain. In addition to the default metrics recorded, identify and track additional system-level metrics within your workload. Record data such as CPU utilization, memory, disk I/O, and network inbound and outbound metrics to gain insight into utilization levels or bottlenecks. This data is crucial to understand how the workload is performing and how the compute solution is utilized. Use these metrics as part of a data-driven approach to actively tune and optimize your workload's resources.

 **Implementation steps:**

1.  Which compute solution metrics are important to track?

   1.  [EC2 default metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)

   1.  [Amazon ECS default metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html)

   1.  [EKS default metrics](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/kubernetes-eks-metrics.html)

   1.  [Lambda default metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-access-metrics.html)

   1.  [EC2 memory and disk metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html)

1.  Do I currently have an approved logging and monitoring solution?

   1.  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

   1.  [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel/)

   1.  [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/grafana/latest/userguide/prometheus-data-source.html)

1.  Have I identified and configured my data retention policies to match my security and operational goals?

   1.  [Default data retention for CloudWatch metrics](https://aws.amazon.com/cloudwatch/faqs/#AWS_resource_.26_custom_metrics_monitoring)

   1.  [Default data retention for CloudWatch Logs](https://aws.amazon.com/cloudwatch/faqs/#Log_management)

1.  How do you deploy your metric and log aggregation agents?

   1.  [AWS Systems Manager automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html?ref=wellarchitected)

   1.  [OpenTelemetry Collector](https://aws-otel.github.io/docs/getting-started/collector)

 **Level of effort for the Implementation Plan: **There is a *medium* level of effort to identify, track, collect, aggregate, and correlate metrics from all compute resources.

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
+  [Build a Monitoring Plan](https://www.youtube.com/watch?v=OMmiGETJpfU&ref=wellarchitected)

 **Related examples:**
+  [Level 100: Monitoring with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_with_cloudwatch_dashboards/)
+  [Level 100: Monitoring Windows EC2 instance with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_windows_ec2_cloudwatch/)
+  [Level 100: Monitoring an Amazon Linux EC2 instance with CloudWatch Dashboards](https://wellarchitectedlabs.com/performance-efficiency/100_labs/100_monitoring_linux_ec2_cloudwatch/)
