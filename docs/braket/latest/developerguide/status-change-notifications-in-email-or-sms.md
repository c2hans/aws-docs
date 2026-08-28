---
source_url: https://docs.aws.amazon.com/braket/latest/developerguide/status-change-notifications-in-email-or-sms.html
---

# Set up email or SMS notifications
<a name="status-change-notifications-in-email-or-sms"></a>

Amazon Braket sends events to Amazon EventBridge when the availability of a QPU changes or when the state of your quantum task changes. Follow these steps to receive device and quantum task status change notifications by email or SMS message:

1. Create an Amazon SNS topic and a subscription to email or SMS. Availability of email or SMS depends on your Region. For more information, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) and [Sending SMS messages](https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-phone-number-as-subscriber.html).

1. Create a rule in EventBridge that triggers the notifications to your SNS topic. For more information, see [Monitoring Amazon Braket with Amazon EventBridge](braket-monitor-eventbridge.md).

## (Optional) Set up SNS notifications
<a name="braket-sns-notifications"></a>

You can set up notifications through the Amazon Simple Notification Service (SNS) so that you receive an alert when your Amazon Braket quantum task is complete. Active notifications are useful if you expect a long wait time; for example, when you submit a large quantum task or when you submit a quantum task outside of a device's availability window. If you do not want to wait for the quantum task to complete, you can set up an SNS notification.

An Amazon Braket notebook walks you through the setup steps. For more information, see [the Amazon Braket examples on GitHub](https://github.com/aws/amazon-braket-examples) and, specifically, [the example notebook for setting up notifications](https://github.com/aws/amazon-braket-examples/tree/main/examples/braket_features).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Braket. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query braket` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
