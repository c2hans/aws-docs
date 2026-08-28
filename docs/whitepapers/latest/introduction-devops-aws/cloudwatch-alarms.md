---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/cloudwatch-alarms.html
---

# Amazon CloudWatch Alarms
<a name="cloudwatch-alarms"></a>

You can set up alarms using [Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) based on the metrics collected by Amazon CloudWatch metrics. The alarm can then send a notification to Amazon SNS topic, or initiate Auto Scaling actions. An alarm requires period (length of the time to evaluate a metric), evaluation period (number of the most recent data points), and datapoints to alarm (number of data points within the evaluation period).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
