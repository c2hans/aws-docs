---
source_url: https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications-sns.html
---

# Receiving Amazon SES notifications using Amazon SNS
<a name="monitor-sending-activity-using-notifications-sns"></a>

You can configure Amazon SES to notify an Amazon SNS topic when you receive bounces or complaints, or when emails are delivered. Amazon SNS notifications are in [JavaScript Object Notation (JSON)](http://www.json.org) format, which enables you to process them programmatically.

In order to send email using Amazon SES, you must configure it to send bounce and complaint notifications by using one of the following methods:
+ By sending notifications to an Amazon SNS topic. The procedure for setting up this type of notification is included in this section.
+ By enabling email feedback forwarding. For more information, see [Receiving Amazon SES notifications through email](monitor-sending-activity-using-notifications-email.md).
+ By publishing event notifications. For more information, see [Monitor email sending using Amazon SES event publishing](monitor-using-event-publishing.md).

**Important**
See [Setting up event notifications for Amazon SES](monitor-sending-activity-using-notifications.md) for important information about notifications.

**Topics**
+ [Configuring Amazon SNS notifications for Amazon SES](configure-sns-notifications.md)
+ [Amazon SNS notification contents for Amazon SES](notification-contents.md)
+ [Amazon SNS notification examples for Amazon SES](notification-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
