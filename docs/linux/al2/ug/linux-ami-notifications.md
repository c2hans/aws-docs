---
source_url: https://docs.aws.amazon.com/linux/al2/ug/linux-ami-notifications.html
---

# AL2 AMI release notifications
<a name="linux-ami-notifications"></a>

To be notified when new Amazon Linux AMIs are released, you can subscribe using Amazon SNS.

For information about subscribing to notifications for AL2023, see [Receiving notifications on new updates](https://docs.aws.amazon.com/linux/al2023/ug/receive-update-notification.html) in the *Amazon Linux 2023 User Guide*.

**Note**
Standard support for AL1 ended on December 31, 2020. The AL1 maintenance support phase ended December 31, 2023. For more information about the AL1 EOL and maintenance support, see the blog post [Update on Amazon Linux AMI end-of-life](https://aws.amazon.com/blogs/aws/update-on-amazon-linux-ami-end-of-life/).

**To subscribe to Amazon Linux notifications**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. In the navigation bar, change the Region to **US East (N. Virginia)**, if necessary. You must select the Region in which the SNS notification that you are subscribing to was created.

1. In the navigation pane, choose **Subscriptions**, **Create subscription**.

1. For the **Create subscription** dialog box, do the following:

   1. [AL2] For **Topic ARN**, copy and paste the following Amazon Resource Name (ARN): **arn:aws:sns:us-east-1:137112412989:amazon-linux-2-ami-updates**.

   1. [Amazon Linux] For **Topic ARN**, copy and paste the following Amazon Resource Name (ARN): **arn:aws:sns:us-east-1:137112412989:amazon-linux-ami-updates**.

   1. For **Protocol**, choose **Email**.

   1. For **Endpoint**, enter an email address that you can use to receive the notifications.

   1. Choose **Create subscription**.

1. You receive a confirmation email with the subject line "AWS Notification - Subscription Confirmation". Open the email and choose **Confirm subscription** to complete your subscription.

Whenever AMIs are released, we send notifications to the subscribers of the corresponding topic. To stop receiving these notifications, use the following procedure to unsubscribe.

**To unsubscribe from Amazon Linux notifications**

1. Open the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home).

1. In the navigation bar, change the Region to **US East (N. Virginia)**, if necessary. You must use the Region in which the SNS notification was created.

1. In the navigation pane, choose **Subscriptions**, select the subscription, and choose **Actions**, **Delete subscriptions**.

1. When prompted for confirmation, choose **Delete**.

**Amazon Linux AMI SNS message format**
The schema for the SNS message is as follows.

```
{
    "description": "Validates output from AMI Release SNS message",
    "type": "object",
    "properties": {
        "v1": {
            "type": "object",
            "properties": {
                "ReleaseVersion": {
                    "description": "Major release (ex. 2018.03)",
                    "type": "string"
                },
                "ImageVersion": {
                    "description": "Full release (ex. 2018.03.0.20180412)",
                    "type": "string"
                },
                "ReleaseNotes": {
                    "description": "Human-readable string with extra information",
                    "type": "string"
                },
                "Regions": {
                    "type": "object",
                    "description": "Each key will be a region name (ex. us-east-1)",
                    "additionalProperties": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "Name": {
                                    "description": "AMI Name (ex. amzn-ami-hvm-2018.03.0.20180412-x86_64-gp2)",
                                    "type": "string"
                                },
                                "ImageId": {
                                    "description": "AMI Name (ex.ami-467ca739)",
                                    "type": "string"
                                }
                            },
                            "required": [
                                "Name",
                                "ImageId"
                            ]
                        }
                    }
                }
            },
            "required": [
                "ReleaseVersion",
                "ImageVersion",
                "ReleaseNotes",
                "Regions"
            ]
        }
    },
    "required": [
        "v1"
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Linux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query linux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
