---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/sns.html
---

# Track Alerts Through Amazon Simple Notification Service
<a name="sns"></a>

Amazon Simple Notification Service (Amazon SNS) is a web service that enables applications, end-users, and devices to send and receive notifications instantly from the cloud. For more information, see *[Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/)*.

AWS Control Tower uses Amazon SNS to send programmatic alerts to the email addresses of your management account and your audit account. These alerts help you prevent drift within your landing zone. For more information, see [Detect and resolve drift in AWS Control Tower](drift.md).

We also use Amazon Simple Notification Service to send compliance notifications from AWS Config.

**Tip**
One of the best ways to receive AWS Control Tower control compliance notifications (in your audit account) is to subscribe to `AggregateConfigurationNotifications`. It is a service that helps you inspect compliance. It gives you real data about AWS Config rules going out of compliance. AWS Config automatically maintains the list of accounts in your OU.
You must subscribe manually, using email or any type of subscription that SNS allows. The statement `arn:aws:sns:{{homeregion}}:{{account}}:aws-controltower-AggregateSecurityNotifications` leads to your audit account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
