---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/monitoring.html
---

# Logging and monitoring in MediaPackage
<a name="monitoring"></a>

Monitoring is an important part of maintaining the reliability, availability, and performance of MediaPackage and your other AWS solutions. AWS provides the following monitoring tools to watch MediaPackage, report when something is wrong, and take automatic actions when appropriate:
+ *Amazon CloudWatch* monitors your AWS resources and the applications that you run on AWS in real-time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2 instances and automatically launch new instances when needed. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ *AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

**Topics**
+ [Monitoring AWS Elemental MediaPackage with Amazon CloudWatch metrics](monitoring-cloudwatch.md)
+ [Monitoring AWS Elemental MediaPackage with EventBridge events](monitoring-eventbridge-events.md)
+ [Logging AWS Elemental MediaPackage API calls with AWS CloudTrail](logging-using-cloudtrail.md)
+ [Access logging](access-logging.md)
+ [Monitoring manifest update time in AWS Elemental MediaPackage](monitoring-manifest-last-updated.md)
+ [MediaPackage response headers](response-headers.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
