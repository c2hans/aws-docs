---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/receive-update-notification.html
---

# Receive notifications on new updates
<a name="receive-update-notification"></a>

You can receive notifications whenever a new AL2023 AMI is released. Notifications are published with [Amazon SNS](https://aws.amazon.com/sns/) using the following topic.

```
arn:aws:sns:us-east-1:137112412989:amazon-linux-2023-ami-updates
```

Messages are posted here when a new AL2023 AMI is published. The version of the AMI will be included in the message.

These messages can be received using several different methods. We recommend that you use the following method.

1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns/v3/home).

1. In the navigation bar, change the AWS Region to **US East (N. Virginia)**, if necessary. You must select the Region where the SNS notification that you're subscribing to was created.

1. In the navigation pane, choose **Subscriptions**, **Create subscription**.

1. For the **Create subscription** dialog box, do the following:

   1. For **Topic ARN**, copy and paste the following **Amazon Resource Name** (ARN): **arn:aws:sns:us-east-1:137112412989:amazon-linux-2023-ami-updates**.

   1. For **Protocol**, choose **Email**.

   1. For **Endpoint**, enter an email address that you can use to receive the notifications.

   1. Choose **Create subscription**.

1. You receive a confirmation email with the subject line "AWS Notification - Subscription Confirmation". Open the email and choose **Confirm subscription** to complete your subscription.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
