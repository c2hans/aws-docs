---
source_url: https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-rules.html
---

# Working with notification rules
<a name="notification-rules"></a>

A notification rule is where you configure which events you want users to receive notifications about and specify the targets that receive those notifications. You can send notifications directly to users through Amazon SNS, or through AWS Chatbot clients configured for Slack or Microsoft Teams channels. If you want to extend the reach of notifications, you can manually configure integration between notifications and AWS Chatbot so that notifications are sent to Amazon Chime chatrooms. For more information, see [Targets](concepts.md#targets) and [To integrate notifications with AWS Chatbot and Amazon Chime](notifications-chatbot.md#notifications-chatbot-chime).

![Creating a notification rule for a repository in the AWS Developer Tools console.](http://docs.aws.amazon.com/dtconsole/latest/userguide/images/create-notification-rule-repository.png)

You can use the Developer Tools console or the AWS CLI to create and manage notification rules.

**Topics**
+ [Create a notification rule](notification-rule-create.md)
+ [View notification rules](notification-rule-view.md)
+ [Edit a notification rule](notification-rule-edit.md)
+ [Enable or disable notifications for a notification rule](notification-rule-enable-disable.md)
+ [Delete a notification rule](notification-rule-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Developer Tools Console. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dtconsole` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
