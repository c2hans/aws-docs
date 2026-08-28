---
source_url: https://docs.aws.amazon.com/step-functions/latest/dg/using-user-notifications-sfn.html
---

# Setting up Step Functions event notification using AWS User Notifications
<a name="using-user-notifications-sfn"></a>

You can use [AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is.html) to set up delivery channels to get notified about AWS Step Functions events. You receive a notification when an event matches a rule that you specify. You can receive notifications for events through multiple channels, including email, [Amazon Q Developer in chat applications](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) chat notifications, or [AWS Console Mobile Application](https://docs.aws.amazon.com/consolemobileapp/latest/userguide/what-is-consolemobileapp.html) push notifications. You can also see notifications in the [Console Notifications Center](https://console.aws.amazon.com/notifications/). User Notifications supports aggregation, which can reduce the number of notifications you receive during specific events.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Step Functions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query step-functions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
