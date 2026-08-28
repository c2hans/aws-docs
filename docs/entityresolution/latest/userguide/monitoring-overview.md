---
source_url: https://docs.aws.amazon.com/entityresolution/latest/userguide/monitoring-overview.html
---

# Monitoring AWS Entity Resolution
<a name="monitoring-overview"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Entity Resolution and your other AWS solutions. AWS provides the following monitoring tools to watch AWS Entity Resolution, report when something is wrong, and take automatic actions when appropriate:
+ *AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP discuss from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).
+ *Amazon CloudWatch Logs* enables you to check, store, and access your logs from Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can check information in the log files and tell you when certain thresholds are met. You can also archive your log data in highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/).

**Topics**
+ [Logging AWS Entity Resolution API calls using AWS CloudTrail](logging-using-cloudtrail.md)
+ [Monitoring and logging workflows using Amazon CloudWatch Logs](cloudwatch-logs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
