---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/cloudwatch-dashboards.html
---

# CloudWatch alarms and dashboards
<a name="cloudwatch-dashboards"></a>

You can use [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to watch a specific Amazon RDS metric over a period of time. For example, you can monitor `FreeStorageSpace`, and then perform one or more actions if the value of the metric breaches the threshold that you set. If you set the threshold to 250 MB and the free storage space is 200 MB (less than the threshold), the alarm will be activated and can trigger an action to automatically provision additional storage for the Amazon RDS DB instance. The alarm can also  send a notification SMS to the DBA by using Amazon Simple Notification Service (Amazon SNS). The following diagram illustrates this process.

![Using CloudWatch alarms to monitor Amazon RDS metrics](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/27885245-c524-4c42-93ec-df53f0efa9f3.png)

Amazon CloudWatch also provides [dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html), which you can use to create, customize, interact with, and save customized views (graphs) of the metrics. You can also use [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) to create a dashboard for monitoring the slow query log and error log, and to receive alerts if a specific pattern has been detected in those logs. The following screen illustration shows an example CloudWatch dashboard.

![Using CloudWatch dashboards to monitor metrics](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/761723bb-76aa-4f97-86e7-474fb2f57051.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
