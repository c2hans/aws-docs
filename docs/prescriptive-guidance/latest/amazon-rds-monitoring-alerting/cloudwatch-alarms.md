---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/cloudwatch-alarms.html
---

# CloudWatch alarms
<a name="cloudwatch-alarms"></a>

When you operate your Amazon RDS DB instances, you want to monitor and generate alerts on different kinds of metrics, events, and traces. For MySQL and MariaDB databases, the critical sources of information are [DB instance metrics](database-instance-monitoring.md), [OS metrics](os-monitoring.md), [events, logs, and audit trails](events-logs-audit.md). We recommend that you use [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to watch a single metric over a time period that you specify.

The following example illustrates how you can set an alarm that watches the `CPUUtilization` metric (percentage of CPU utilization) on all your Amazon RDS DB instances. You configure the alarm to be triggered if the CPU utilization on any DB instance is greater than 80 percent for the evaluation period of 5 minutes.

![Setting an alarm for the CPUUtilization metric](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/bcf169c7-79df-46ad-9c7c-4be8ffe45251.png)

This means that the alarm goes into the `ALARM` state if any of your databases experiences a high CPU utilization (over 80 percent) for 5 minutes or more. The alarm remains in the `OK` state if the CPU occasionally bursts to over 80 percent utilization for a short period of time, and then drops again below the threshold. The following diagram illustrates this logic.

![Alarm states and thresholds](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/1059fe3e-eca3-437b-bef4-8a187a1d5157.png)

CloudWatch alarms support *metric* and *composite* alarms.
+ A metric alarm watches a single CloudWatch metric and can perform mathematical expressions on the metric. A metric alarm can send Amazon SNS messages, which, in turn, can take one or more actions based on the value of the metric relative to a given threshold over a number of time periods.
+ A composite alarm is based on a rule expression, which evaluates the states of multiple alarms and goes into the `ALARM` state only if all conditions of the rule are met. Composite alarms are typically used to reduce the number of unnecessary alerts. For example, you might have a composite alarm that contains several metric alarms that are configured never to take actions. The composite alarm would send an alert when all the individual metric alarms in the composite are already in the `ALARM`

CloudWatch alarms can watch only CloudWatch metrics. If you want to create an alarm based on the error, slow query, or general logs, you must create CloudWatch metrics from the logs. You can accomplish that as discussed earlier in the [OS](os-monitoring.md) monitoring and [Events, logs, and audit trails](events-logs-audit.md) sections, by using filters to [create metrics from log events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html). Similarly, to alert on Enhanced Monitoring metrics, you must create metric filters in CloudWatch from CloudWatch Logs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
