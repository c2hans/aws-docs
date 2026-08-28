---
source_url: https://docs.aws.amazon.com/sns/latest/dg/sns-logging-monitoring.html
---

# Logging and monitoring in Amazon SNS
<a name="sns-logging-monitoring"></a>

Amazon SNS allows you to track and monitor messaging activity by logging API calls with CloudTrail and monitoring topics with CloudWatch. These tools help you gain insights into message delivery, troubleshoot issues, and ensure the health of your messaging workflows. This topic covers the following:
+ [Logging AWS SNS API calls using AWS CloudTrail](logging-using-cloudtrail.md). This logging enables you to track the actions performed on your Amazon SNS topics, such as topic creation, subscription management, and message publishing. By analyzing CloudTrail logs, you can identify who made specific API requests and when those requests were made, helping you audit and troubleshoot your Amazon SNS usage.
+ [Monitoring Amazon SNS topics using CloudWatch](sns-monitoring-using-cloudwatch.md). CloudWatch provides metrics that allow you to observe the performance and health of your Amazon SNS topics in real time. Set up alarms based on these metrics, enabling you to respond promptly to any anomalies, such as delivery failures or high message latency. This monitoring capability ensures that you can maintain the reliability of your SNS-based messaging system by proactively addressing potential issues.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
