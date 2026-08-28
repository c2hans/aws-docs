---
source_url: https://docs.aws.amazon.com/notifications/latest/userguide/nhr-add-remove.html
---

# Adding or removing a notification hub in AWS User Notifications
<a name="nhr-add-remove"></a>

You can add or remove a notification hub using the AWS Management Console. When you add a new notification hub, User Notifications replicates new notifications into that Region. User Notifications doesn’t backfill earlier notifications. When you remove a notification hub, User Notifications stops replicating new notifications into that Region. User Notifications doesn’t remove previous notifications from that Region. However, notifications expire 90 days after they are generated.

**To add or remove notification hubs**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/).

   1. In the navigation pane, choose **Notification hubs**.

1. Choose **Edit**.

1. Either add Regions by selecting them or remove Regions by choosing the **×** next to a Region.

1. Choose **Update**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
