---
source_url: https://docs.aws.amazon.com/notifications/latest/userguide/uc-notifications.html
---

# User-configured notifications in AWS User Notifications
<a name="uc-notifications"></a>

User-configured notifications (UCNs) are notifications about AWS services and events that you specify by creating [notification configurations](managing-notifications.md). You can generate notifications for Amazon CloudWatch alarms, Support case, and more. You can receive UCNs through multiple channels, including the Console Notification Center (default), email, [Amazon Q Developer chat notifications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html), [AWS Console Mobile App](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/what-is-consolemobileapp.html) push notifications, or the [User Notifications API](https://docs.aws.amazon.com/notifications/latest/APIReference/Welcome.html). To receive UCNs, you must choose at least one [notification hub](notification-hubs.md) and then [ create notification configurations](getting-started.md#getting-started-step1).

**Note**
Notification hubs and notification configurations are only used with UCNs.

**Topics**
+ [Notification configurations in AWS User Notifications](managing-notifications.md)
+ [Storing, processing, and replicating notifications using notification hubs in AWS User Notifications](notification-hubs.md)
+ [Managing notifications across your organization with AWS User Notifications](managing-org-notifications.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
