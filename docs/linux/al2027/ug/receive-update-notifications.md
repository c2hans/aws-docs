---
source_url: https://docs.aws.amazon.com/linux/al2027/ug/receive-update-notifications.html
---

# Receive notifications on new updates
<a name="receive-update-notifications"></a>

**AL2027 Preview**
AL2027 is currently available for preview. It is intended for evaluation and testing only and is not recommended for production workloads.

You can find out about new AL2027 releases in the following ways:
+ Each release is documented in the [AL2027 Release Notes](https://docs.aws.amazon.com/linux/al2027/release-notes/relnotes.html), including the package changes it contains.
+ On a running instance, the `dnf check-release-update` command reports when a newer release than the one the system is locked to is available. For more information, see [Checking for newer repository versions with `dnf check-release-update`](manage-updates.md#dnf-repository-updates).
+ An Amazon SNS topic sends a notification each time we release a new AL2027 AMI. This page includes the subscription steps.

[Amazon SNS](https://aws.amazon.com/sns/) publishes a notification to the following topic each time we release a new AL2027 AMI.

```
arn:aws:sns:us-east-1:137112412989:amazon-linux-2027-ami-updates
```

The message includes the version of the new AMI.

You can receive these messages in several ways. We recommend the following method.

1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns/v3/home).

1. In the navigation bar, change the AWS Region to **US East (N. Virginia)**, if necessary. You subscribe in the Region that hosts the topic.

1. In the navigation pane, choose **Subscriptions**, **Create subscription**.

1. For the **Create subscription** dialog box, do the following:

   1. For **Topic ARN**, copy and paste the following **Amazon Resource Name** (ARN): **arn:aws:sns:us-east-1:137112412989:amazon-linux-2027-ami-updates**.

   1. For **Protocol**, choose **Email**.

   1. For **Endpoint**, enter an email address that you can use to receive the notifications.

   1. Choose **Create subscription**.

1. You receive a confirmation email with the subject line "AWS Notification - Subscription Confirmation". Open the email and choose **Confirm subscription** to complete your subscription.
