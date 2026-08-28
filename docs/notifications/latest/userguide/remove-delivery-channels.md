---
source_url: https://docs.aws.amazon.com/notifications/latest/userguide/remove-delivery-channels.html
---

# Removing delivery channels in AWS User Notifications
<a name="remove-delivery-channels"></a>

You can remove delivery channels from notification configurations and toggle off AWS managed notification subscription categories from a delivery channel's detail view. When you remove a delivery channel, notifications are no longer sent to that location.

------
#### [ Emails ]

**To remove delivery channels**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/).

1. In the navigation panel, choose **Delivery channels**.

1. Choose **Emails**.

1. Choose the **Name** of the email address that you want to remove.

1. In **Notification configurations**, select the notification configurations you want to remove the email address from.

1. Choose **Remove**.

1.  In **AWS managed notifications subscriptions**, toggle each relevant category off.

------
#### [ Mobile devices ]

**To remove delivery channels**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/).

1. In the navigation panel, choose **Delivery channels**.

1. Choose **Mobile devices**.

1. Choose the **Name** of the mobile device that you want to remove.

1. In **Notification configurations**, select the notification configurations you want to remove the mobile device from.

1. Choose **Remove**.

1.  In **AWS managed notifications subscriptions**, toggle each relevant category off.

**Note**
For more information about the AWS Console Mobile Application, see [What is the AWS Console Mobile Application?](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/what-is-consolemobileapp.html) in the *AWS Console Mobile Application User Guide*.

------
#### [ Chat channels ]

**To remove delivery channels**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/).

1. In the navigation panel, choose **Delivery channels**.

1. Choose **Chat channels**.

1. Choose the **Name** of the chat channel that you want to remove.

1. In **Notification configurations**, select the notification configurations you want to remove the chat channel from.

1. Choose **Remove**.

1.  In **AWS managed notifications subscriptions**, toggle each relevant category off.

**Note**
For more information about Amazon Q Developer in chat applications, see [What is Amazon Q Developer in chat applications?](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) in the *Amazon Q Developer in chat applications Administrator Guide*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
