---
source_url: https://docs.aws.amazon.com/route53globalresolver/1.0/userguide/monitoring.html
---

# Monitoring DNS activity and performance with Amazon Route 53 Global Resolver
<a name="monitoring"></a>

Amazon Route 53 Global Resolver provides comprehensive visibility into DNS activity across your organization, enabling you to identify security threats, analyze client device behavior, and maintain compliance. This chapter covers both the monitoring tools available and detailed procedures for setting up DNS monitoring, configuring logging destinations, and analyzing DNS data to investigate threats and optimize performance.

AWS provides these monitoring tools to help you maintain secure, reliable DNS service:
+ *Amazon CloudWatch* tracks DNS query volumes, response times, and security events in real time. Create dashboards to monitor DNS performance across locations and set up alarms to notify you when query volumes spike or response times increase that you specify. For Amazon Route 53 Global Resolver, you can monitor query volumes, response times, and filtering activity. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ *Amazon CloudWatch Logs* enables you to monitor, store, and access your log files from Amazon EC2 instances, CloudTrail, and other sources. Amazon Route 53 Global Resolver can deliver DNS query logs directly to CloudWatch Logs for real-time monitoring and analysis. You can also archive your log data in highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/).
+ *Amazon EventBridge* can be used to automate your AWS services and respond automatically to system events, such as application availability issues or resource changes. Events from AWS services are delivered to EventBridge in near real time. You can write simple rules to indicate which events are of interest to you and which automated actions to take when an event matches a rule. For more information, see [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/).
+ *AWS CloudTrail* captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

**Topics**
+ [CloudWatch metrics](cloudwatch-metrics.md)
+ [Security monitoring](security-monitoring.md)
+ [EventBridge events](eventbridge-events.md)
+ [Gain DNS visibility](gain-visibility-into-dns-activity.md)
+ [Configure DNS monitoring](configure-dns-monitoring.md)
