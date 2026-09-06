---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/cloudwatch-logs.html
---

# Amazon CloudWatch Logs
<a name="cloudwatch-logs"></a>

[Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) enables you to centralize the logs from all of your systems, applications, and AWS services that you use, in a single, highly scalable service. You can then easily view them, search them for specific error codes or patterns, filter them based on specific fields, or archive them securely for future analysis. You can see all of your log events, regardless of their source, as a single and consistent flow of events ordered by time. You can query them and sort them, group them by specific fields, create custom computations, and visualize log data in dashboards.

## Using CloudWatch Logs
<a name="using-cloudwatch-logs"></a>

In CloudWatch Logs, log events are organized into log streams and log groups. A *log stream* is a sequence of log events that share the same source. More specifically, a log stream is generally intended to represent the sequence of events coming from the application instance or resource being monitored. *Log groups* define one or more log streams that share the same retention, monitoring, and access control settings. Each log stream must belong to at least one log group. For more information, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) (CloudWatch Logs documentation).

You can use CloudWatch Logs Insights to search and analyze your log data in Amazon CloudWatch Logs. You can perform queries to help you more efficiently and effectively respond to operational issues. If an issue occurs, you can use CloudWatch Logs Insights to identify potential causes and validate deployed fixes. For more information, see [Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) (CloudWatch Logs documentation).

You can search and filter the log data coming into CloudWatch Logs by creating one or more *metric filters*. Metric filters define the terms and patterns to look for in log data as it is sent to CloudWatch Logs. CloudWatch Logs uses these metric filters to turn log data into numerical CloudWatch metrics that you can graph or set an alarm on. For more information, see [Creating metrics from log events using filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) (CloudWatch Logs documentation).

## Use cases for CloudWatch Logs
<a name="cloudwatch-logs-use-cases"></a>
+ **Monitoring CloudTrail logs** ­– You can create alarms in CloudWatch and receive notifications of particular API activity, as captured by CloudTrail, and use the notification to perform troubleshooting. For more information, see [Sending CloudTrail Events to CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cw_send_ct_events.html) (CloudTrail documentation).
+ **Logging AWS API calls** – If you have a third-party monitoring solution in place, you can use CloudWatch Logs to log AWS API calls. You set up the third-party monitoring service to evaluate this log and the and the application-level APIs.
+ **Configuring log retention** – By default, logs in CloudWatch Logs are kept indefinitely and never expire. You can adjust the retention policy for each log group, keeping the indefinite retention, or choosing a retention period between one day and 10 years.
+ **Archiving and storing logs** – You can use CloudWatch Logs to store your log data in highly durable storage. The CloudWatch Logs agent sends both rotated and non-rotated log data into the log service. You can then access the raw log data when you need it.
