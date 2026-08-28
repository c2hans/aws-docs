---
source_url: https://docs.aws.amazon.com/ses/latest/dg/security-monitoring-overview.html
---

# Logging and monitoring in Amazon SES
<a name="security-monitoring-overview"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon SES and your AWS solutions. AWS provides tools to help you monitor Amazon SES and respond to potential incidents.
+ *Amazon CloudWatch* monitors your AWS resources and the applications you run on AWS in real time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For more information, see [Retrieving Amazon SES event data from CloudWatch](event-publishing-retrieving-cloudwatch.md) and [Creating reputation monitoring alarms using CloudWatch](reputationdashboard-cloudwatch-alarm.md).
+ *AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see [Logging Amazon SES API calls with AWS CloudTrail](logging-using-cloudtrail.md).
+ Amazon SES *email sending events* can help you fine-tune your email sending strategy. Amazon SES captures detailed information, including the numbers of sends, deliveries, opens, clicks, bounces, complaints, and rejections. For more information, see [Monitoring sending activity](monitor-sending-activity.md).
+ Amazon SES *reputation metrics* tracks the bounce and complaint rates for your account. For more information, see [Monitoring sender reputation](monitor-sender-reputation.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
