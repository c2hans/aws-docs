---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/publishing-performance-insights-to-cloudwatch.html
---

# Publishing Performance Insights metrics to Amazon CloudWatch
<a name="publishing-performance-insights-to-cloudwatch"></a>

Amazon RDS Performance Insights monitors most of the DB instance metrics and dimensions and makes them available through the [Performance Insights dashboard](https://console.aws.amazon.com/rds/home#performance-insights-v20206:) on the AWS Management Console. This dashboard is well-suited for database troubleshooting and root cause analysis. However, it is not possible to create alarms in Performance Insights for performance-related metrics. If you want to create alarms based on Performance Insights metrics, those metrics must be in CloudWatch.

Performance Insights [automatically publishes metrics to CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Cloudwatch.html). You can query the same data from Performance Insights, but having the metrics in CloudWatch makes it easy to add CloudWatch alarms and add the metrics to existing CloudWatch dashboards. [Counters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html) are operating system and database performance metrics such as `os.memory.free` or `db.Locks.Innodb_row_lock_time`. The OS metrics collection depends on the Enhanced Monitoring setting. If Enhanced Monitoring is turned off, OS metrics are collected once every minute. If Enhanced Monitoring is turned on, OS metrics are collected for the selected time period. For more information, see [Turning Enhanced Monitoring on and off](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.Enabling.html#USER_Monitoring.OS.Enabling.Procedure) in the Amazon RDS documentation.

Performance Insights lets you [export the preconfigured or custom metrics dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PI_metrics_export_CW.html) for your DB instance to CloudWatch. You can export the metrics dashboard as a new dashboard or add it to an existing CloudWatch dashboard. Exporting the Performance Insights metrics dashboard to the CloudWatch dashboard gives you a unified, holistic view of your system's health by providing an overview of metrics associated with various resources in your system, such as EC2 instances, Amazon Elastic File System (Amazon EFS) resources, and Elastic Load Balancing (ELB) resources, along with your DB instance metrics.

You can use the CloudWatch `DB_PERF_INSIGHTS` metric math function to query and create alarms and graphs based on Performance Insights metrics from CloudWatch. To create an alarm on a Performance Insights metric, follow the instructions in the [CloudWatch documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_alarm_database_performance_insights.html). For example, if you want to trigger an alarm when the total active transactions in your DB instance reaches a specific threshold, follow the instructions on that page, use the following: `DB_PERF_INSIGHTS` math expression, and then choose **Apply**:

```
DB_PERF_INSIGHTS('RDS', 'db-BQ2TPYY7HG2GDFC7APMB3BVB3M', 'db.Transactions.active_transactions.avg')
```

where `db-BQ2TPYY7HG2GDFC7APMB3BVB3M` is the resource ID of your DB instance. Specify the period (for example, 1 minute) and conditions (for example, greater than 1000). To finalize the creation of the alarm, configure alarm actions, add a name and description, and preview and create the alarm.
