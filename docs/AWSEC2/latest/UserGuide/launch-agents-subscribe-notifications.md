---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-agents-subscribe-notifications.html
---

# Subscribe to EC2 Windows launch agent notifications
<a name="launch-agents-subscribe-notifications"></a>

Amazon SNS can notify you when new versions of the EC2 launch agents are released. Use the following procedure to subscribe to these notifications.

**Subscribe to EC2Config notifications**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. In the navigation bar, change the Region to **US East (N. Virginia)**, if necessary. You must select this Region because the SNS notifications that you are subscribing to were created in this Region.

1. In the navigation pane, choose **Subscriptions**.

1. Choose **Create subscription**.

1. In the **Create subscription** dialog box, do the following:

   1. For **Topic ARN**, use the following Amazon Resource Name (ARN) that matches the agent you want to receive notifications for:
      + **EC2Launch v2**:

        ```
        arn:aws:sns:us-east-1:309726204594:amazon-ec2launch-v2
        ```
      + **EC2Launch or EC2Config**:

        ```
        arn:aws:sns:us-east-1:801119661308:ec2-windows-ec2config
        ```

   1. For **Protocol**, choose `Email`.

   1. For **Endpoint**, enter the email address where you want to receive the notifications.

   1. Choose **Create subscription**.

1. You'll receive a email asking you to confirm your subscription. Open the email and follow the directions to complete your subscription.

Whenever a new version of the launch agent is released, we send notifications to subscribers. If you no longer want to receive these notifications, use the following procedure to unsubscribe.

**Unsubscribe from launch agent notifications**

1. Open the Amazon SNS console.

1. In the navigation pane, choose **Subscriptions**.

1. Select the subscription and then choose **Actions**, **Delete subscriptions**. When prompted for confirmation, choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
