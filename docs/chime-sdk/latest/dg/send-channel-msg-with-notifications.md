---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/send-channel-msg-with-notifications.html
---

# Send a channel message with notifications enabled in Amazon Chime SDK messaging
<a name="send-channel-msg-with-notifications"></a>

The [SendChannelMessage](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SendChannelMessage.html) API has an optional `PushNotification` attribute that the Amazon Chime SDK uses to build the push notification to send to Amazon Pinpoint. Currently, the Amazon Chime SDK only supports the notification title and body fields.

The Amazon Chime SDK also supports APNs VoIP pushes. To send a push notification as an APNs VoIP push, set the type in the `PushNotification` attribute to VOIP.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
