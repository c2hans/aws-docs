---
source_url: https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-target-delete.html
---

# Delete a notification rule target
<a name="notification-target-delete"></a>

You can delete a target if it is no longer needed. A resource can only have 10 notification rule targets configured for it, so deleting unneeded targets can help create room for other targets you might want to add to that notification rule.

**Note**
Deleting a notification rule target removes the target from all notification rules configured to use it as a target, but it does not delete the target itself.<a name="notification-target-delete-console"></a>

# To delete a notification rule target (console)
<a name="notification-target-delete-console"></a>

1. Open the AWS Developer Tools console at [https://console.aws.amazon.com/codesuite/settings/notifications](https://console.aws.amazon.com/codesuite/settings/notifications/).

1. In the navigation bar, expand **Settings**, and then choose **Notification rules**.

1. In **Notification rule targets**, review the list of targets configured for your resources in your AWS account in the AWS Region where you are currently signed in. Use the selector to change the AWS Region.

1. Choose the notification rule target, and then choose **Delete**.

1. Type **delete**, and then choose **Delete**.<a name="notification-target-delete-cli"></a>

# To delete a notification rule target (AWS CLI)
<a name="notification-target-delete-cli"></a>

1. At a terminal or command prompt, run the **delete-target** command, specifying the ARN of the target. For example, the following command deletes a target that uses an Amazon SNS topic.

   ```
   aws codestar-notifications delete-target --target-address arn:aws:sns:{{us-east-1}}:{{123456789012}}:{{MyNotificationTopic}}
   ```

1. If successful, the command returns nothing. If unsuccessful, the command returns an error. The most common error is that the topic is the target for one or more notification rules.

   ```
   An error occurred (ValidationException) when calling the DeleteTarget operation: Unsubscribe target before deleting.
   ```

   You can use the `--force-unsubscribe-all` parameter to remove the target from all notification rules configured to use it as a target, and then delete the target.

   ```
   aws codestar-notifications delete-target --target-address arn:aws:sns:{{us-east-1}}:{{123456789012}}:{{MyNotificationTopic}} --force-unsubscribe-all
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Developer Tools Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dtconsole` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
