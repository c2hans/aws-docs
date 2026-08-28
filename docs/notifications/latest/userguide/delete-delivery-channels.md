---
source_url: https://docs.aws.amazon.com/notifications/latest/userguide/delete-delivery-channels.html
---

# Deleting email addresses for user-configured notifications in AWS User Notifications
<a name="delete-delivery-channels"></a>

You can delete emails used as delivery channels. When you delete an email address, it's removed from all associated notification configurations. If you delete an email address, you must verify it again if you add it back.

**Note**
You can't delete mobile devices and chat channels from the User Notifications console. You can only [remove them from notification configurations](remove-delivery-channels.md).

**To delete email addresses**

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/notifications/).

1. In the navigation panel, choose **Delivery channels**.

1. Choose **Emails**

1. Select the email addresses that you want to delete.

1. Choose **Delete**.

1. Choose **Delete** again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
