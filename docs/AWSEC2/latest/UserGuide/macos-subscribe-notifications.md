---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/macos-subscribe-notifications.html
---

# Subscribe to macOS AMI notifications
<a name="macos-subscribe-notifications"></a>

To be notified when new AMIs are released or when bridgeOS has been updated, subscribe for notifications using Amazon SNS.

For more information about EC2 macOS AMIs, see [Amazon EC2 macOS AMIs release notes](macos-ami-overview.md).

**To subscribe to macOS AMI notifications**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. In the navigation bar, change the Region to **US East (N. Virginia)**, if necessary. You must use this Region because the SNS notifications that you are subscribing to were created in this Region.

1. In the navigation pane, choose **Subscriptions**.

1. Choose **Create subscription**.

1. For the **Create subscription** dialog box, do the following:

   1. For **Topic ARN**, copy and paste one of the following Amazon Resource Names (ARNs):
      + **arn:aws:sns:us-east-1:898855652048:amazon-ec2-macos-ami-updates**
      + **arn:aws:sns:us-east-1:898855652048:amazon-ec2-bridgeos-updates**

   1. For **Protocol**, choose one of the following:
      + **Email:**

        For **Endpoint**, type an email address that you can use to receive the notifications. After you create your subscription you'll receive a confirmation message with the subject line `AWS Notification - Subscription Confirmation`. Open the email and choose **Confirm subscription** to complete your subscription
      + **SMS:**

        For **Endpoint**, type a phone number that you can use to receive the notifications.
      + **AWS Lambda, Amazon SQS, Amazon Data Firehose** (*Notifications come in JSON format*):

        For **Endpoint**, enter the ARN for the Lambda function, SQS queue, or Firehose stream you can use to receive the notifications.

   1. Choose **Create subscription**.

Whenever macOS AMIs are released, we send notifications to the subscribers of the `amazon-ec2-macos-ami-updates` topic. Whenever bridgeOS is updated, we send notifications to the subscribers of the `amazon-ec2-bridgeos-updates` topic. If you no longer want to receive these notifications, use the following procedure to unsubscribe.

**To unsubscribe from macOS AMI notifications**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. In the navigation bar, change the Region to **US East (N. Virginia)**, if necessary. You must use this Region because the SNS notifications were created in this Region.

1. In the navigation pane, choose **Subscriptions**.

1. Select the subscriptions and then choose **Actions**, **Delete subscriptions** When prompted for confirmation, choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
