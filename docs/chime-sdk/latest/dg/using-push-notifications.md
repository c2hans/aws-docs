---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/using-push-notifications.html
---

# Using mobile push notifications for Amazon Chime SDK messaging to receive messages
<a name="using-push-notifications"></a>

You can configure Amazon Chime SDK Messaging to send channel messages to mobile push notification channels. The Amazon Chime SDK requires an Amazon Pinpoint application configured for push notifications. Your Amazon Pinpoint application must meet these prerequisites:
+ Your Amazon Pinpoint application must have at least an FCM or APNS channel configured and enabled.
+ Your Amazon Pinpoint application must reside in the same AWS account and region as your Amazon Chime SDK app instance.

**Note**
By default, all the members of a push notification channel receive the push notifications, including message senders. However, you can set a filter rule that prevents messages from going to senders. For more information, see [Using filter rules to filter messages for Amazon Chime SDK messaging](filter-msgs.md), later in this section.

**Topics**
+ [Create an Amazon Pinpoint application for Amazon Chime SDK messaging](create-pinpoint.md)
+ [Create a service role for Amazon Chime SDK messaging](create-service-role.md)
+ [Register a mobile device endpoint as an App Instance user for Amazon Chime SDK messaging](register-endpoint.md)
+ [Send a channel message with notifications enabled in Amazon Chime SDK messaging](send-channel-msg-with-notifications.md)
+ [Receiving push notifications in Amazon Chime SDK messaging](receive-notifications.md)
+ [Debugging push notification failures for Amazon Chime SDK messaging](debug-notifications.md)
+ [Using filter rules to filter messages for Amazon Chime SDK messaging](filter-msgs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
