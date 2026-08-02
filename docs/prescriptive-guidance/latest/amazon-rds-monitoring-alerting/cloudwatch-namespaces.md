---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/cloudwatch-namespaces.html
---

# Amazon CloudWatch namespaces
<a name="cloudwatch-namespaces"></a>

Amazon RDS integrates with [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html), which is a monitoring and alerting service for cloud resources and applications that run on AWS. Amazon RDS automatically collects metrics, log files, traces, and events about the operation, utilization, performance, and health of DB instances, and sends them to CloudWatch for long-term storage, analysis, and alerting.

Amazon RDS for MySQL and Amazon RDS for MariaDB automatically publish a default set of metrics to Amazon CloudWatch in one-minute intervals without additional charge. Those metrics are collected into two *namespaces*, which are containers for metrics:
+ The [AWS/RDS namespace](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html#rds-cw-metrics-instance) includes DB instance-level metrics. Examples include `BinLogDiskUsage` (the amount of disk space occupied by binary logs), `CPUUtilization` (the percentage of CPU utilization), `DatabaseConnections` (the number of client network connections to the DB instance), and many more.
+ The [AWS/Usage namespace](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html#rds-metrics-usage) includes account-level usage metrics, which are used to determine if you are operating within your [Amazon RDS service quotas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html#RDS_Limits.Limits). Examples include `DBInstances` (the number of DB instances in your AWS account or Region), `DBSubnetGroups` (the number of DB subnet groups in your AWS account or Region), and `ManualSnapshots` (the number of manually created database snapshots in your AWS account or Region).

CloudWatch retains metric data as follows:
+ 3 hours: High-resolution custom metrics with a period of less than 60 seconds are retained for 3 hours. After 3 hours, the data points are aggregated into 1-minute period metrics and kept for 15 days.
+ 15 days: Data points with a period of 60 seconds (1 minute) are retained for 15 days. After 15 days, the data points are aggregated into 5-minute period metrics and kept for 63 days.
+ 63 days: Data points with a period of 300 seconds (5 minutes) are retained for 63 days. After 63 days, the data points are aggregated into 1-hour period metrics and kept for 15 months.
+ 15 months: Data points with a period of 3,600 seconds (1 hour) are available for 15 months (455 days).

For more information, see [Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Metric) in the CloudWatch documentation.
