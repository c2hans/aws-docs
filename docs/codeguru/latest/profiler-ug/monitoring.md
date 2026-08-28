---
source_url: https://docs.aws.amazon.com/codeguru/latest/profiler-ug/monitoring.html
---

# Monitoring Amazon CodeGuru Profiler with Amazon CloudWatch
<a name="monitoring"></a>

 You can use Amazon CloudWatch to monitor the number of recommendations created on your profiling groups over time. You can set a CloudWatch alarm that notifies you when the number of recommendations on a profiling group exceeds a threshold you set.

 For more information about creating and using CloudWatch alarms and metrics, see [Using Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html).

 You can track the following metric per profiling group.

|   Metric   |   Description   |
| --- | --- |
| Recommendations | The number of recommendations for a profiling group.<br />Units: Count<br />Valid CloudWatch statistic: Maximum<br />Valid CloudWatch period: Hourly |

**Topics**
+ [Monitoring profiling groups with CloudWatch metrics](cloudwatch-metric.md)
+ [Monitoring profiling groups with CloudWatch alarms](cloudwatch-alarm.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
